from git import Repo, GitCommandError
import sys
from .print import error, warning

def get_commits(repo: Repo, branches, since=None, until=None, authors=None):
    results = []

    if len(branches) > 1:
        warning("Analyzing multiple branches may produce inconsistent results, because commits can occur on multiple branches.") 

    for branch in branches:
        try:
            commits = list(repo.iter_commits(branch, since=since, until=until))
            results.append({"branch": branch, "commits": commits})
        except GitCommandError:
            error(f"The branch {branch} is not a existing branch in this repository.")
            sys.exit(1)

    if authors:
        authors = authors.split(",")
        for entry in results:
            entry["commits"] = [
                c for c in entry["commits"]
                if c.author.name in authors
            ]

    return results