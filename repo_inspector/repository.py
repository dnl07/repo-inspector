from git import Repo, GitCommandError

def get_commits(repo: Repo, branches, since=None, until=None, authors=None):
    all_commits = []        

    for branch in branches:
        try:
            commits = list(repo.iter_commits(branches, since=since, until=until))
            all_commits.extend(commits)
        except GitCommandError:
            raise GitCommandError(f"{branch} is not a existing branch in this repository")

    if authors:
        authors = authors.replace(" ", "").split(",")
        all_commits = [c for c in all_commits if c.author.name in authors]

    return all_commits