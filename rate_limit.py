from exceptions import GitHubRateLimitError
from config import settings
import time

def check_rate_limit(headers):
    remaining = int(headers.get("X-RateLimit-Remaining", 0))
    reset_time = int(headers.get("X-RateLimit-Reset", 0))

    if remaining == 0:
        sleep_for = reset_time - int(time.time())
        raise GitHubRateLimitError(
            f"Rate limit exhausted. Retry after {sleep_for}s"
        )

    if remaining < settings.RATE_LIMIT_THRESHOLD:
        print(f"[WARN] GitHub rate limit low: {remaining}")