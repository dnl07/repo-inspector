import numpy as np

def commits_per_weekday(commits):
    weekday_counts = {i: 0 for i in range(7)}

    for c in commits:
        if len(c.parents) > 1: 
            continue        

        wd = c.committed_datetime.weekday()
        weekday_counts[wd] += 1
    
    return weekday_counts

def commits_per_hour(commits):
    hour_counts = {h: 0 for h in range(24)}

    for c in commits:
        if len(c.parents) > 1: 
            continue        

        h = c.committed_datetime.hour
        hour_counts[h] += 1
    
    return hour_counts

def commits_heatmap(commits):
    heat = np.zeros((7, 24), dtype=int)

    for c in commits:
        if len(c.parents) > 1: 
            continue        

        wd = c.committed_datetime.weekday()
        h = c.committed_datetime.hour
        heat[wd, h] += 1
    
    return heat 