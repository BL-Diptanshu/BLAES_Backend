import os
import shutil
from git_utils import clone_or_fetch, checkout_branch

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
    base_repo_dir = os.path.join(WORKSPACE_ROOT, f"{owner}__{repo}")
    temp_git_dir = os.path.join(base_repo_dir, "_git")

    os.makedirs(WORKSPACE_ROOT, exist_ok=True)

    # Clone or fetch once
    clone_or_fetch(repo_url, temp_git_dir)

    for branch in branches:
        print(f"Processing branch: {branch}")

        checkout_branch(temp_git_dir, branch)

        branch_dir = os.path.join(base_repo_dir, branch)
        clean_dir(branch_dir)

        for item in os.listdir(temp_git_dir):
            if item == ".git":
                continue

            src = os.path.join(temp_git_dir, item)
            dst = os.path.join(branch_dir, item)

            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)

    print(f"Files stored at → {base_repo_dir}")