import sys

from reviewers.eye1_structure import review as eye1
from reviewers.eye2_rules import review as eye2
from reviewers.eye4_scoring import review as eye4
from reviewers.eye5_report import review as eye5
from reviewers.eye4_confidence import review as confidence_eye
     confidence = confidence_eye(findings)
def main():

    target = sys.argv[1] if len(sys.argv) > 1 else "."

    structure = eye1(target)
    findings = eye2(target)
    score = eye4(findings)

    json_path, md_path = eye5(
        findings,
        score
    )

    print()
    print("===== FIVE EYES =====")
    print()

    print(f"Target: {target}")
    print()

    print(f"Files Scanned: {structure['files_scanned']}")
    print(f"Total Lines: {structure['total_lines']}")

    print()
    print("===== FINDINGS =====")

    if not findings:

        print("No findings.")

    else:

        print(f"Total Findings: {len(findings)}")
        print()

        for finding in findings[:20]:

            print(
                f"{finding['file']} | "
                f"{finding['description']}"
            )

        if len(findings) > 20:

            print()
            print(
                f"... {len(findings)-20} "
                f"additional findings hidden ..."
            )

    print()
    print("===== RISK =====")

    print(f"Score: {score['score']}")
    print(f"Level: {score['risk']}")

    print()
    print("===== REPORTS =====")

    print(json_path)
    print(md_path)
    print()
    print("===== CONFIDENCE =====")

    print(
    f"Confidence: "
    f"{confidence['confidence']}%"
   )

if __name__ == "__main__":
    main()
