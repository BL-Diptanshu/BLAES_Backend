from datetime import datetime
from typing import List, Optional

def parse_github_date(date_str: str) -> datetime:
    return datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")


def filter_repositories(
    repos: List[dict],
    *,
    is_private: Optional[bool] = None,
    created_after: Optional[str] = None,
    created_before: Optional[str] = None,
    updated_after: Optional[str] = None,
    updated_before: Optional[str] = None,
    include_repos: Optional[List[str]] = None,
    exclude_repos: Optional[List[str]] = None,
) -> List[dict]:
    """
    Filter repositories based on multiple criteria.
    Dates must be in YYYY-MM-DD format.
    """

    filtered = repos

    # --- Public / Private filter ---
    if is_private is not None:
        filtered = [
            r for r in filtered if r["private"] == is_private
        ]

    # --- Date filters ---
    if created_after:
        ca = datetime.fromisoformat(created_after)
        filtered = [
            r for r in filtered
            if parse_github_date(r["created_at"]) >= ca
        ]

    if created_before:
        cb = datetime.fromisoformat(created_before)
        filtered = [
            r for r in filtered
            if parse_github_date(r["created_at"]) <= cb
        ]

    if updated_after:
        ua = datetime.fromisoformat(updated_after)
        filtered = [
            r for r in filtered
            if parse_github_date(r["updated_at"]) >= ua
        ]

    if updated_before:
        ub = datetime.fromisoformat(updated_before)
        filtered = [
            r for r in filtered
            if parse_github_date(r["updated_at"]) <= ub
        ]

    # --- Repo name filters ---
    if include_repos:
        include_set = set(include_repos)
        filtered = [
            r for r in filtered if r["name"] in include_set
        ]

    if exclude_repos:
        exclude_set = set(exclude_repos)
        filtered = [
            r for r in filtered if r["name"] not in exclude_set
        ]

    return filtered