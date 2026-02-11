def commits_per_day(commits):
    counts = {}

    for c in commits:
        day = c.committed_datetime.date()
        counts[day] = counts.get(day, 0) + 1

    dates = sorted(counts.keys())
    values = [counts[d] for d in dates]

    return dates, values