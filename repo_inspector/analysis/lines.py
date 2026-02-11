from ..utils import get_stats_from_commit

def lines_per_day(commits):
    daily = {}

    for c in commits:
        if len(c.parents) > 1: 
            continue

        day = c.committed_datetime.date()
        insertions, deletions, total = get_stats_from_commit(c)

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
