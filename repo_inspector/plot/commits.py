import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
import matplotlib.dates as mdates
from datetime import datetime

def plot_commit_timeline(commit_data):
    all_dates = commit_data["days"][0]

    start, end = min(all_dates), max(all_dates)
    days_range = (end - start).days

    if days_range <= 60:
        interval = "days"
    elif days_range <= 365:
        interval = "weeks"
    elif days_range <= 365*3:
        interval = "months"
    else:
        interval = "years"

    dates, counts = commit_data[interval]

    if interval == "weeks":
        dates = [datetime.strptime(f"{y}-{w}-1", "%G-%V-%u") for y, w in dates]
    elif interval == "months":
        dates = [datetime(y, m, 1) for y, m in dates]
    elif interval == "years":
        dates = [datetime(y, 1, 1) for y in dates]
    elif interval == "days":
        dates = [datetime.combine(d, datetime.min.time()) for d in dates]

    # main line
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, counts, marker="o", linestyle="-", color="#0273a0", linewidth=2, markersize=4)

    # total commits
    total_commits = sum(counts)
    ax.text(
        0.95, 0.95,
        f"Total commits: {total_commits}",
        transform=ax.transAxes,
        ha="right",
        va="top",
        fontsize=10,
        bbox=dict(facecolor="white", alpha=0.7, edgecolor="none")
    )

    # title and axis
    ax.set_title("Commit frequency over time", weight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of commits")

    # major ticks
    if interval == "days":
        locator = mdates.DayLocator()
        fmt = "%Y-%m-%d"
    elif interval == "weeks":
        locator = mdates.WeekdayLocator(byweekday=mdates.MO)
        fmt = "%Y-%m-%d"
    elif interval == "months":
        locator = mdates.MonthLocator()
        fmt = "%Y-%m"
    else:
        locator = mdates.YearLocator()
        fmt = "%Y"

    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(mdates.DateFormatter(fmt))

    # minor ticks
    if interval == "days":
        ax.xaxis.set_minor_locator(mdates.DayLocator())
        ax.tick_params(axis='x', which='minor', length=5, color='gray')
    else:
        ax.xaxis.set_minor_locator(NullLocator())

    ax.grid(True, linestyle="--", alpha=0.5, axis="x")
    fig.autofmt_xdate(rotation=45, ha="right")

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    return fig