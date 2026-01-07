from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    GITHUB_TOKENS: str
    GITHUB_API_BASE: str = "https://api.github.com"

    def parsed_tokens(self) -> List[str]:
        return [t.strip() for t in self.GITHUB_TOKENS.split(",") if t.strip()]

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()