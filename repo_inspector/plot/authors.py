import matplotlib.pyplot as plt
import numpy as np

def plot_author_pie(author_stats):
    authors = list(author_stats.keys())
    lines = [author_stats[a]["total"] for a in authors]

    # colors
    cmap = plt.get_cmap("tab20")
    colors = [cmap(i) for i in range(len(authors))]

    # pie
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(
        lines,
        labels=authors,
        autopct=lambda pct: f"{pct:.1f}%",
        startangle=140,
        colors=colors,
        wedgeprops={"edgecolor": "white", "linewidth": 1}
    )

    # title
    ax.set_title("Share of code changed per author", weight="bold")
    fig.tight_layout()

    return fig

def plot_author_bar(author_stats):
    data = [(a, stats["insertions"], stats["deletions"], stats["total"]) for a, stats in author_stats.items()]
    authors, insertions, deletions, total = zip(*data)

    x = np.arange(len(authors))
    width = 0.6

    fig, ax = plt.subplots(figsize=(12, 8))

    # bars
    ax.bar(x, deletions, width=width, label="Deletions", color="salmon")
    ax.bar(x, insertions, width=width, bottom=deletions, label="Insertions", color="lightgreen")

    ax.set_title("Lines changed per author (Insertions + Deletions)", weight="bold")
    ax.set_xticks(x, authors, rotation=45, ha="right")
    ax.set_ylabel("Number of lines")

    ax.grid(True, axis="y", linestyle="--", alpha=0.5)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend()
    fig.tight_layout()
    return fig