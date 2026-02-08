from datetime import datetime

def check_datetime(date_str: str) -> None:
    if date_str is None:
        return

    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError(f"{date_str} is not a valid date") 

def split_authors(authors: str) -> list[str]:
    return []