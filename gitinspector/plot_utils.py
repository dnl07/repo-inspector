def commits_per_day(commit_data: list[object]):
    dates = [c["date"].date() for c in commit_data]

    counts = {}

    for date in dates:
        if date in counts:
            counts[date] += 1
        else:
            counts[date] = 1
    
    sorted_dates = sorted(counts.keys())
    sorted_counts = [counts[d] for d in sorted_dates]

    return sorted_dates, sorted_counts

def lines_per_day(commit_data: list[object]):
    insertions = {}
    deletions = {}
    total_lines = {}

    for c in commit_data:
        day = c["date"].date()
        
        # Insertions
        if day in insertions:
            insertions[day] += c["insertions"]
        else:
            insertions[day] = c["insertions"]

        # Deletions
        if day in deletions:
            deletions[day] += c["deletions"]
        else:
            deletions[day] = c["deletions"]
        
        # Total lines
        if day in total_lines:
            total_lines[day] += c["lines"]
        else:
            total_lines[day] = c["lines"]

    # Sort all
    sorted_dates = sorted(insertions.keys())
    sorted_insertions = [insertions[d] for d in sorted_dates]
    sorted_deletions = [deletions[d] for d in sorted_dates]
    sorted_lines = [total_lines[d] for d in sorted_dates]

    return sorted_dates, sorted_insertions, sorted_deletions, sorted_lines