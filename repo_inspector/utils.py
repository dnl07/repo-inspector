from datetime import datetime
from collections import Counter

def check_datetime(date_str: str) -> None:
    if date_str is None:
        return

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{date_str} is not a valid date") 

def split_authors(authors: str) -> list[str]:
    return []

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