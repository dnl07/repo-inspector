from . import utils
import numpy as np

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
        if len(c.parents) > 1: 
            continue

        day = c.committed_datetime.date()
        insertions, deletions, total = utils.get_stats_from_commit(c)

        if day not in daily:
            daily[day] = {"insertions": 0, "deletions": 0, "total": 0}

        daily[day]["insertions"] += insertions
        daily[day]["deletions"] += deletions
        daily[day]["total"] += total

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
        if len(c.parents) > 1: 
            continue

        author = names[c.author.email.lower()]
        insertions, deletions, total = utils.get_stats_from_commit(c)

        if author not in authors:
            authors[author] = {"insertions": 0, "deletions": 0, "total": 0}

        authors[author]["insertions"] += insertions
        authors[author]["deletions"] += deletions
        authors[author]["total"] += total

    return authors

def commits_per_author(commits):
    authors = {}
    names = utils.normalize_authors(commits)

    for c in commits:
        if len(c.parents) > 1: 
            continue

        author = names[c.author.email.lower()]
        insertions, deletions, total = utils.get_stats_from_commit(c)

        if author not in authors:
            authors[author] = {"insertions": 0, "deletions": 0, "total": 0}

        authors[author]["insertions"] += insertions
        authors[author]["deletions"] += deletions
        authors[author]["total"] += total

    return authors

def changes_per_files(commits, top_n: int = 10):
    file_stats = {}

    for c in commits:
        if len(c.parents) > 1: 
            continue

        for filename, stats in c.stats.files.items():
            if not utils.is_text_file(filename):
                continue

            if filename not in file_stats:
                file_stats[filename] = {"insertions": 0, "deletions": 0, "total": 0, "changes": 0}
            file_stats[filename]["insertions"] += stats["insertions"]
            file_stats[filename]["deletions"] += stats["deletions"]
            file_stats[filename]["total"] += stats["lines"]
            file_stats[filename]["changes"] += 1

    sorted_files = dict(sorted(file_stats.items(), key=lambda x: x[1]["total"], reverse=True)[:top_n])
    return sorted_files

def commits_per_weekday(commits):
    weekday_counts = {i: 0 for i in range(7)}

    for c in commits:
        if len(c.parents) > 1: 
            continue        

        wd = c.committed_datetime.weekday()
        weekday_counts[wd] += 1
    
    return weekday_counts

def commits_per_hour(commits):
    hour_counts = {h: 0 for h in range(24)}

    for c in commits:
        if len(c.parents) > 1: 
            continue        

        h = c.committed_datetime.hour
        hour_counts[h] += 1
    
    return hour_counts

def commits_heatmap(commits):
    heat = np.zeros((7, 24), dtype=int)

    for c in commits:
        if len(c.parents) > 1: 
            continue        

        wd = c.committed_datetime.weekday()
        h = c.committed_datetime.hour
        heat[wd, h] += 1
    
    return heat    