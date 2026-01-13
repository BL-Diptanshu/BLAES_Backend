import os
import shutil
from git_utils import clone_or_fetch, checkout_branch
from file_inspector import (
    is_binary_file,
    is_large_file,
    is_text_file,
    is_git_submodule
)

WORKSPACE_ROOT = "workspace"


def clean_dir(path: str):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path, exist_ok=True)


def retrieve_branch_files(
    owner: str,
    repo: str,
    repo_url: str,
    branches: list
):
    """
    Clones/fetches a repository and stores branch-wise safe text files.
    """

    base_repo_dir = os.path.join(WORKSPACE_ROOT, f"{owner}__{repo}")
    temp_git_dir = os.path.join(base_repo_dir, "_git")

    os.makedirs(WORKSPACE_ROOT, exist_ok=True)

    # Clone or fetch repo once
    clone_or_fetch(repo_url, temp_git_dir)

    for branch in branches:
        print(f"\nProcessing branch: {branch}")

        try:
            checkout_branch(temp_git_dir, branch)
        except Exception as e:
            print(f"Failed to checkout branch {branch}: {e}")
            continue

        branch_dir = os.path.join(base_repo_dir, branch)
        clean_dir(branch_dir)

        files_copied = 0

        for root, dirs, files in os.walk(temp_git_dir):
            # Never copy git internals
            if ".git" in dirs:
                dirs.remove(".git")

            # Skip nested repositories / submodules
            if is_git_submodule(root) and root != temp_git_dir:
                dirs.clear()
                continue

            rel_root = os.path.relpath(root, temp_git_dir)
            target_root = os.path.join(branch_dir, rel_root)

            os.makedirs(target_root, exist_ok=True)

            for file in files:
                src = os.path.join(root, file)
                dst = os.path.join(target_root, file)

                if is_large_file(src):
                    continue

                if is_binary_file(src):
                    continue

                if not is_text_file(src):
                    continue

                try:
                    shutil.copy2(src, dst)
                    files_copied += 1
                except Exception:
                    continue

        if files_copied == 0:
            print("No valid text files found in this branch")

    print(f"\nRepository processed → {base_repo_dir}")