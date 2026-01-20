from collections import defaultdict
from commit_fetcher import fetch_commits
from commit_parser import enrich_commit

async def build_commit_graph(owner: str, repo: str, branches: list):
    """
    Builds commit relationship graph across branches.
    """
    graph = {}
    commit_to_branches = defaultdict(set)

    for branch in branches:
        commits = await fetch_commits(owner, repo, branch)

        for c in commits:
            sha = c["sha"]
            commit_to_branches[sha].add(branch)

            if sha not in graph:
                details = await enrich_commit(owner, repo, sha)
                graph[sha] = {
                    "sha": sha,
                    "parents": details["parents"],
                    "children": set(),
                    "branches": set()
                }

    # Build parent → child relationships
    for sha, data in graph.items():
        for parent in data["parents"]:
            if parent in graph:
                graph[parent]["children"].add(sha)

    # Attach branches
    for sha, branches in commit_to_branches.items():
        graph[sha]["branches"].update(branches)

    return graph