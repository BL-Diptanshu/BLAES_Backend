from client import GitHubClient

client = GitHubClient()

async def enrich_commit(owner: str, repo: str, sha: str) -> dict:
    """
    Fetch full commit details including diffs and stats.
    """
    resp = await client.get(f"/repos/{owner}/{repo}/commits/{sha}")
    data = resp.json()

    commit = data["commit"]

    return {
        "sha": sha,
        "message": commit["message"],
        "author_name": commit["author"]["name"] if commit.get("author") else None,
        "author_email": commit["author"]["email"] if commit.get("author") else None,
        "timestamp": commit["author"]["date"] if commit.get("author") else None,
        "parents": [p["sha"] for p in data.get("parents", [])],
        "is_merge_commit": len(data.get("parents", [])) > 1,
        "stats": data.get("stats", {}),
        "files": [
            {
                "filename": f["filename"],
                "status": f["status"],
                "additions": f["additions"],
                "deletions": f["deletions"],
                "changes": f["changes"],
            }
            for f in data.get("files", [])
        ],
    }