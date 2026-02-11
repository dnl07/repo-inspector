import matplotlib.pyplot as plt
from ..constants import WEEKDAYS

def plot_weekday_rhythm(weekday_counts):
    days = list(weekday_counts.keys())
    counts = [weekday_counts[d] for d in days]

    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(days, counts)
    ax.set_xticks(days, WEEKDAYS)
    ax.set_title("Commits per weekday")
    ax.set_xlabel("Weekday")
    ax.set_ylabel("Commits")   
    return fig

def plot_hours_rhythm(hour_counts):
    hours = list(hour_counts.keys())
    counts = [hour_counts[h] for h in hours]

    fig, ax = plt.subplots(figsize=(10,5))
    ax.bar(hours, counts)
    ax.set_xticks(hours)
    ax.set_title("Commits per hour")
    ax.set_xlabel("Hours")
    ax.set_ylabel("Commits")
    return fig

def plot_heatmap_rhythm(heat_matrix):
    fig, ax = plt.subplots(figsize=(12,5))
    ax.imshow(heat_matrix, aspect="auto")

    ax.set_yticks(range(7), WEEKDAYS)
    ax.set_xticks(range(24), range(24))
    ax.set_title("Weekly commit heatmap")
    return fig