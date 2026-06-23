from pathlib import Path

SUPPORTED = {
    ".py",
    ".js",
    ".html",
    ".htm"
}

def review(folder="."):

    files_scanned = 0
    total_lines = 0

    for path in Path(folder).rglob("*"):

        if not path.is_file():
            continue

        if path.suffix.lower() not in SUPPORTED:
            continue

        try:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            files_scanned += 1
            total_lines += len(
                text.splitlines()
            )

        except Exception:
            pass

    return {
        "files_scanned": files_scanned,
        "total_lines": total_lines
    }
