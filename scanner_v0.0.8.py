from reviewers.eye1_structure import review as eye1
from reviewers.eye2_rules import review as eye2
from reviewers.eye4_scoring import review as eye4

def main():

    structure = eye1(".")
    findings = eye2(".")
    score = eye4(findings)

    print()
    print("===== FIVE EYES =====")
    print()

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

    print()
    print("===== RISK =====")

    print(
        f"Score: {score['score']}"
    )

    print(
        f"Level: {score['risk']}"
    )

if __name__ == "__main__":
    main()
