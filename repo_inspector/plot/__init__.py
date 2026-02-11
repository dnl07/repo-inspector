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
    "commits": {
        "timeline": lambda data: plot_commit_timeline(data)
    },
    "lines": {
        "timeline": lambda data: plot_lines_timeline(data)
    },
    "authors": {
        "pie": lambda data: plot_author_pie(data[0]),
        "bar": lambda data: plot_author_bar(data[0])
    },
    "files": {
        "bar": lambda data: plot_files_lines_bar(*data[0]),
        "heatmap": lambda data: plot_files_changes_heatmap(*data[1])
    },
    "rhythm": {
        "weekly": lambda data: plot_weekday_rhythm(data[0]),
        "hourly": lambda data: plot_hours_rhythm(data[1]),
        "heatmap": lambda data: plot_heatmap_rhythm(data[2])
    },
    "messages": {
        "bar": lambda data: plot_top_words_bar(data)
    }
}

PLOT_OPTIONS = {
    "commits": ["timeline"],
    "lines": ["timeline"],
    "authors": ["pie", "bar"],
    "files": ["bar", "heatmap"],
    "rhythm": ["weekly", "hourly", "heatmap"],
    "messages": ["bar"]
}