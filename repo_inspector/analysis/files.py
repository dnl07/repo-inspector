from ..utils import is_text_file

def lines_per_files(commits, top_k: int = 25):
    file_stats = {}

    for c in commits:
        if len(c.parents) > 1: 
            continue

        for filename, stats in c.stats.files.items():
            if not is_text_file(filename):
                continue

            if filename not in file_stats:
                file_stats[filename] = {"insertions": 0, "deletions": 0, "total": 0, "changes": 0}
            file_stats[filename]["insertions"] += stats["insertions"]
            file_stats[filename]["deletions"] += stats["deletions"]
            file_stats[filename]["total"] += stats["lines"]
            file_stats[filename]["changes"] += 1

    # Sort all
    sorted_files = sorted(file_stats.keys(), key=lambda f: file_stats[f]["total"], reverse=True)
    sorted_insertions = [file_stats[d]["insertions"] for d in sorted_files]
    sorted_deletions = [file_stats[d]["deletions"] for d in sorted_files]
    sorted_lines = [file_stats[d]["total"] for d in sorted_files]

    sorted_files = sorted_files[:top_k]
    sorted_insertions = sorted_insertions[:top_k]
    sorted_deletions = sorted_deletions[:top_k]
    sorted_lines = sorted_lines[:top_k]

    return sorted_files, sorted_insertions, sorted_deletions, sorted_lines

def changes_per_files(commits, top_k: int = 25):
    file_stats = {}

    for c in commits:
        if len(c.parents) > 1: 
            continue

        for filename, stats in c.stats.files.items():
            if not is_text_file(filename):
                continue

            if filename not in file_stats:
                file_stats[filename] = 0
            file_stats[filename] += 1

    # Sort all
    sorted_files = sorted(file_stats.keys(), key=lambda f: file_stats[f], reverse=True)
    sorted_changes = [file_stats[f] for f in sorted_files]

    sorted_files = sorted_files[:top_k]
    sorted_changes = sorted_changes[:top_k]

    return sorted_files, sorted_changes