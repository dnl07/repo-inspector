import matplotlib.pyplot as plt

def plot_commit_timeline(dates, counts):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dates, counts, marker="o", linestyle="-")
    ax.set_title("Commit frequency over time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of commits")
    return fig