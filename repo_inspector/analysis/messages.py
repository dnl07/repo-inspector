import re

def top_words(commits, top_k: int = 25):
    word_counts = {}

    for c in commits:
        if len(c.parents) > 1: 
            continue     
    
        msg = c.message.lower()
        msg = re.sub(r"[^a-z]", " ", msg) 

        words = msg.split()

        for w in words:
            if w not in word_counts:
                word_counts[w] = 0
            word_counts[w] += 1

    sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_words[:top_k]