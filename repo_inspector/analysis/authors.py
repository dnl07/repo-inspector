from ..utils import normalize_authors, get_stats_from_commit

def lines_per_author(commits):
    authors = {}
    names = normalize_authors(commits)

    for c in commits:
        if len(c.parents) > 1: 
            continue

        author = names[c.author.email.lower()]
        insertions, deletions, total = get_stats_from_commit(c)

        if author not in authors:
            authors[author] = {"insertions": 0, "deletions": 0, "total": 0}

        authors[author]["insertions"] += insertions
        authors[author]["deletions"] += deletions
        authors[author]["total"] += total

    return authors

def commits_per_author(commits):
    authors = {}
    names = normalize_authors(commits)

    for c in commits:
        if len(c.parents) > 1: 
            continue

        author = names[c.author.email.lower()]
        insertions, deletions, total = get_stats_from_commit(c)

        if author not in authors:
            authors[author] = {"insertions": 0, "deletions": 0, "total": 0}

        authors[author]["insertions"] += insertions
        authors[author]["deletions"] += deletions
        authors[author]["total"] += total

    return authors