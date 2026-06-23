from pathlib import Path
from rules import RULES

SUPPORTED = {".py", ".js", ".html", ".htm"}

def scan_folder(folder):

    files_scanned = 0
    total_lines = 0

    findings = []

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

            files_scanned += 1
            total_lines += len(text.splitlines())

            print(
                f"[+] {path.name}"
            )

            lower = text.lower()

            for pattern, description in RULES.items():

                if pattern.lower() in lower:

                    findings.append(
                        (
                            path.name,
                            pattern,
                            description
                        )
                    )

        except Exception as e:

            print(
                f"[!] {path}: {e}"
            )

    print()
    print("===== FIVE EYES =====")
    print(f"Files Scanned : {files_scanned}")
    print(f"Total Lines   : {total_lines}")
    print()

    print("===== FINDINGS =====")

    if not findings:

        print("No findings.")

    else:

        for file_name, pattern, description in findings:

            print(
                f"{file_name} | "
                f"{pattern} | "
                f"{description}"
            )

if __name__ == "__main__":
    scan_folder(".")


