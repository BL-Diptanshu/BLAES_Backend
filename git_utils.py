import subprocess
import os

def run_git(cmd, cwd=None):
    result = subprocess.run(
        cmd,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    if result.returncode != 0:
        raise Exception(result.stderr.strip())
    return result.stdout.strip()


def clone_or_fetch(repo_url: str, local_repo_path: str):
    if not os.path.exists(local_repo_path):
        print(f"Cloning repository → {local_repo_path}")
        run_git(["git", "clone", repo_url, local_repo_path])
    else:
        print(f"Fetching updates → {local_repo_path}")
        run_git(["git", "fetch", "--all"], cwd=local_repo_path)


def checkout_branch(local_repo_path: str, branch: str):
    run_git(["git", "checkout", branch], cwd=local_repo_path)
    run_git(["git", "pull"], cwd=local_repo_path)