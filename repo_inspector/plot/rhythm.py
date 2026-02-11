import matplotlib.pyplot as plt
from ..constants import WEEKDAYS

def plot_weekday_rhythm(weekday_counts):
    days = list(weekday_counts.keys())
    counts = [weekday_counts[d] for d in days]

    fig, ax = plt.figure(figsize=(10,5))
    ax.bar(days, counts)
    ax.xticks(days, WEEKDAYS)
    ax.title("Commits per weekday")
    ax.xlabel("Weekday")
    ax.ylabel("Commits")   
    return fig

def plot_hours_rhythm(hour_counts):
    hours = list(hour_counts.keys())
    counts = [hour_counts[h] for h in hours]

    fig, ax = plt.figure(figsize=(10,5))
    ax.bar(hours, counts)
    ax.xticks(hours)
    ax.title("Commits per hour")
    ax.xlabel("Hours")
    ax.ylabel("Commits")
    return fig

def plot_heatmap_rhythm(heat_matrix):
    fig, ax = plt.figure(figsize=(12,5))
    ax.imshow(heat_matrix, aspect="auto")

    ax.yticks(range(7), WEEKDAYS)
    ax.xticks(range(24), range(24))
    ax.title("Weekly commit heatmap")
    return fig