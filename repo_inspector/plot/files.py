import matplotlib.pyplot as plt
import numpy as np

def plot_files_lines_bar(file_stats):
    files = list(file_stats.keys())
    x = np.arange(len(files))

    insertions = [file_stats[f]["insertions"] for f in files]
    deletions = [file_stats[f]["deletions"] for f in files]
    total = [file_stats[f]["total"] for f in files]

    fig, ax = plt.figure(figsize=(12, 8))

    p1 = ax.bar(x, insertions, label="Insertions")
    p2 = ax.bar(x, deletions, label="Deletions")

    ax.title("Lines changed per file (insertions + deletions)")
    ax.xticks(x, files, rotation=45, ha="right")
    ax.legend()

    ax.tight_layout()   
    return fig  

def plot_files_changes_bar(file_stats):
    files = list(file_stats.keys())
    x = np.arange(len(files))

    changes = [file_stats[f]["changes"] for f in files]

    fig, ax = plt.figure(figsize=(12, 8))

    p2 = ax.bar(x, changes, label="Changes")

    ax.title("Most changed files")
    ax.xticks(x, files, rotation=45, ha="right")
    ax.legend()

    ax.tight_layout()
    return fig 