#!/usr/bin/env python

import configparser
import contextlib
import csv
import glob
import gzip
import hashlib
import io
import json
import math
import os
import re
import shutil
import ssl
import struct
import sys
import tarfile
import time
import urllib.request
from functools import partial
from xml.etree import ElementTree as etree

import setuptools
from distutils import log
from distutils.command.build import build as _build
from distutils.command.clean import clean as _clean
from setuptools.command.sdist import sdist as _sdist

try:
    from tqdm import tqdm
except ImportError as err:
    tqdm = err

try:
    from pyhmmer.plan7 import HMMFile
except ImportError as err:
    HMMFile = err


class sdist(_sdist):
    """An extension to the `sdist` command that generates a `pyproject.toml`.
    """

    def run(self):
        # build `pyproject.toml` from `setup.cfg`
        c = configparser.ConfigParser()
        c.add_section("build-system")
        c.set("build-system", "requires", str(self.distribution.setup_requires))
        c.set("build-system", "build-backend", '"setuptools.build_meta"')
        with open("pyproject.toml", "w") as pyproject:
            c.write(pyproject)

        # run the rest of the packaging
        _sdist.run(self)


class list_requirements(setuptools.Command):
    """A custom command to write the project requirements.
    """

    description = "list the project requirements"
    user_options = [
        ("setup", "s", "show the setup requirements as well."),
        (
            "requirements=",
            "r",
            "the name of the requirements file (defaults to requirements.txt)"
        )
    ]

    def initialize_options(self):
        self.setup = False
        self.output = None

    def finalize_options(self):
        if self.output is None:
            self.output = "requirements.txt"

    def run(self):
        cfg = configparser.ConfigParser()
        cfg.read(__file__.replace(".py", ".cfg"))

        with open(self.output, "w") as f:
            if self.setup:
                f.write(cfg.get("options", "setup_requires"))
            f.write(cfg.get("options", "install_requires"))
            for _, v in cfg.items("options.extras_require"):
                f.write(v)


class update_interpro(setuptools.Command):
    """A custom command to update the internal InterPro metadata.
    """

    description = "update the InterPro metadata embedded in the source"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def info(self, msg):
        self.announce(msg, level=2)

    def run(self):
        # Update the interpro entries
        entries = []
        path = os.path.join("gecco", "interpro", "interpro.json")
        self.info("getting Pfam entries from InterPro")
        entries.extend(self.download_interpro_entries("pfam"))
        self.info("getting Tigrfam entries from InterPro")
        entries.extend(self.download_interpro_entries("tigrfams"))
        # sort by id
        entries.sort(key=lambda entry: entry["accession"])
        with open(path, "wt") as dest:
            json.dump(entries, dest, sort_keys=True, indent=4)

    def download_interpro_entries(self, db):
        next = f"https://www.ebi.ac.uk:443/interpro/api/entry/all/{db}/?page_size=200"
        entries = []
        context = ssl._create_unverified_context()
        with tqdm(desc=db, leave=False) as pbar:
            while next:
                time.sleep(1) # wait between query to avoid being throttled by the server
                with urllib.request.urlopen(next, context=context) as res:
                    payload = json.load(res)
                    pbar.total = payload["count"]
                    next = payload["next"]
                    entries.extend(entry["metadata"] for entry in payload["results"])
                    pbar.update(len(payload["results"]))
        return entries


class update_model(setuptools.Command):
    """A custom command to update the internal CRF model.
    """

    description = "update the CRF model embedded in the source"
    user_options = [
        ("model=", "m", "the path to the new CRF model to use"),
    ]

    def initialize_options(self):
        self.model = None

    def finalize_options(self):
        if self.model is None:
            raise ValueError("--model argument must be given")
        elif not os.path.isdir(self.model):
            raise FileNotFoundError(self.model)

    def info(self, msg):
        self.announce(msg, level=2)

    def run(self):
        # Check `tqdm` is installed
        if isinstance(tqdm, ImportError):
            raise RuntimeError("tqdm is required to run the `update_model` command") from tqdm

        # Copy the file to the new in-source location and compute its hash.
        hasher = hashlib.md5()
        self.info("Copying the trained CRF model to the in-source location")
        with open(os.path.join(self.model, "model.pkl"), "rb") as src:
            with open(os.path.join("gecco", "crf", "model.pkl"), "wb") as dst:
                read = lambda: src.read(io.DEFAULT_BUFFER_SIZE)
                for chunk in iter(read, b""):
                    hasher.update(chunk)
                    dst.write(chunk)

        # Write the hash to the signature file next to the model
        self.info("Writing the MD5 signature file")
        with open(os.path.join("gecco", "crf", "model.pkl.md5"), "w") as sig:
            sig.write(hasher.hexdigest())

        # Update the domain composition table
        self.info("Copying the RF training data to the in-source location")
        for filename in ["compositions.npz", "domains.tsv", "types.tsv"]:
            src = os.path.join(self.model, filename)
            dst = os.path.join("gecco", "types", filename)
            shutil.copy(src=src, dst=dst)

        # Rebuild the InterPro metadata
        update_interpro = self.get_finalized_command("update_interpro")
        update_interpro.run()

        # Rebuild the HMMs using the new domains from the model
        build_data = self.get_finalized_command("build_data")
        build_data.force = build_data.rebuild = True
        build_data.run()


class build_data(setuptools.Command):
    """A custom `setuptools` command to download data before wheel creation.
    """

    description = "download the HMM libraries used by GECCO to annotate proteins"
    user_options = [
        ("force", "f", "force downloading the files even if they exist"),
        ("inplace", "i", "ignore build-lib and put data alongside your Python code"),
        ("rebuild", "r", "rebuild the HMM from the source instead of getting "
                         "the pre-filtered HMM files from GitHub"),
    ]

    def initialize_options(self):
        self.force = False
        self.inplace = False
        self.rebuild = False

    def finalize_options(self):
        _build_py = self.get_finalized_command("build_py")
        self.build_lib = _build_py.build_lib

    def info(self, msg):
        self.announce(msg, level=2)

    def run(self):
        # make sure the build/lib/ folder exists
        self.mkpath(self.build_lib)

        # Check `tqdm` and `pyhmmer` are installed
        if isinstance(HMMFile, ImportError):
            raise RuntimeError("pyhmmer is required to run the `build_data` command") from HMMFile
        if isinstance(tqdm, ImportError):
            raise RuntimeError("tqdm is required to run the `build_data` command") from tqdm

        # Load domain whitelist from the type classifier data
        domains_file = os.path.join("gecco", "types", "domains.tsv")
        self.info(f"loading domain accesssions from {domains_file}")
        with open(domains_file, "rb") as f:
            domains = [line.strip() for line in f]

        # Download and binarize required HMMs
        for in_ in glob.iglob(os.path.join("gecco", "hmmer", "*.ini")):
            local = os.path.join(self.build_lib, in_).replace(".ini", ".h3m")
            self.mkpath(os.path.dirname(local))
            self.download(in_, local, domains)
            if self.inplace:
                copy = in_.replace(".ini", ".h3m")
                self.make_file([local], copy, shutil.copy, (local, copy))

    def download(self, in_, local, domains):
        # read the configuration file for each HMM database
        cfg = configparser.ConfigParser()
        cfg.read(in_)
        options = dict(cfg.items("hmm"))

        # download the HMM to `local`, and delete the file if any error
        # or interruption happens during the download
        try:
            self.make_file([in_], local, self.download_hmm, (local, domains, options))
        except BaseException:
            if os.path.exists(local):
                os.remove(local)
            raise

        # update the MD5 if the HMMs are being rebuilt, otherwise
        # check the hashes are consistent
        if self.rebuild:
            self._rebuild_checksum(in_, local, cfg)
            self._rebuild_size(in_, local, cfg)
        else:
            self._validate_checksum(local, options)

    def download_hmm(self, output, domains, options):
        # try getting the GitHub artifacts first, unless asked to rebuild
        if not self.rebuild:
            try:
                self._download_release_hmm(output, domains, options)
            except urllib.error.HTTPError:
                pass
            else:
                return
        # fallback to filtering the HMMs from their release location
        self._rebuild_hmm(output, domains, options)

    def _download_release_hmm(self, output, domains, options):
        # build the GitHub releases URL
        base = "https://github.com/zellerlab/GECCO/releases/download/v{version}/{id}.h3m.gz"
        url = base.format(id=options["id"], version=self.distribution.get_version())
        # fetch the resource
        self.info(f"fetching {url}")
        response = urllib.request.urlopen(url)
        # use `tqdm` to make a progress bar
        pbar = tqdm.wrapattr(
            response,
            "read",
            total=int(response.headers["Content-Length"]),
            desc=os.path.basename(output),
            leave=False,
        )
        # download to `output`
        with contextlib.ExitStack() as ctx:
            dl = ctx.enter_context(pbar)
            src = ctx.enter_context(gzip.open(dl))
            dst = ctx.enter_context(open(output, "wb"))
            shutil.copyfileobj(src, dst)

    def _rebuild_hmm(self, output, domains, options):
        # fetch the resource from the URL in the ".ini" files
        self.info(f"using fallback {options['url']}")
        response = urllib.request.urlopen(options["url"])
        # use `tqdm` to make a progress bar
        pbar = tqdm.wrapattr(
            response,
            "read",
            total=int(response.headers["Content-Length"]),
            desc=os.path.basename(output),
            leave=False,
        )
        # download to `output`
        nsource = nwritten = 0
        with contextlib.ExitStack() as ctx:
            dl = ctx.enter_context(pbar)
            src = ctx.enter_context(gzip.open(dl))
            dst = ctx.enter_context(open(output, "wb"))
            for hmm in HMMFile(src):
                nsource += 1
                if hmm.accession.split(b".")[0] in domains:
                    nwritten += 1
                    hmm.write(dst, binary=True)
        # log number of HMMs kept in final files
        self.info(f"kept {nwritten} HMMs out of {nsource} in the source file")

    def _checksum(self, path):
        hasher = hashlib.md5()
        with HMMFile(path) as hmm_file:
            for hmm in hmm_file:
                hasher.update(struct.pack("<I", hmm.checksum))
        return hasher.hexdigest()

    def _size(self, path):
        with HMMFile(path) as hmm_file:
            size = sum(1 for _ in hmm_file)
        return size

    def _validate_checksum(self, local, options):
        self.info(f"checking HMM/MD5 signature of {local}")
        md5 = self._checksum(local)
        if md5 != options["md5"]:
            self.info("local HMM/MD5 does not match the expected HMM/MD5 hash")
            self.info(f"(expected {options['md5']}, found {md5}")
            self.info("rerun `python setup.py build_data --force`")
            raise ValueError("HMM/MD5 hash mismatch")

    def _rebuild_checksum(self, in_, local, cfg):
        self.info(f"updating HMM/MD5 signature in {in_}")
        cfg.set("hmm", "md5", self._checksum(local))
        with open(in_, "w") as f:
            cfg.write(f)

    def _rebuild_size(self, in_, local, cfg):
        self.info(f"updating HMM size in {in_}")
        cfg.set("hmm", "size", str(self._size(local)))
        with open(in_, "w") as f:
            cfg.write(f)


class build(_build):
    """A hacked `build` command that will also run `build_data`.
    """

    def run(self):
        # build data if needed
        if not self.distribution.have_run.get("build_data", False):
            _build_data = self.get_finalized_command("build_data")
            _build_data.force = self.force
            _build_data.run()
        # build rest as normal
        _build.run(self)


class clean(_clean):

    def run(self):
        # remove HMM files that have been installed inplace
        hmm_dir = os.path.join(os.path.dirname(__file__), "gecco", "hmmer")
        for ini in glob.iglob(os.path.join(hmm_dir, "*.ini")):
            for ext in [".h3m", ".hmm"]:
                path = ini.replace(".ini", ext)
                if os.path.exists(path):
                    log.info("Removing %s", path)
                    if not self.dry_run:
                        os.remove(path)
        # run the rest of the command as normal
        _clean.run(self)


if __name__ == "__main__":
    setuptools.setup(
        cmdclass={
            "build": build,
            "build_data": build_data,
            "clean": clean,
            "list_requirements": list_requirements,
            "sdist": sdist,
            "update_model": update_model,
            "update_interpro": update_interpro,
        },
    )
