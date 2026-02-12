EXTENSIONS_WHITELIST = {
    # Python
    ".py", ".pyi", ".pyc", ".pyd", ".pyo",
    
    # C/C++
    ".c", ".cpp", ".cxx", ".h", ".hpp", ".hxx",
    
    # Java
    ".java", ".class", ".jar",
    
    # JavaScript/TypeScript
    ".js", ".jsx", ".ts", ".tsx",
    
    # Web
    ".html", ".htm", ".css", ".scss", ".less", ".xml", ".xhtml",
    
    # Shell
    ".sh", ".bash", ".zsh", ".bat", ".ps1", ".cmd", ".ksh", ".fish",
    
    # Ruby, Perl, PHP
    ".rb", ".pl", ".pm", ".php",
    
    # Go, Rust
    ".go", ".rs",
    
    # Kotlin, Swift
    ".kt", ".kts", ".swift",
    
    # Text files and documentation
    ".txt", ".md", ".markdown", ".rst", ".tex", ".bib", ".csv", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".log",
    
    # SQL
    ".sql", ".db", ".sqlite", ".sqlite3",

    # Makefiles & CI
    "Makefile", "makefile", "Dockerfile", "Jenkinsfile", ".gitignore", ".gitattributes", ".editorconfig",
}

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