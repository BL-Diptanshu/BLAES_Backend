from client import GitHubClient

client = GitHubClient()

async def validate_username(username: str) -> bool:
    resp = await client.get(f"/users/{username}")
    return resp.status_code == 200

async def validate_repo(owner: str, repo: str) -> dict:
    resp = await client.get(f"/repos/{owner}/{repo}")
    if resp.status_code != 200:
        raise Exception("Repo not accessible")
    return resp.json()