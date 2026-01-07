from client import GitHubClient

client = GitHubClient()

async def fetch_all_accessible_repos() -> list:
    repos = []
    page = 1
    per_page = 100

    while True:
        endpoint = f"/user/repos?per_page={per_page}&page={page}"
        response = await client.get(endpoint)

        if response.status_code != 200:
            raise Exception("Failed to fetch repositories")

        data = response.json()

        # Explicit empty response handling
        if not data:
            break

        repos.extend(data)
        page += 1

    return repos