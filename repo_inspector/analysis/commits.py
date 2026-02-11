from collections import Counter

def commits_per_day(commits):
    day_counter = Counter()
    week_counter = Counter()
    month_counter = Counter()
    year_counter = Counter()

    for c in commits:
        dt = c.committed_datetime
        d = dt.date()

        day_counter[d] += 1
        year, week, _ = d.isocalendar()
        week_counter[(year, week)] += 1
        month_counter[(d.year, d.month)] += 1
        year_counter[d.year] += 1

    days = sorted(day_counter.items())
    weeks = sorted(week_counter.items())
    months = sorted(month_counter.items())
    years = sorted(year_counter.items())

    def unpack(counter_items):
        labels, values = zip(*counter_items) if counter_items else ([], [])
        return list(labels), list(values)

    return {
        "days": unpack(days),
        "weeks": unpack(weeks),
        "months": unpack(months),
        "years": unpack(years)
    }