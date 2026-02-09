from datetime import datetime
import re

def check_datetime(date_str: str) -> None:
    if date_str is None:
        return

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{date_str} is not a valid date") 

def split_authors(authors: str) -> list[str]:
    return []

def extract_github_username(email: str) -> str:
    m = re.match(r"")