from pathlib import Path

from reviewers.eye1_structure import review as eye1
from reviewers.eye2_rules import review as eye2

def main():

    target = "."

    print()
    print("===== FIVE EYES =====")
    print()

    structure = eye1(target)
    findings = eye2(target)

    print(f"Files Scanned: {structure['files_scanned']}")
    print(f"Total Lines: {structure['total_lines']}")

    print()
    print("===== FINDINGS =====")

    if not findings:
        print("No findings.")
    else:
        for finding in findings:
            print(
                f"{finding['file']} | "
                f"{finding['description']}"
            )

if __name__ == "__main__":
    main()
