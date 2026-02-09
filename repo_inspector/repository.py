from git import Repo

def get_commits(repo: Repo, since=None, until=None, authors=None):
    commits = list(repo.iter_commits(since=since, until=until))

    if authors:
        commits = [c for c in commits if c.author.name in authors]

    return commits