import matplotlib.pyplot as plt

def plot_lines_timeline(dates, insertions, deletions, total_lines):
    fig, ax = plt.figure(figsize=(10, 5))
    ax.plot(dates, insertions, marker="o", linestyle="-")
    ax.plot(dates, deletions, marker="o", linestyle="-")
    ax.plot(dates, total_lines, marker="o", linestyle="-")
    ax.title("Lines over time")
    ax.xlabel("Date")
    ax.ylabel("Number of changed lines")
    return fig