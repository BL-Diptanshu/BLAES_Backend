import asyncio
from repo_fetcher import fetch_all_accessible_repos
from repo_filter import filter_repositories

def print_repos(repos: list, title: str):
    print(f"\n {title}")
    print("-" * 90)

    for idx, repo in enumerate(repos, start=1):
        owner = repo["owner"]["login"]
        print(
            f"{idx:02d}. "
            f"{owner}/{repo['name']} | "
            f"Private: {repo['private']} | "
            f"Updated: {repo['updated_at'][:10]}"
        )

    print("-" * 90)
    print(f"Total: {len(repos)} repositories\n")


async def main():
    repos = await fetch_all_accessible_repos()

    # CASE 1: No repositories at all
    if not repos:
        print("\n NO REPOSITORIES FOUND")
        print("-" * 60)
        print(
            "The GitHub token is valid, but it has no accessible repositories.\n"
            "Possible reasons:\n"
            " • No repos owned by the user\n"
            " • No org repos granted to this token\n"
            " • Missing 'read:org' permission\n"
        )
        return

    # Apply filters
    filtered_repos = filter_repositories(
        repos,
        is_private=True,
    )

    # CASE 2: Repos exist but filters removed all
    if not filtered_repos:
        print("\n NO REPOSITORIES MATCH THE FILTER CRITERIA")
        print("-" * 60)
        print(
            f"Total repositories accessible: {len(repos)}\n"
            "Try relaxing filters such as:\n"
            " • public/private flag\n"
            " • date ranges\n"
            " • include/exclude lists\n"
        )
        return

    # Normal case
    print_repos(filtered_repos, "Filtered Repositories")

if __name__ == "__main__":
    asyncio.run(main())