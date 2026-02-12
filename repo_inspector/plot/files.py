import matplotlib.pyplot as plt
import numpy as np

def plot_files_lines_bar(files, insertions, deletions, total):
    x = np.arange(len(files))
    width = 0.6

    fig, ax = plt.subplots(figsize=(16, 8))

    # bars
    ax.bar(x, deletions, width=width, label="Deletions", color="salmon")
    ax.bar(x, insertions, width=width, bottom=deletions, label="Insertions", color="lightgreen")

    ax.set_title("Lines changed per file (Insertions + Deletions)", weight="bold")
    ax.set_xticks(x, files, rotation=45, ha="right")
    ax.set_ylabel("Number of lines changed")

    ax.grid(True, axis="y", linestyle="--", alpha=0.5)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    ax.legend()
    fig.tight_layout()
    return fig

def plot_files_changes_heatmap(files, changes):
    data = np.array(changes).reshape(-1, 1)

    fig, ax = plt.subplots(figsize=(12, max(6, len(files)*0.3)))

    cax = ax.imshow(data, cmap="Reds", aspect="auto")

    ax.set_yticks(np.arange(len(files)))
    ax.set_yticklabels(files)
    
    ax.set_xticks([0])
    ax.set_xticklabels(["Changes"])

    cbar = fig.colorbar(cax)
    cbar.set_label("Number of changes")

    ax.set_title("Most changed files (Heatmap)")    

    fig.tight_layout()
    return fig 