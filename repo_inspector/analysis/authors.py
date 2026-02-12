from ..utils import normalize_authors, get_stats_from_commit

def lines_per_author(commits, min_percent=1.0):
    author_stats = {}
    names = normalize_authors(commits)

    for c in commits:
        if len(c.parents) > 1: 
            continue

        author = names[c.author.email.lower()]
        insertions, deletions, total = get_stats_from_commit(c)

        if author not in author_stats:
            author_stats[author] = {"insertions": 0, "deletions": 0, "total": 0}

        author_stats[author]["insertions"] += insertions
        author_stats[author]["deletions"] += deletions
        author_stats[author]["total"] += total

    total_lines = sum(a["total"] for a in author_stats.values())

    result = {}
    others = {"insertions": 0, "deletions": 0, "total": 0, "count": 0}

    for author, stats in author_stats.items():
        percent = stats["total"] / total_lines * 100
        if percent < min_percent:
            others["insertions"] += stats["insertions"]
            others["deletions"] += stats["deletions"]
            others["total"] += stats["total"]
            others["count"] += 1
        else:
            result[author] = stats

    if others["total"] > 0:
        result["Others"] = others

    result = dict(sorted(result.items(), key=lambda x: x[1]["total"], reverse=True))

    return result

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