def review(findings):

    count = len(findings)

    if count == 0:
        confidence = 95

    elif count <= 3:
        confidence = 85

    elif count <= 10:
        confidence = 70

    else:
        confidence = 50

    if confidence >= 80:
        recommendation = "PASS"

    elif confidence >= 60:
        recommendation = "REVIEW"

    else:
        recommendation = "ESCALATE"

    return {
        "confidence": confidence,
        "recommendation": recommendation
    }
