from reviewers.eye1_structure import review as eye1
from reviewers.eye2_rules import review as eye2
from reviewers.eye4_scoring import review as eye4
from reviewers.eye5_report import review as eye5

def main():

    structure = eye1(".")
    findings = eye2(".")
    score = eye4(findings)

    json_path, md_path = eye5(
        findings,
        score
    )

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

    print()
    print("===== REPORTS =====")

    print(json_path)
    print(md_path)

if __name__ == "__main__":
    main()
