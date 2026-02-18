from git import Repo, GitCommandError
import sys
from .print import error, info
from pathlib import Path
import tempfile

def load_repo(path_or_url: str):
    if Path(path_or_url).exists():
        try:
            repo = Repo(path_or_url)
            return repo, None
        except Exception:
            error(f"The path {path_or_url} is not a valid Git repository.")
            sys.exit(1)
    
    if path_or_url.startswith(("http://", "https://", "git://")):
        tmp_dir = tempfile.TemporaryDirectory(prefix="repo_")
        info(f"Cloning repository from {path_or_url} to temporary directory...")
        try:
            repo = Repo.clone_from(path_or_url, tmp_dir.name)
            return repo, tmp_dir
        except Exception:
                error(f"Failed to clone repository from {path_or_url}. Please check the URL and your network connection.")
                sys.exit(1)
        
    error(f"The path {path_or_url} does not exist and is not a valid URL.")
    sys.exit(1)

def get_commits(repo: Repo, branches, since=None, until=None, authors=None):
    results = []

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