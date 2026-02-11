from .commits import plot_commit_timeline
from .lines import plot_lines_timeline
from .authors import plot_author_bar, plot_author_pie
from .files import plot_files_changes_bar, plot_files_lines_bar
from .rhythm import (
    plot_weekday_rhythm,
    plot_hours_rhythm,
    plot_heatmap_rhythm
)
from .messages import plot_top_words

PLOTTERS = {
    "commits": lambda data: plot_commit_timeline(*data),
    "lines": lambda data: plot_lines_timeline(*data),
    "authors": lambda data: (
        plot_author_bar(*data),
        plot_author_pie(*data)
    ),
    "files": lambda data: (
        plot_files_changes_bar(*data),
        plot_files_lines_bar(*data)
    ),
    "rhythm": lambda data: (
        plot_weekday_rhythm(*data),
        plot_hours_rhythm(*data),
        plot_heatmap_rhythm(*data)
    ), 
    "messages": lambda data: plot_top_words(data),
}