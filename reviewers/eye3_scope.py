IGNORE_DIRS = {
    ".git",
    "__pycache__",
    "reviewers"
}

IGNORE_FILES = {
    "rules.py",
    "scanner.py"
}

def should_scan(path):

    parts = set(path.parts)

    for item in IGNORE_DIRS:
        if item in parts:
            return False

    if path.name in IGNORE_FILES:
        return False

    return True

