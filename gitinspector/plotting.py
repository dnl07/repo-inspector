import matplotlib.pyplot as plt
from pathlib import Path
from . import plot_utils as utils

def plot_commit_timeline(commit_data: object, save_path: Path | None = None):
    dates, counts = utils.commits_per_day(commit_data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, marker="o", linestyle="-")
    plt.title("Commit frequency over time")
    plt.xlabel("Date")
    plt.ylabel("Number of commits")

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def plot_lines_timeline(commit_data: object, save_path: Path | None = None):
    dates, insertions, deletions, total_lines = utils.lines_per_day(commit_data)

    plt.figure(figsize=(10, 5))
    plt.plot(dates, insertions, marker="o", linestyle="-")
    plt.plot(dates, deletions, marker="o", linestyle="-")
    plt.plot(dates, total_lines, marker="o", linestyle="-")
    plt.title("Lines over time")
    plt.xlabel("Date")
    plt.ylabel("Number of changed lines")

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()