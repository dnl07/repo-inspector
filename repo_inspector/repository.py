from git import Repo, GitCommandError
import sys
from .print import error, warning

def get_commits(repo: Repo, branches, since=None, until=None, authors=None):
    all_commits = []    

    if len(branches) > 1:
        warning("Analyzing multiple branches may produce inconsistent results, because commits can occur on multiple branches.") 

    for branch in branches:
        try:
            commits = list(repo.iter_commits(branches, since=since, until=until))
            all_commits.extend(commits)
        except GitCommandError:
            error(f"The branch {branch} is not a existing branch in this repository.")
            sys.exit(1)

    if authors:
        authors = authors.split(",")
        all_commits = [c for c in all_commits if c.author.name in authors]

    return all_commits