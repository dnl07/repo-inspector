import matplotlib.pyplot as plt
import numpy as np

def plot_top_words(top_words, save_path=None):
    words = [w[0] for w in top_words]
    counts = [w[1] for w in top_words]
    x = np.arange(len(words))

    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(words, counts)
    ax.set_xticks(x, words, rotation=45, ha="right")
    ax.set_title("Most used words in commit messages")
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Commits")
    return fig