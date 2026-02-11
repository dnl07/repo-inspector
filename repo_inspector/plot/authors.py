import matplotlib.pyplot as plt
import numpy as np

def plot_author_pie(author_stats):
    authors = list(author_stats.keys())
    lines = [author_stats[a]["total"] for a in authors]

    fig, ax = plt.figure(figsize=(8, 8))
    ax.pie(lines, labels=authors, autopct="%1.1f%%", startangle=140)
    ax.title("Share of code changed per author")
    return fig

def plot_author_bar(author_stats):
    authors = list(author_stats.keys())
    x = np.arange(len(authors))

    insertions = [author_stats[a]["insertions"] for a in authors]
    deletions = [author_stats[a]["deletions"] for a in authors]
    total = [author_stats[a]["total"] for a in authors]

    fig, ax = plt.figure(figsize=(12, 8))

    p1 = plt.bar(x, insertions, label="Insertions")
    p2 = plt.bar(x, deletions, label="Deletions")

    ax.title("Lines changed per author (insertions + deletions)")
    ax.xticks(x, authors, rotation=45, ha="right")
    ax.legend()

    ax.tight_layout()
    return fig