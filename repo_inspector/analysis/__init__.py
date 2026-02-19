from .commits import commits_per_day
from .lines import lines_per_day
from .authors import lines_per_author, commits_per_author
from .files import lines_per_files, changes_per_files
from .rhythm import (
    commits_per_weekday,
    commits_per_hour,
    commits_heatmap
)
from .messages import top_words

def analyze_all(commits):
    """Analyze all metrics and return a dictionary with all results."""
    return {
        "commits": commits_per_day(commits),
        "lines": lines_per_day(commits),
        "authors": (
            lines_per_author(commits),
            commits_per_author(commits)
        ),
        "files": (
            lines_per_files(commits),
            changes_per_files(commits)
        ),
        "rhythm": (
            commits_per_weekday(commits),
            commits_per_hour(commits),
            commits_heatmap(commits)
        ),
        "messages": top_words(commits)
    }

ANALYZERS = {
    "commits": commits_per_day,
    "lines": lines_per_day,
    "authors": lambda c: (
        lines_per_author(c),
        commits_per_author(c)
    ),
    "files": lambda c: (
        lines_per_files(c),
        changes_per_files(c)
    ),
    "rhythm": lambda c: (
        commits_per_weekday(c),
        commits_per_hour(c),
        commits_heatmap(c)
    ),    
    "messages": top_words,
    "all": analyze_all
}