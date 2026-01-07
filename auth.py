from client import GitHubClient
from exceptions import GitHubRepoAccessError

client = GitHubClient()

async def check_repo_permissions(owner: str, repo: str):
    resp = await client.get(f"/repos/{owner}/{repo}")

    permissions = resp.json().get("permissions", {})

    if not permissions.get("pull"):
        raise GitHubRepoAccessError(
            "No read permission on repository"
        )

    return True