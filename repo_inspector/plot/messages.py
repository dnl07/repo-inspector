import matplotlib.pyplot as plt
import numpy as np

def plot_top_words_bar(top_words):
    words = [w[0] for w in top_words]
    counts = [w[1] for w in top_words]
    x = np.arange(len(words))
    width = 0.6

    # Bars and axis
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.bar(x, counts, width=width, color="#0273a0", label="Commits")

    # Title and axis
    ax.set_title("Most used words in commit messages", weight="bold")
    ax.set_xticks(x, words, rotation=45, ha="right")
    ax.set_ylabel("Commits")

    # Grid
    ax.grid(True, axis="y", linestyle="--", alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    fig.tight_layout()

    return fig