import matplotlib.pyplot as plt

def plot_commit_timeline(dates, counts):
    fig, ax = plt.figure(figsize=(10, 5))
    ax.plot(dates, counts, marker="o", linestyle="-")
    ax.title("Commit frequency over time")
    ax.xlabel("Date")
    ax.ylabel("Number of commits")
    return fig