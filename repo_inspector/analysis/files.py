from ..utils import is_text_file

def changes_per_files(commits, top_n: int = 10):
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

    sorted_files = dict(sorted(file_stats.items(), key=lambda x: x[1]["total"], reverse=True)[:top_n])
    return sorted_files