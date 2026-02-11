from collections import Counter
from ..utils import get_stats_from_commit

def lines_per_day(commits):
    day_counter = {}
    week_counter = {}
    month_counter = {}
    year_counter = {}

    for c in commits:
        if len(c.parents) > 1:
            continue

        dt = c.committed_datetime
        day = dt.date()
        insertions, deletions, total = get_stats_from_commit(c)

        # days
        if day not in day_counter:
            day_counter[day] = {"insertions": 0, "deletions": 0, "total": 0}         
        day_counter[day]["insertions"] += insertions
        day_counter[day]["deletions"] += deletions
        day_counter[day]["total"] += total

        # weeks
        year, week, _ = day.isocalendar()
        if (year, week) not in week_counter:
            week_counter[(year, week)] = {"insertions": 0, "deletions": 0, "total": 0}
        week_counter[(year, week)]["insertions"] += insertions
        week_counter[(year, week)]["deletions"] += deletions
        week_counter[(year, week)]["total"] += total

        # months
        if (day.year, day.month) not in month_counter:
            month_counter[(day.year, day.month)] = {"insertions": 0, "deletions": 0, "total": 0}
        month_counter[(day.year, day.month)]["insertions"] += insertions
        month_counter[(day.year, day.month)]["deletions"] += deletions
        month_counter[(day.year, day.month)]["total"] += total

        # years
        if day.year not in year_counter:
            year_counter[day.year] = {"insertions": 0, "deletions": 0, "total": 0}
            year_counter[day.year]["insertions"] = 0
            year_counter[day.year]["deletions"] = 0
            year_counter[day.year]["total"] = 0
        year_counter[day.year]["insertions"] += insertions
        year_counter[day.year]["deletions"] += deletions
        year_counter[day.year]["total"] += total

    def unpack(counter):
        dates = sorted(counter.keys())
        insertions = [counter[d]["insertions"] for d in dates]
        deletions = [counter[d]["deletions"] for d in dates]
        totals = [counter[d]["total"] for d in dates]
        return dates, insertions, deletions, totals

    return {
        "days": unpack(day_counter),
        "weeks": unpack(week_counter),
        "months": unpack(month_counter),
        "years": unpack(year_counter)
    }