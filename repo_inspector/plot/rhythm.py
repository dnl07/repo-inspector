import matplotlib.pyplot as plt
import numpy as np
from ..constants import WEEKDAYS

def plot_weekday_rhythm(weekday_counts):
    days = list(weekday_counts.keys())
    counts = [weekday_counts[d] for d in days]
    x = np.arange(len(days))
    width = 0.6

    # Bars
    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(x, counts, width=width, color="#0273a0", label="Commits")

    # Title and axis
    ax.set_title("Commits per weekday")
    ax.set_xticks(x)
    ax.set_xticklabels([WEEKDAYS[d] for d in days], rotation=45, ha="right")
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Commits")  

    # Gtid
    ax.grid(True, axis="y", linestyle="--", alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    fig.tight_layout()
 
    return fig

def plot_hours_rhythm(hour_counts):
    hours = list(hour_counts.keys())
    counts = [hour_counts[h] for h in hours]
    x = np.arange(len(hours))
    width = 0.6

    fig, ax = plt.subplots(figsize=(12,5))
    ax.bar(x, counts, width=width, color="#0273a0", label="Commits")

    # Title and axis
    ax.set_title("Commits per hour")
    ax.set_xticks(x)
    ax.set_xticklabels(hours, rotation=45, ha="right")
    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Commits")  

    # Grid
    ax.grid(True, axis="y", linestyle="--", alpha=0.5)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    fig.tight_layout()

def plot_heatmap_rhythm(heat_matrix):
    fig, ax = plt.subplots(figsize=(12,5))
    cax = ax.imshow(heat_matrix, aspect="auto", cmap="YlOrRd", origin="lower")

    # Axis
    ax.set_yticks(np.arange(7))
    ax.set_yticklabels(WEEKDAYS)
    ax.set_xticks(np.arange(24))
    ax.set_xticklabels(np.arange(24))

    ax.set_xlabel("Hour of the day")
    ax.set_ylabel("Weekday")
    ax.set_title("Weekly commit heatmap", weight="bold")

    cbar = fig.colorbar(cax, ax=ax)
    cbar.set_label("Number of commits")

    fig.tight_layout()
    return fig