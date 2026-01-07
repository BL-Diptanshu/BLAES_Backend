import asyncio
from repo_fetcher import fetch_all_accessible_repos
from branch_fetcher import fetch_branches
from file_retriever import retrieve_branch_files

async def main():
    repos = await fetch_all_accessible_repos()

    if not repos:
        print("No repositories accessible")
        return

    print("\nSelect Repository")
    print("-" * 60)
    for i, repo in enumerate(repos, start=1):
        print(f"{i:02d}. {repo['owner']['login']}/{repo['name']}")
    print("-" * 60)

    choice = input("Enter repo number: ").strip()
    if not choice.isdigit():
        print("Invalid input")
        return

    repo = repos[int(choice) - 1]
    owner = repo["owner"]["login"]
    repo_name = repo["name"]
    repo_url = repo["clone_url"]

    if repo["archived"]:
        print("Repository is archived (read-only)")

    branch_data = await fetch_branches(owner, repo_name)
    branches = [b["name"] for b in branch_data["branches"]]

    if not branches:
        print("No branches found")
        return

    retrieve_branch_files(
        owner=owner,
        repo=repo_name,
        repo_url=repo_url,
        branches=branches
    )

if __name__ == "__main__":
    asyncio.run(main())