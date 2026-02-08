from git import Repo

def analyze_repository(repo: Repo, 
                        metric: str, 
                        since: str | None = None,
                        until: str | None = None,
                        authors: list[str] | None = None) -> list[object]:

    commits = list(repo.iter_commits(
        since=since,
        until=until
    ))

    if authors is not None and len(authors) > 0:
        commits = [c for c in commits if c.author.name in authors]

    if (metric == "commits"):
        return analyze_commits(commits)
    elif (metric == "lines"):
        return analyze_lines(commits)

def analyze_commits(commits):
    commit_data = []

    for c in commits:
        commit_data.append({
            "date": c.committed_datetime,
        })

    return commit_data

def analyze_lines(commits):
    commits_data = []

    for c in commits:
        commits_data.append({
            "date": c.committed_datetime,
            "insertions": c.stats.total["insertions"],
            "deletions": c.stats.total["deletions"],
            "lines": c.stats.total["lines"]
        })
    
    return commits_data