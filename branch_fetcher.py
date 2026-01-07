from client import GitHubClient

client = GitHubClient()

async def fetch_branches(owner: str, repo: str) -> dict:
    """
    Fetch all branches for a repository along with metadata.
    """
    endpoint = f"/repos/{owner}/{repo}/branches"
    response = await client.get(endpoint)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch branches for {owner}/{repo}")

    branches = response.json()

    # Fetch repo info to get default branch
    repo_resp = await client.get(f"/repos/{owner}/{repo}")
    repo_data = repo_resp.json()
    default_branch = repo_data.get("default_branch")

    enriched_branches = []

    for br in branches:
        commit_url = br["commit"]["url"]
        commit_resp = await client.get(commit_url.replace("https://api.github.com", ""))

        commit_data = commit_resp.json()
        commit_info = commit_data["commit"]

        enriched_branches.append({
            "name": br["name"],
            "is_default": br["name"] == default_branch,
            "last_commit_sha": br["commit"]["sha"],
            "last_commit_date": commit_info["committer"]["date"],
            "last_commit_author": commit_info["committer"]["name"],
        })

    return {
        "repo": f"{owner}/{repo}",
        "default_branch": default_branch,
        "branches": enriched_branches,
    }