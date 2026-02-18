from datetime import datetime
from collections import Counter
from .constants import EXTENSIONS_WHITELIST, STOPWORDS
from .print import error
import sys

def check_datetime(date_str: str) -> None:
    if date_str is None:
        return

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        error(f"The date {date_str} is not a valid date (YYYY-MM-DD).")
        sys.exit(1)

# collects most used names, because sometimes different names appear with same emails
def normalize_authors(commits):
    email_to_names = {}

    for c in commits:
        email = c.author.email.lower()
        name = c.author.name

        if email not in email_to_names:
            email_to_names[email] = [name]
        else:
            email_to_names[email].append(name)
    
    canonical_names = {}
    for email, names in email_to_names.items():
        most_common_name = Counter(names).most_common(1)[0][0]
        canonical_names[email] = most_common_name
    
    return canonical_names

def get_stats_from_commit(commit):
    insertions = 0
    deletions = 0

    for filename, filestats in commit.stats.files.items():
        if not is_text_file(filename):
            continue

        insertions += filestats["insertions"]
        deletions += filestats["deletions"]

    return insertions, deletions, insertions + deletions

def is_text_file(filename: str) -> bool:
    return any(filename.lower().endswith(ext) for ext in EXTENSIONS_WHITELIST)

def is_stopword(word: str) -> bool:
    return word in STOPWORDS