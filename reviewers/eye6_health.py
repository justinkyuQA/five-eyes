from pathlib import Path

def review(target="."):
    target = Path(target)

    checks = {
        "README.md": False,
        "LICENSE": False,
        "requirements.txt": False,
        "screenshots": False,
        "reports": False,
    }

    for item in checks:
        if (target / item).exists():
            checks[item] = True

    issues = []

    for item, exists in checks.items():
        if not exists:
            issues.append({
                "category": "Project Health",
                "file": item,
                "description": f"Missing {item}",
                "recommendation": f"Consider adding {item}."
            })

    score = 100 - (len(issues) * 10)

    if score < 0:
        score = 0

    return {
        "health_score": score,
        "issues": issues
    }
