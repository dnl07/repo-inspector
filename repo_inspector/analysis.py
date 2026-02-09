from . import utils

def commits_per_day(commits):
    counts = {}

    for c in commits:
        day = c.committed_datetime.date()
        counts[day] = counts.get(day, 0) + 1

    dates = sorted(counts.keys())
    values = [counts[d] for d in dates]

    return dates, values

def lines_per_day(commits):
    daily = {}

    for c in commits:
        day = c.committed_datetime.date()
        stats = c.stats.total

        if day not in daily:
            daily[day] = {"insertions": 0, "deletions": 0, "total": 0}

        daily[day]["insertions"] += stats["insertions"]
        daily[day]["deletions"] += stats["deletions"]
        daily[day]["total"] += stats["lines"]

    # Sort all
    sorted_dates = sorted(daily.keys())
    sorted_insertions = [daily[d]["insertions"] for d in sorted_dates]
    sorted_deletions = [daily[d]["deletions"] for d in sorted_dates]
    sorted_lines = [daily[d]["total"] for d in sorted_dates]

    return sorted_dates, sorted_insertions, sorted_deletions, sorted_lines

def lines_per_author(commits):
    authors = {}
    names = utils.normalize_authors(commits)

    for c in commits:
        author = names[c.author.email.lower()]
        stats = c.stats.total

        if author not in authors:
            authors[author] = {"insertions": 0, "deletions": 0, "total": 0}

        authors[author]["insertions"] += stats["insertions"]
        authors[author]["deletions"] += stats["deletions"]
        authors[author]["total"] += stats["lines"]

    return authors

def analyze_files(commits):
    files_data = []

    for c in commits:
        for filename, stats in c.stats.files.items():
            files_data.append({
                "file": filename,
                "insertions": stats.total["insertions"],
                "deletions": stats.total["deletions"],
                "total_lines": stats.total["lines"]
            })

    return files_data 