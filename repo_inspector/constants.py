EXTENSIONS_WHITELIST = [
    # Source code
    ".py", ".c", ".cpp", ".cxx", ".h", ".hpp", ".hxx",
    ".java", ".js", ".jsx", ".ts", ".tsx",
    ".go", ".rs", ".kt", ".kts", ".swift",
    ".rb", ".php", ".pl", ".cs",

    # Web
    ".html", ".htm", ".css", ".scss",

    # Shell / Scripting
    ".sh", ".bash", ".zsh", ".ksh", ".fish",
    ".bat", ".cmd", ".ps1",

    # Documentation
    ".txt", ".md", ".markdown", ".rst", ".tex", ".bib"
]

WEEKDAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves",
    "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself",
    "it", "its", "itself", "they", "them", "their", "theirs", "themselves",
    "what", "which", "who", "whom", "this", "that", "these", "those",
    "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", 
    "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", 
    "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
    "for", "with", "about", "against", "between", "into", "through",
    "during", "before", "after", "above", "below", "to", "from", "up", "down",
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", 
    "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more", "most", "other", "some", "such",
    "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very",
    "s", "t", "can", "will", "just", "don", "should", "now"
}