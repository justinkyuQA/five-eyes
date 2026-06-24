import json
from pathlib import Path
from datetime import datetime

def review(findings, score):

    reports = Path("reports")
    reports.mkdir(exist_ok=True)

    json_path = reports / "report.json"
    md_path = reports / "report.md"

    json_path.write_text(
        json.dumps(
            {
                "findings": findings,
                "score": score
            },
            indent=2
        ),
        encoding="utf-8"
    )

    with open(md_path, "w", encoding="utf-8") as f:

        f.write("# Five Eyes Report\n\n")

        f.write(
            f"Generated: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
        )

        f.write(
            f"Risk Score: "
            f"{score['score']}\n\n"
        )

        f.write(
            f"Risk Level: "
            f"{score['risk']}\n\n"
        )

        f.write(
            f"Findings Count: "
            f"{len(findings)}\n\n"
        )

        f.write("## Findings\n\n")

        if not findings:
            f.write("- No findings detected\n")
        else:
            for finding in findings:
                f.write(
                    f"- {finding['file']} : "
                    f"{finding['description']}\n"
                )

    return str(json_path), str(md_path)

