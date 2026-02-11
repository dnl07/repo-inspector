import matplotlib.pyplot as plt
import numpy as np

def plot_files_lines_bar(files, insertions, deletions, total):
    x = np.arange(len(files))

    fig, ax = plt.subplots(figsize=(12, 8))

    p1 = ax.bar(x, insertions, label="Insertions")
    p2 = ax.bar(x, deletions, label="Deletions")

    ax.set_title("Lines changed per file (insertions + deletions)")
    ax.set_xticks(x, files, rotation=45, ha="right")
    ax.legend()

    fig.tight_layout()   
    return fig  

def plot_files_changes_bar(files, changes):
    x = np.arange(len(files))

    fig, ax = plt.subplots(figsize=(12, 8))

    p2 = ax.bar(x, changes, label="Changes")

    ax.set_title("Most changed files")
    ax.set_xticks(x, files, rotation=45, ha="right")
    ax.legend()

    fig.tight_layout()
    return fig 