import sys
from pathlib import Path

from reviewers.eye1_structure import review as eye1
from reviewers.eye2_rules import review as eye2
from reviewers.eye4_scoring import review as eye4
from reviewers.eye4_confidence import review as confidence_eye
from reviewers.eye5_report import review as eye5
from reviewers.eye6_health import review as health_eye
from reviewers.eye7_recommendations import review as recommendations_eye


def scan(target):

    target_path = Path(target).expanduser()

    if not target_path.exists():
        print()
        print("===== FIVE EYES ERROR =====")
        print()
        print(f"Target not found: {target_path}")
        return

    structure = eye1(target_path)
    findings = eye2(target_path)
    findings = recommendations_eye(findings)
    score = eye4(findings)
    confidence = confidence_eye(findings)
    health = health_eye(target_path)

    json_path, md_path = eye5(findings, score)

    # History snapshots removed for clean v0.2.0 release.
    history_path = None

    print()
    print("===== FIVE EYES =====")
    print()
    print(f"Target: {target_path}")
    print()
    print(f"Files Scanned: {structure['files_scanned']}")
    print(f"Total Lines: {structure['total_lines']}")

    print()
    print("===== FINDINGS =====")

    if findings:
        print(f"Total Findings: {len(findings)}")
        print()

        for finding in findings[:20]:
            print(f"{finding['file']} | {finding['description']}")
            print(f"  Recommendation: {finding['recommendation']}")
    else:
        print("No findings.")

    print()
    print("===== RISK =====")
    print(f"Score: {score['score']}")
    print(f"Level: {score['risk']}")

    print()
    print("===== CONFIDENCE =====")
    print(f"Confidence: {confidence['confidence']}%")
    print(f"Action: {confidence['recommendation']}")

    print()
    print("===== PROJECT HEALTH =====")
    print(f"Health Score: {health['health_score']}")

    if health["issues"]:
        for issue in health["issues"]:
            print(f"- {issue['description']}")
    else:
        print("No project health issues detected.")

    print()
    print("===== REPORTS =====")
    print(json_path)
    print(md_path)



def main():
    targets = sys.argv[1:] if len(sys.argv) > 1 else ["."]

    for target in targets:
        scan(target)


if __name__ == "__main__":
    main()
