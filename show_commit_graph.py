import asyncio
from repo_fetcher import fetch_all_accessible_repos
from branch_fetcher import fetch_branches
from commit_graph import build_commit_graph

async def main():
    repos = await fetch_all_accessible_repos()

    print("\nSelect Repository")
    for i, repo in enumerate(repos, start=1):
        print(f"{i:02d}. {repo['owner']['login']}/{repo['name']}")

    repo = repos[int(input("Repo number: ")) - 1]
    owner = repo["owner"]["login"]
    repo_name = repo["name"]

    branch_data = await fetch_branches(owner, repo_name)
    branches = [b["name"] for b in branch_data["branches"]]

    graph = await build_commit_graph(owner, repo_name, branches)

    print("\nCommit Relationships")
    print("-" * 80)

    for sha, data in graph.items():
        merge_tag = "MERGE" if len(data["parents"]) > 1 else ""
        branch_info = ", ".join(sorted(data["branches"]))

        print(
            f"{sha[:7]} {merge_tag}\n"
            f"  Parents : {[p[:7] for p in data['parents']]}\n"
            f"  Children: {[c[:7] for c in data['children']]}\n"
            f"  Branches: {branch_info}\n"
        )

if __name__ == "__main__":
    asyncio.run(main())