from pathlib import Path
import matplotlib.pyplot as plt

def plot_commit_timeline(dates, counts, save_path: Path | None = None):
    plt.figure(figsize=(10, 5))
    plt.plot(dates, counts, marker="o", linestyle="-")
    plt.title("Commit frequency over time")
    plt.xlabel("Date")
    plt.ylabel("Number of commits")

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()

def plot_lines_timeline(dates, insertions, deletions, total_lines, save_path: Path | None = None):
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

def plot_author_pie(author_stats, save_path: Path | None = None):
    authors = list(author_stats.keys())
    lines = [author_stats[a]["total"] for a in authors]

    plt.figure(figsize=(8, 8))
    plt.pie(lines, labels=authors, autopct="%1.1f%%", startangle=140)
    plt.title("Share of code changed per author")

    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()