import matplotlib.pyplot as plt

def plot_lines_timeline(dates, insertions, deletions, total_lines):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, insertions, marker="o", linestyle="-")
    ax.plot(dates, deletions, marker="o", linestyle="-")
    ax.plot(dates, total_lines, marker="o", linestyle="-")
    ax.set_title("Lines over time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of changed lines")
    return fig