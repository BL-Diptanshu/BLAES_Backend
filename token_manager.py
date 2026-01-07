import time
from typing import Dict, List

class GitHubTokenManager:
    def __init__(self, tokens: List[str]):
        if not tokens:
            raise ValueError("No GitHub tokens provided")

        self.tokens = tokens
        self.token_meta: Dict[str, Dict] = {
            token: {
                "remaining": 5000,
                "reset": 0,
                "valid": True
            } for token in tokens
        }

    def get_token(self) -> str:
        now = int(time.time())

        for token, meta in self.token_meta.items():
            if not meta["valid"]:
                continue
            if meta["remaining"] > 0 or meta["reset"] <= now:
                return token

        raise Exception("All GitHub tokens exhausted")

    def update(self, token: str, headers: dict):
        self.token_meta[token]["remaining"] = int(
            headers.get("X-RateLimit-Remaining", 0)
        )
        self.token_meta[token]["reset"] = int(
            headers.get("X-RateLimit-Reset", 0)
        )

    def invalidate(self, token: str):
        self.token_meta[token]["valid"] = False