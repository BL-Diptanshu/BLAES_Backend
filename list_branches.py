import asyncio
from repo_fetcher import fetch_all_accessible_repos
from branch_fetcher import fetch_branches

def print_repo_choices(repos):
    print("\nSelect Repository (Enter number)")
    print("-" * 70)
    for idx, repo in enumerate(repos, start=1):
        owner = repo["owner"]["login"]
        archived = "ARCHIVED" if repo["archived"] else ""
        print(f"{idx:02d}. {owner}/{repo['name']} {archived}")
    print("-" * 70)


def print_branch_info(data: dict):
    print(f"\nranches for {data['repo']}")
    print("-" * 80)

    if not data["branches"]:
        print("No branches found")
        return

    for br in data["branches"]:
        default_mark = "DEFAULT" if br["is_default"] else ""
        print(
            f"- {br['name']} {default_mark}\n"
            f"    Last Commit: {br['last_commit_sha'][:7]}\n"
            f"    Author     : {br['last_commit_author']}\n"
            f"    Updated    : {br['last_commit_date']}\n"
        )


async def main():
    repos = await fetch_all_accessible_repos()

    # Filter out archived repos (still show, but mark)
    if not repos:
        print("No repositories accessible")
        return

    print_repo_choices(repos)

    choice = input("Enter repo number: ").strip()

    if not choice.isdigit():
        print("Invalid input")
        return

    idx = int(choice) - 1
    if idx < 0 or idx >= len(repos):
        print("Invalid selection")
        return

    repo = repos[idx]

    if repo["archived"]:
        print("\nRepository is archived. Branches may be read-only.\n")

    owner = repo["owner"]["login"]
    repo_name = repo["name"]

    branch_data = await fetch_branches(owner, repo_name)
    print_branch_info(branch_data)

if __name__ == "__main__":
    asyncio.run(main())