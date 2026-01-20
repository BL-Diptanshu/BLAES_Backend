from client import GitHubClient

client = GitHubClient()

async def fetch_commits(owner: str, repo: str, branch: str, max_commits: int = None):
    """
    Fetch complete commit history for a branch.
    Handles pagination and very long histories.
    """
    commits = []
    page = 1
    per_page = 100

    while True:
        endpoint = (
            f"/repos/{owner}/{repo}/commits"
            f"?sha={branch}&per_page={per_page}&page={page}"
        )

        resp = await client.get(endpoint)
        if resp.status_code != 200:
            raise Exception("Failed to fetch commits")

        data = resp.json()
        if not data:
            break

        for commit in data:
            commits.append(commit)
            if max_commits and len(commits) >= max_commits:
                return commits

        page += 1

    return commits