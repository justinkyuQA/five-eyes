from reviewers.eye1_structure import review as eye1
from reviewers.eye2_rules import review as eye2

def main():

    print()
    print("===== FIVE EYES =====")
    print()

    structure = eye1(".")
    findings = eye2(".")

    print(
        f"Files Scanned: "
        f"{structure['files_scanned']}"
    )

    print(
        f"Total Lines: "
        f"{structure['total_lines']}"
    )

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
