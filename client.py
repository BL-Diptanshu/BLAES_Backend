import httpx
from config import settings
from token_manager import GitHubTokenManager

token_manager = GitHubTokenManager(settings.parsed_tokens())

class GitHubClient:

    async def get(self, endpoint: str):
        token = token_manager.get_token()

        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{settings.GITHUB_API_BASE}{endpoint}",
                headers=headers
            )

        if response.status_code == 401:
            token_manager.invalidate(token)
            raise Exception("Invalid GitHub token")

        token_manager.update(token, response.headers)
        return response