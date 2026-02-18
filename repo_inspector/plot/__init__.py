from .commits import plot_commit_timeline
from .lines import plot_lines_timeline
from .authors import plot_author_bar, plot_author_pie
from .files import plot_files_changes_heatmap, plot_files_lines_bar
from .rhythm import (
    plot_weekday_rhythm,
    plot_hours_rhythm,
    plot_heatmap_rhythm
)
from .messages import plot_top_words_bar

PLOTTERS = {
    "commits": lambda data: ("commit_timeline", plot_commit_timeline(data)),
    "lines": lambda data: ("lines_timeline", plot_lines_timeline(data)),
    "authors": lambda data: (
        ("author_pie", plot_author_pie(data[0])),
        ("author_bar", plot_author_bar(data[0]))
    ),
    "files": lambda data: (
        ("files_lines_bar", plot_files_lines_bar(*data[0])),
        ("files_changes_heatmap", plot_files_changes_heatmap(*data[1]))
    ),
    "rhythm": lambda data: (
        ("rhythm_weekly", plot_weekday_rhythm(data[0])),
        ("rhythm_hourly", plot_hours_rhythm(data[1])),
        ("rhythm_heatmap", plot_heatmap_rhythm(data[2]))
    ),
    "messages": lambda data: ("messages_top_words", plot_top_words_bar(data)),
    "all":  lambda data: (
        ("commit_timeline", plot_commit_timeline(data["commits"])),
        ("lines_timeline", plot_lines_timeline(data["lines"])),
        ("author_pie", plot_author_pie(data["authors"][0])),
        ("author_bar", plot_author_bar(data["authors"][0])),
        ("files_lines_bar", plot_files_lines_bar(*data["files"][0])),
        ("files_changes_heatmap", plot_files_changes_heatmap(*data["files"][1])),
        ("rhythm_weekly", plot_weekday_rhythm(data["rhythm"][0])),
        ("rhythm_hourly", plot_hours_rhythm(data["rhythm"][1])),
        ("rhythm_heatmap", plot_heatmap_rhythm(data["rhythm"][2])),
        ("messages_top_words", plot_top_words_bar(data["messages"]))
    )
}