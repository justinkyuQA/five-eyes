SCORES = {
    "Dangerous dynamic execution": 8,
    "Dangerous code execution": 8,
    "Potential XSS sink": 4,
    "Hardcoded credential": 5,
    "Possible secret": 5,
    "Possible token": 5,
    "Possible API key": 5
}

def review(findings):

    score = 0

    for finding in findings:

        description = finding["description"]

        score += SCORES.get(
            description,
            1
        )

    if score >= 15:
        risk = "HIGH"
    elif score >= 8:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return {
        "score": score,
        "risk": risk
    }
