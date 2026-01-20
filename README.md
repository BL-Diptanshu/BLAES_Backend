# BLAES – BridgeLabz Assignment Evaluation System (Phase 1)

BLAES is a backend system designed to automatically understand and analyze GitHub repositories before performing any assignment evaluation.
Phase 1 focuses on secure GitHub access, repository ingestion, branch and commit analysis, and safe file retrieval.

---

## Objective

The goal of Phase 1 is to ensure the system can reliably answer:
- What repositories exist and are accessible?
- What branches do they contain?
- What files are present in each branch?
- How did the code evolve over time?
- Who contributed what, and when?

---

## Current Capabilities

### Authentication & Authorization
- System-level GitHub token authentication
- Private repository access handling
- Centralized authorization logic

### Rate Limit & Error Handling
- GitHub API rate-limit awareness
- Clear exception handling for failures

### Repository Discovery
- Fetches all accessible repositories
- Supports public, private, and organization repositories

### Branch Analysis
- Fetches all branches
- Identifies default branch
- Handles archived repositories

### File Retrieval
- Clones/fetches repositories safely
- Extracts branch-wise files
- Skips binaries, large files, unsupported encodings, and submodules

### Commit History & Relationships
- Complete commit history per branch
- Commit metadata, diffs, and stats
- Parent–child commit relationships
- Merge and branch-point detection

---

## Design Philosophy

- Flat structure used intentionally for faster iteration and clarity
- Modular responsibilities for easy future restructuring
- Correctness prioritized before scale

---

## How to Run

List repositories:
    python list_repos.py

List branches:
    python list_branches.py

Retrieve files:
    python retrieve_files.py

View commit history:
    python list_commits.py

View commit relationships:
    python show_commit_graph.py

---

## Environment Setup

Create a .env file (ignored by git):

GITHUB_TOKENS=your_github_pat_here

---

## Status

Phase 1 ingestion layer complete and ready for evaluation logic.
