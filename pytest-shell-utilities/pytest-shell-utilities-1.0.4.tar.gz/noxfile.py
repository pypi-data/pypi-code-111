# Copyright 2021-2022 VMware, Inc.
# SPDX-License-Identifier: Apache-2.0
#
# pylint: disable=import-error,protected-access,line-too-long
import datetime
import gzip
import json
import os
import pathlib
import shutil
import sys
import tarfile
import tempfile

import nox
from nox.command import CommandFailed


COVERAGE_VERSION_REQUIREMENT = "coverage==6.2"
PYTEST_VERSION_REQUIREMENT = os.environ.get("PYTEST_VERSION_REQUIREMENT") or None
IS_WINDOWS = sys.platform.lower().startswith("win")
IS_DARWIN = sys.platform.lower().startswith("darwin")

if IS_WINDOWS:
    COVERAGE_FAIL_UNDER_PERCENT = 98
elif IS_DARWIN:
    COVERAGE_FAIL_UNDER_PERCENT = 98
else:
    COVERAGE_FAIL_UNDER_PERCENT = 98

# Be verbose when running under a CI context
PIP_INSTALL_SILENT = (os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS")) is None
CI_RUN = PIP_INSTALL_SILENT is False
SKIP_REQUIREMENTS_INSTALL = "SKIP_REQUIREMENTS_INSTALL" in os.environ
EXTRA_REQUIREMENTS_INSTALL = os.environ.get("EXTRA_REQUIREMENTS_INSTALL")

# Paths
REPO_ROOT = pathlib.Path(__file__).resolve().parent
# Change current directory to REPO_ROOT
os.chdir(str(REPO_ROOT))

SITECUSTOMIZE_DIR = str(REPO_ROOT / "tests" / "support" / "coverage")
ARTIFACTS_DIR = REPO_ROOT / "artifacts"
# Make sure the artifacts directory exists
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)
RUNTESTS_LOGFILE = ARTIFACTS_DIR.relative_to(REPO_ROOT) / "runtests-{}.log".format(
    datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")
)
COVERAGE_REPORT_DB = REPO_ROOT / ".coverage"
COVERAGE_REPORT_PROJECT = ARTIFACTS_DIR.relative_to(REPO_ROOT) / "coverage-project.xml"
COVERAGE_REPORT_TESTS = ARTIFACTS_DIR.relative_to(REPO_ROOT) / "coverage-tests.xml"
JUNIT_REPORT = ARTIFACTS_DIR.relative_to(REPO_ROOT) / "junit-report.xml"

# Nox options
#  Reuse existing virtualenvs
nox.options.reuse_existing_virtualenvs = True
#  Don't fail on missing interpreters
nox.options.error_on_missing_interpreters = False


def pytest_version(session):
    try:
        return session._runner._pytest_version_info
    except AttributeError:
        session_pytest_version = session_run_always(
            session,
            "python",
            "-c",
            'import sys, pkg_resources; sys.stdout.write("{}".format(pkg_resources.get_distribution("pytest").version))',
            silent=True,
            log=False,
        )
        session._runner._pytest_version_info = tuple(
            int(part) for part in session_pytest_version.split(".") if part.isdigit()
        )
    return session._runner._pytest_version_info


def python_version(session):
    try:
        return session._runner._python_version_info
    except AttributeError:
        session_python_version = session_run_always(
            session,
            "python",
            "-c",
            'import sys; sys.stdout.write("{}.{}".format(*sys.version_info));',
            silent=True,
            log=False,
        )
        session._runner._python_version_info = tuple(
            int(part) for part in session_python_version.split(".") if part.isdigit()
        )
    return session._runner._python_version_info


def session_run_always(session, *command, **kwargs):
    try:
        # Guess we weren't the only ones wanting this
        # https://github.com/theacodes/nox/pull/331
        return session.run_always(*command, **kwargs)
    except AttributeError:
        old_install_only_value = session._runner.global_config.install_only
        try:
            # Force install only to be false for the following chunk of code
            # For additional information as to why see:
            #   https://github.com/theacodes/nox/pull/181
            session._runner.global_config.install_only = False
            return session.run(*command, **kwargs)
        finally:
            session._runner.global_config.install_only = old_install_only_value


@nox.session(python=("3", "3.5", "3.6", "3.7", "3.8", "3.9"))
def tests(session):
    """
    Run tests.
    """
    env = {}
    install_arguments = ["--progress-bar=off"]
    if SKIP_REQUIREMENTS_INSTALL is False:
        # Always have the wheel package installed
        if python_version(session) < (3, 6):
            install_arguments.append("--no-python-version-warning")
            session.install(*install_arguments, "-U", "pip<21.0", silent=PIP_INSTALL_SILENT)
            coverage_requirements = ["coverage==5.2"]
        else:
            env["COVERAGE_PLUGINS_LIST"] = "coverage_conditional_plugin"
            coverage_requirements = [COVERAGE_VERSION_REQUIREMENT, "coverage-conditional-plugin"]
        session.install(*install_arguments, "wheel", silent=PIP_INSTALL_SILENT)
        session.install(
            *install_arguments,
            *coverage_requirements,
            silent=PIP_INSTALL_SILENT,
        )

        pytest_version_requirement = PYTEST_VERSION_REQUIREMENT
        if pytest_version_requirement:
            if not pytest_version_requirement.startswith("pytest"):
                pytest_version_requirement = "pytest{}".format(pytest_version_requirement)
            session.install(pytest_version_requirement, silent=PIP_INSTALL_SILENT)
        session.install(*install_arguments, "-e", ".[tests]", silent=PIP_INSTALL_SILENT)

        if EXTRA_REQUIREMENTS_INSTALL:
            session.log(
                "Installing the following extra requirements because the EXTRA_REQUIREMENTS_INSTALL "
                "environment variable was set: EXTRA_REQUIREMENTS_INSTALL='%s'",
                EXTRA_REQUIREMENTS_INSTALL,
            )
            install_command = [req.strip() for req in EXTRA_REQUIREMENTS_INSTALL.split()]
            session.install(*install_arguments, *install_command, silent=PIP_INSTALL_SILENT)

    session.run("coverage", "erase")

    python_path_env_var = os.environ.get("PYTHONPATH") or None
    if python_path_env_var is None:
        python_path_env_var = SITECUSTOMIZE_DIR
    else:
        python_path_entries = python_path_env_var.split(os.pathsep)
        if SITECUSTOMIZE_DIR in python_path_entries:
            python_path_entries.remove(SITECUSTOMIZE_DIR)
        python_path_entries.insert(0, SITECUSTOMIZE_DIR)
        python_path_env_var = os.pathsep.join(python_path_entries)

    env.update(
        {
            # The updated python path so that sitecustomize is importable
            "PYTHONPATH": python_path_env_var,
            # The full path to the .coverage data file. Makes sure we always write
            # them to the same directory
            "COVERAGE_FILE": str(COVERAGE_REPORT_DB),
            # Instruct sub processes to also run under coverage
            "COVERAGE_PROCESS_START": str(REPO_ROOT / ".coveragerc"),
        }
    )

    args = [
        "--rootdir",
        str(REPO_ROOT),
        "--log-file={}".format(RUNTESTS_LOGFILE),
        "--log-file-level=debug",
        "--show-capture=no",
        "--junitxml={}".format(JUNIT_REPORT),
        "--showlocals",
        "--strict-markers",
        "-ra",
        "-s",
    ]
    if pytest_version(session) > (6, 2):
        args.append("--lsof")
    if session._runner.global_config.forcecolor:
        args.append("--color=yes")
    if not session.posargs:
        args.append("tests/")
    else:
        for arg in session.posargs:
            if arg.startswith("--color") and session._runner.global_config.forcecolor:
                args.remove("--color=yes")
            args.append(arg)

    try:
        session.run("coverage", "run", "-m", "pytest", *args, env=env)
    finally:
        # Always combine and generate the XML coverage report
        try:
            session.run("coverage", "combine")
        except CommandFailed:
            # Sometimes some of the coverage files are corrupt which would
            # trigger a CommandFailed exception
            pass
        # Generate report for project code coverage
        session.run(
            "coverage",
            "xml",
            "-o",
            str(COVERAGE_REPORT_PROJECT),
            "--omit=tests/*",
            "--include=src/pytestshellutils/*",
        )
        # Generate report for tests code coverage
        session.run(
            "coverage",
            "xml",
            "-o",
            str(COVERAGE_REPORT_TESTS),
            "--omit=src/pytestshellutils/*",
            "--include=tests/*",
        )
        try:
            cmdline = [
                "coverage",
                "report",
                "--show-missing",
                "--include=src/pytestshellutils/*,tests/*",
            ]
            session.run(*cmdline)
            if pytest_version(session) >= (6, 2):
                cmdline.append("--fail-under={}".format(COVERAGE_FAIL_UNDER_PERCENT))
        finally:
            if COVERAGE_REPORT_DB.exists():
                shutil.copyfile(str(COVERAGE_REPORT_DB), str(ARTIFACTS_DIR / ".coverage"))


def _lint(session, rcfile, flags, paths):
    session.install("--progress-bar=off", "-e", ".[lint]", silent=PIP_INSTALL_SILENT)
    session.run("pylint", "--version")
    pylint_report_path = os.environ.get("PYLINT_REPORT")

    cmd_args = ["pylint", "--rcfile={}".format(rcfile)] + list(flags) + list(paths)

    stdout = tempfile.TemporaryFile(mode="w+b")
    try:
        session.run(*cmd_args, stdout=stdout)
    finally:
        stdout.seek(0)
        contents = stdout.read()
        if contents:
            contents = contents.decode("utf-8")
            sys.stdout.write(contents)
            sys.stdout.flush()
            if pylint_report_path:
                # Write report
                with open(pylint_report_path, "w", encoding="utf-8") as wfh:
                    wfh.write(contents)
                session.log("Report file written to %r", pylint_report_path)
        stdout.close()


@nox.session(python="3")
def lint(session):
    """
    Run PyLint against Salt and it's test suite. Set PYLINT_REPORT to a path to capture output.
    """
    session.notify("lint-code-{}".format(session.python))
    session.notify("lint-tests-{}".format(session.python))


@nox.session(python="3", name="lint-code")
def lint_code(session):
    """
    Run PyLint against the code. Set PYLINT_REPORT to a path to capture output.
    """
    flags = ["--disable=I", "--ignore-paths=src/pytestshellutils/downgraded/.*"]
    if session.posargs:
        paths = session.posargs
    else:
        paths = ["setup.py", "noxfile.py", "src/pytestshellutils/"]
    _lint(session, ".pylintrc", flags, paths)


@nox.session(python="3", name="lint-tests")
def lint_tests(session):
    """
    Run PyLint against Salt and it's test suite. Set PYLINT_REPORT to a path to capture output.
    """
    flags = ["--disable=I"]
    if session.posargs:
        paths = session.posargs
    else:
        paths = ["tests/"]
    _lint(session, ".pylintrc", flags, paths)


@nox.session(python="3")
def docs(session):
    """
    Build Docs.
    """
    session.install("--progress-bar=off", "-e", ".[docs]", silent=PIP_INSTALL_SILENT)
    os.chdir("docs/")
    session.run("make", "clean", external=True)
    # session.run("make", "linkcheck", "SPHINXOPTS=-W", external=True)
    session.run("make", "coverage", "SPHINXOPTS=-W", external=True)
    docs_coverage_file = os.path.join("_build", "html", "python.txt")
    if os.path.exists(docs_coverage_file):
        with open(docs_coverage_file, encoding="utf-8") as rfh:
            contents = rfh.readlines()[2:]
            if contents:
                session.error("\n" + "".join(contents))
    session.run("make", "html", "SPHINXOPTS=-W", external=True)
    os.chdir("..")


@nox.session(name="docs-dev", python="3")
def docs_dev(session):
    """
    Build Docs.
    """
    session.install("--progress-bar=off", "-e", ".[docs]", silent=PIP_INSTALL_SILENT)
    os.chdir("docs/")
    session.run("make", "html", "SPHINXOPTS=-W", external=True, env={"LOCAL_DEV_BUILD": "1"})
    os.chdir("..")


@nox.session(name="docs-crosslink-info", python="3")
def docs_crosslink_info(session):
    """
    Report intersphinx cross links information.
    """
    session.install("--progress-bar=off", "-e", ".[docs]", silent=PIP_INSTALL_SILENT)
    os.chdir("docs/")
    intersphinx_mapping = json.loads(
        session.run(
            "python",
            "-c",
            "import json; import conf; print(json.dumps(conf.intersphinx_mapping))",
            silent=True,
            log=False,
        )
    )
    try:
        mapping_entry = intersphinx_mapping[session.posargs[0]]
    except IndexError:
        session.error(
            "You need to pass at least one argument whose value must be one of: {}".format(
                ", ".join(list(intersphinx_mapping))
            )
        )
    except KeyError:
        session.error(
            "Only acceptable values for first argument are: {}".format(
                ", ".join(list(intersphinx_mapping))
            )
        )
    session.run(
        "python", "-m", "sphinx.ext.intersphinx", mapping_entry[0].rstrip("/") + "/objects.inv"
    )
    os.chdir("..")


@nox.session(name="gen-api-docs", python="3")
def gen_api_docs(session):
    """
    Generate API Docs.
    """
    session.install("--progress-bar=off", "-e", ".[docs]", silent=PIP_INSTALL_SILENT)
    shutil.rmtree("docs/ref", ignore_errors=True)
    session.run("sphinx-apidoc", "--module-first", "-o", "docs/ref/", "src/pytestshellutils/")


@nox.session(name="twine-check", python="3")
def twine_check(session):
    """
    Run ``twine-check`` against the source distribution package.
    """
    build(session)
    session.run("twine", "check", "dist/*")


@nox.session(name="changelog", python="3")
@nox.parametrize("draft", [False, True])
def changelog(session, draft):
    """
    Generate changelog.
    """
    session.install("--progress-bar=off", "-e", ".[changelog]", silent=PIP_INSTALL_SILENT)

    version = session.run(
        "python",
        "setup.py",
        "--version",
        silent=True,
        log=False,
        stderr=None,
    ).strip()

    town_cmd = ["towncrier", "build", "--version={}".format(version)]
    if draft:
        town_cmd.append("--draft")
    session.run(*town_cmd)


@nox.session(name="release")
def release(session):
    """
    Create a release tag.
    """
    if not session.posargs:
        session.error(
            "Forgot to pass the version to release? For example `nox -e release -- 1.1.0`"
        )
    if len(session.posargs) > 1:
        session.error(
            "Only one argument is supported by the `release` nox session. "
            "For example `nox -e release -- 1.1.0`"
        )
    version = session.posargs[0]
    try:
        session.log("Generating temporary %s tag", version)
        session.run("git", "tag", "-as", version, "-m", "Release {}".format(version), external=True)
        changelog(session, draft=False)
    except CommandFailed:
        session.error("Failed to generate the temporary tag")
    # session.notify("changelog(draft=False)")
    try:
        session.log("Generating the release changelog")
        session.run(
            "git",
            "commit",
            "-a",
            "-m",
            "Generate Changelog for version {}".format(version),
            external=True,
        )
    except CommandFailed:
        session.error("Failed to generate the release changelog")
    try:
        session.log("Overwriting temporary %s tag", version)
        session.run(
            "git", "tag", "-fas", version, "-m", "Release {}".format(version), external=True
        )
    except CommandFailed:
        session.error("Failed to overwrite the temporary tag")
    session.warn("Don't forget to push the newly created tag")


class Recompress:
    """
    Helper class to re-compress a ``.tag.gz`` file to make it reproducible.
    """

    def __init__(self, mtime):
        self.mtime = int(mtime)

    def tar_reset(self, tarinfo):
        """
        Reset user, group, mtime, and mode to create reproducible tar.
        """
        tarinfo.uid = tarinfo.gid = 0
        tarinfo.uname = tarinfo.gname = "root"
        tarinfo.mtime = self.mtime
        if tarinfo.type == tarfile.DIRTYPE:
            tarinfo.mode = 0o755
        else:
            tarinfo.mode = 0o644
        if tarinfo.pax_headers:
            raise ValueError(tarinfo.name, tarinfo.pax_headers)
        return tarinfo

    def recompress(self, targz):
        """
        Re-compress the passed path.
        """
        tempd = pathlib.Path(tempfile.mkdtemp()).resolve()
        d_src = tempd.joinpath("src")
        d_src.mkdir()
        d_tar = tempd.joinpath(targz.stem)
        d_targz = tempd.joinpath(targz.name)
        with tarfile.open(d_tar, "w|") as wfile:
            with tarfile.open(targz, "r:gz") as rfile:
                rfile.extractall(d_src)
                extracted_dir = next(pathlib.Path(d_src).iterdir())
                for name in sorted(extracted_dir.rglob("*")):
                    wfile.add(
                        str(name),
                        filter=self.tar_reset,
                        recursive=False,
                        arcname=str(name.relative_to(d_src)),
                    )

        with open(d_tar, "rb") as rfh:
            with gzip.GzipFile(
                fileobj=open(d_targz, "wb"), mode="wb", filename="", mtime=self.mtime
            ) as gz:
                while True:
                    chunk = rfh.read(1024)
                    if not chunk:
                        break
                    gz.write(chunk)
        targz.unlink()
        shutil.move(str(d_targz), str(targz))


@nox.session(python="3")
def build(session):
    """
    Build source and binary distributions based off the current commit author date UNIX timestamp.

    The reason being, reproducible packages.

    .. code-block: shell

        git show -s --format=%at HEAD
    """
    shutil.rmtree("dist/", ignore_errors=True)
    session.install("--progress-bar=off", "-r", "requirements/build.txt", silent=PIP_INSTALL_SILENT)

    timestamp = session.run(
        "git",
        "show",
        "-s",
        "--format=%at",
        "HEAD",
        silent=True,
        log=False,
        stderr=None,
    ).strip()
    env = {"SOURCE_DATE_EPOCH": str(timestamp)}
    session.run(
        "python",
        "-m",
        "build",
        "--sdist",
        "--wheel",
        str(REPO_ROOT),
        env=env,
    )
    # Recreate sdist to be reproducible
    recompress = Recompress(timestamp)
    for targz in REPO_ROOT.joinpath("dist").glob("*.tar.gz"):
        session.log("Re-compressing %s...", targz.relative_to(REPO_ROOT))
        recompress.recompress(targz)

    sha256sum = shutil.which("sha256sum")
    if sha256sum:
        packages = [str(pkg.relative_to(REPO_ROOT)) for pkg in REPO_ROOT.joinpath("dist").iterdir()]
        session.run("sha256sum", *packages, external=True)
    session.run("python", "-m", "twine", "check", "dist/*")
