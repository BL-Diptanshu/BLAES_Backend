import asyncio
from repo_fetcher import fetch_all_accessible_repos
from branch_fetcher import fetch_branches
from commit_fetcher import fetch_commits
from commit_parser import enrich_commit

async def main():
    repos = await fetch_all_accessible_repos()

    print("\nSelect Repository")
    for i, repo in enumerate(repos, start=1):
        print(f"{i:02d}. {repo['owner']['login']}/{repo['name']}")

    repo_idx = int(input("Repo number: ")) - 1
    repo = repos[repo_idx]

    owner = repo["owner"]["login"]
    repo_name = repo["name"]

    branch_data = await fetch_branches(owner, repo_name)
    branches = [b["name"] for b in branch_data["branches"]]

    print("\nSelect Branch")
    for i, br in enumerate(branches, start=1):
        print(f"{i:02d}. {br}")

    branch = branches[int(input("Branch number: ")) - 1]

    commits = await fetch_commits(owner, repo_name, branch, max_commits=20)

    print(f"\nCommits for {branch}\n" + "-" * 70)

    for c in commits:
        detailed = await enrich_commit(owner, repo_name, c["sha"])

        merge_tag = "MERGE" if detailed["is_merge_commit"] else ""
        print(
            f"{detailed['sha'][:7]} {merge_tag}\n"
            f"  Author : {detailed['author_name']} ({detailed['author_email']})\n"
            f"  Date   : {detailed['timestamp']}\n"
            f"  Msg    : {detailed['message'].splitlines()[0]}\n"
            f"  Files  : {len(detailed['files'])}, "
            f"+{detailed['stats'].get('additions', 0)} "
            f"-{detailed['stats'].get('deletions', 0)}\n"
        )

if __name__ == "__main__":
    asyncio.run(main())