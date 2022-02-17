import os
import shutil

from git.repo.base import Repo
from test_nautilus_librarian.test_typer.test_commands.test_workflows.test_gold_images_processing import (
    create_initial_state,
)
from test_nautilus_librarian.utils import compact_json

from nautilus_librarian.mods.console.domain.utils import execute_shell_command
from nautilus_librarian.mods.git.domain.git_command_wrapper import git
from nautilus_librarian.mods.namecodes.domain.filename import Filename
from nautilus_librarian.typer.commands.workflows.actions.action_result import ResultCode
from nautilus_librarian.typer.commands.workflows.actions.auto_commit_base_images import (
    auto_commit_base_images,
    calculate_the_corresponding_base_image_from_gold_image,
    get_new_gold_images_filenames_from_dvc_diff,
)


def test_get_new_gold_images_from_dvc_diff():

    dvc_diff = {
        "added": [
            {"path": "data/000001/32/000001-32.600.2.tif"},
            {"path": "data/000001/42/000001-42.600.2.tif"},
        ],
        "deleted": [],
        "modified": [],
        "renamed": [],
    }

    result = get_new_gold_images_filenames_from_dvc_diff(compact_json(dvc_diff))

    assert result == [Filename("data/000001/32/000001-32.600.2.tif")]


def test_calculate_the_corresponding_base_image_from_gold_image():
    git_repo_dir = "/home/repo"
    gold_image = Filename("000001-32.600.2.tif")

    base_image_path = calculate_the_corresponding_base_image_from_gold_image(
        git_repo_dir, gold_image
    )

    assert base_image_path == (
        "data/000001/42/000001-42.600.2.tif",  # relative path
        "/home/repo/data/000001/42/000001-42.600.2.tif",  # absolute path
    )


def remove_base_image_dvc_files(temp_git_dir):
    os.remove(f"{temp_git_dir}/data/000001/42/000001-42.600.2.tif.dvc")
    os.remove(f"{temp_git_dir}/data/000001/42/.gitignore")


def overwrite_base_image(fixtures_dir, temp_git_dir):
    shutil.copyfile(
        f"{fixtures_dir}/images/000001-42.600.2-modified.tif",
        f"{temp_git_dir}/data/000001/42/000001-42.600.2.tif",
    )


def rename_base_image(temp_git_dir):
    execute_shell_command(
        """
        mkdir -p data/000002/42
        dvc move data/000001/42/000001-42.600.2.tif data/000002/42/000002-42.600.2.tif
    """,
        cwd=temp_git_dir,
        print_output=True,
    )


def add_base_image_to_dvc(temp_git_dir):
    execute_shell_command(
        """
        dvc add data/000001/42/000001-42.600.2.tif
    """,
        cwd=temp_git_dir,
        print_output=True,
    )


def commit_added_base_images(temp_git_dir, temp_gpg_home_dir, git_user):

    dvc_diff = {
        "added": [
            {"path": "data/000001/32/000001-32.600.2.tif"},
        ],
        "deleted": [],
        "modified": [],
        "renamed": [],
    }

    return auto_commit_base_images(
        compact_json(dvc_diff), str(temp_git_dir), str(temp_gpg_home_dir), git_user
    )


def assert_commit_content(commit, expected_commit_stats_files, git_user):
    assert commit.stats.files == expected_commit_stats_files

    # Assert the commit was created by the right user
    assert commit.committer.name == git_user.name
    assert commit.committer.email == git_user.email


def assert_commit_summary(commit, expected_commit_summary):
    assert commit.summary == expected_commit_summary


def assert_commit_signingkey(commit, temp_git_dir, git_user):
    # Assert the commit was signed with the right signing key
    assert (
        git(temp_git_dir).get_commit_signing_key(commit.hexsha) == git_user.signingkey
    )


def given_a_dvc_diff_object_with_a_new_gold_image_it_should_commit_the_added_base_image_to_dvc(
    temp_git_dir,
    temp_dvc_local_remote_storage_dir,
    sample_base_image_absolute_path,
    temp_gpg_home_dir,
    git_user,
):
    create_initial_state(
        temp_git_dir,
        temp_dvc_local_remote_storage_dir,
        sample_base_image_absolute_path,
        temp_gpg_home_dir,
        git_user,
    )

    add_base_image_to_dvc(temp_git_dir)

    result = commit_added_base_images(temp_git_dir, temp_gpg_home_dir, git_user)

    # Assert command runned successfully
    assert result.code == ResultCode.CONTINUE

    # Git commit Asserts

    # Assert Base commit was created
    repo = Repo(temp_git_dir)
    commit = repo.commit(repo.heads[0].commit)  # latest commit on the branch

    assert_commit_summary(commit, "feat: new base image: 000001-42.600.2.tif")

    # Assert the commit contains the right files
    expected_commit_stats_files = {
        "data/000001/42/.gitignore": {"insertions": 1, "deletions": 0, "lines": 1},
        "data/000001/42/000001-42.600.2.tif.dvc": {
            "insertions": 4,
            "deletions": 0,
            "lines": 4,
        },
    }

    assert_commit_content(commit, expected_commit_stats_files, git_user)
    assert_commit_signingkey(commit, temp_git_dir, git_user)


def given_a_dvc_diff_object_with_a_gold_image_deleton_it_should_commit_the_base_image_deletion_to_git(
    temp_git_dir,
    temp_dvc_local_remote_storage_dir,
    sample_base_image_absolute_path,
    temp_gpg_home_dir,
    git_user,
):
    create_initial_state(
        temp_git_dir,
        temp_dvc_local_remote_storage_dir,
        sample_base_image_absolute_path,
        temp_gpg_home_dir,
        git_user,
    )

    add_base_image_to_dvc(temp_git_dir)
    commit_added_base_images(temp_git_dir, temp_gpg_home_dir, git_user)
    remove_base_image_dvc_files(temp_git_dir)

    dvc_diff = {
        "added": [],
        "deleted": [
            {"path": "data/000001/32/000001-32.600.2.tif"},
        ],
        "modified": [],
        "renamed": [],
    }

    result = auto_commit_base_images(
        compact_json(dvc_diff), str(temp_git_dir), str(temp_gpg_home_dir), git_user
    )

    # Assert command runned successfully
    assert result.code == ResultCode.CONTINUE

    # Git commit Asserts

    repo = Repo(temp_git_dir)
    commit = repo.commit(repo.heads[0].commit)  # latest commit on the branch

    assert_commit_summary(commit, "feat: deleted base image: 000001-42.600.2.tif")

    expected_commit_stats_files = {
        "data/000001/42/.gitignore": {"insertions": 0, "deletions": 1, "lines": 1},
        "data/000001/42/000001-42.600.2.tif.dvc": {
            "insertions": 0,
            "deletions": 4,
            "lines": 4,
        },
    }
    assert_commit_content(commit, expected_commit_stats_files, git_user)
    assert_commit_signingkey(commit, temp_git_dir, git_user)


def given_a_dvc_diff_object_with_a_gold_image_rename_it_should_commit_the_base_image_rename_to_git(
    temp_git_dir,
    temp_dvc_local_remote_storage_dir,
    sample_base_image_absolute_path,
    temp_gpg_home_dir,
    git_user,
):

    create_initial_state(
        temp_git_dir,
        temp_dvc_local_remote_storage_dir,
        sample_base_image_absolute_path,
        temp_gpg_home_dir,
        git_user,
    )
    add_base_image_to_dvc(temp_git_dir)
    commit_added_base_images(temp_git_dir, temp_gpg_home_dir, git_user)
    rename_base_image(temp_git_dir)

    repo = Repo(temp_git_dir)

    dvc_diff = {
        "added": [],
        "deleted": [],
        "modified": [],
        "renamed": [
            {
                "path": {
                    "old": "data/000001/32/000001-32.600.2.tif",
                    "new": "data/000002/32/000002-32.600.2.tif",
                }
            }
        ],
    }
    result = auto_commit_base_images(
        compact_json(dvc_diff), str(temp_git_dir), str(temp_gpg_home_dir), git_user
    )
    assert result.code == ResultCode.CONTINUE

    commit = repo.commit(repo.heads[0].commit)

    expected_commit_stats_files = {
        "data/000001/42/.gitignore": {"insertions": 0, "deletions": 1, "lines": 1},
        "data/000002/42/.gitignore": {"insertions": 3, "deletions": 0, "lines": 3},
        "data/{000001/42/000001-42.600.2.tif.dvc => 000002/42/000002-42.600.2.tif.dvc}": {
            "insertions": 1,
            "deletions": 1,
            "lines": 2,
        },
    }
    assert_commit_summary(
        commit, "feat: renamed base image: 000001-42.600.2.tif -> 000002-42.600.2.tif"
    )
    assert_commit_content(commit, expected_commit_stats_files, git_user)
    assert_commit_signingkey(commit, temp_git_dir, git_user)


def given_a_dvc_diff_object_with_a_gold_image_modification_it_should_commit_the_base_image_rename_to_git(
    temp_git_dir,
    temp_dvc_local_remote_storage_dir,
    sample_base_image_absolute_path,
    temp_gpg_home_dir,
    git_user,
    workflows_fixtures_dir,
):

    create_initial_state(
        temp_git_dir,
        temp_dvc_local_remote_storage_dir,
        sample_base_image_absolute_path,
        temp_gpg_home_dir,
        git_user,
    )
    add_base_image_to_dvc(temp_git_dir)
    commit_added_base_images(temp_git_dir, temp_gpg_home_dir, git_user)
    overwrite_base_image(workflows_fixtures_dir, temp_git_dir)
    add_base_image_to_dvc(temp_git_dir)

    repo = Repo(temp_git_dir)

    dvc_diff = {
        "added": [],
        "deleted": [],
        "modified": [{"path": "data/000001/32/000001-32.600.2.tif"}],
        "renamed": [],
    }

    result = auto_commit_base_images(
        compact_json(dvc_diff), str(temp_git_dir), str(temp_gpg_home_dir), git_user
    )
    assert result.code == ResultCode.CONTINUE

    commit = repo.commit(repo.heads[0].commit)

    assert_commit_summary(commit, "feat: modified base image: 000001-42.600.2.tif")

    expected_commit_stats_files = {
        "data/000001/42/000001-42.600.2.tif.dvc": {
            "insertions": 2,
            "deletions": 2,
            "lines": 4,
        }
    }
    assert_commit_content(commit, expected_commit_stats_files, git_user)
    assert_commit_signingkey(commit, temp_git_dir, git_user)
