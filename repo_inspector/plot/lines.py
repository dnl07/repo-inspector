import matplotlib.pyplot as plt
from matplotlib.ticker import NullLocator
import matplotlib.dates as mdates
from datetime import datetime

def plot_lines_timeline(lines_data):
    all_dates = lines_data["days"][0]

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

    dates, insertions, deletions, total = lines_data[interval]

    if interval == "weeks":
        dates = [datetime.strptime(f"{y}-{w}-1", "%G-%V-%u") for y, w in dates]
    elif interval == "months":
        dates = [datetime(y, m, 1) for y, m in dates]
    elif interval == "years":
        dates = [datetime(y, 1, 1) for y in dates]
    elif interval == "days":
        dates = [datetime.combine(d, datetime.min.time()) for d in dates]

    # main lines
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(dates, insertions, marker="o", linestyle="-", color="lightgreen", label="Insertions")
    ax.plot(dates, deletions, marker="o", linestyle="-", color="salmon", label="Deletions")
    ax.plot(dates, total, marker="o", linestyle="-", color="#5e5e5e", label="Total")

    # title and axis
    ax.set_title("Lines changed over time", weight="bold")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of lines")

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
    ax.legend()

    return fig