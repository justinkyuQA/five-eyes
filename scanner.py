from pathlib import Path

SUPPORTED = {".py", ".js", ".html", ".htm"}

def scan_folder(folder):
    files_scanned = 0
    total_lines = 0

    extensions = {}

    for path in Path(folder).rglob("*"):
        if not path.is_file():
            continue

        ext = path.suffix.lower()

        if ext not in SUPPORTED:
            continue

        try:
            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            line_count = len(text.splitlines())

            files_scanned += 1
            total_lines += line_count

            extensions[ext] = (
                extensions.get(ext, 0) + 1
            )

            print(
                f"[+] {path.name} "
                f"({line_count} lines)"
            )

        except Exception as e:
            print(
                f"[!] Failed: {path} : {e}"
            )

    print()
    print("===== FIVE EYES =====")
    print(f"Files Scanned : {files_scanned}")
    print(f"Total Lines   : {total_lines}")
    print()

    for ext, count in sorted(
        extensions.items()
    ):
        print(f"{ext}: {count}")

if __name__ == "__main__":
    scan_folder(".")

