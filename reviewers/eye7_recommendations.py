RECOMMENDATIONS = {
    "Potential XSS sink": "Review innerHTML usage. Prefer textContent when rendering plain text.",
    "Dangerous dynamic execution": "Avoid eval(). Replace with explicit logic or safer parsing.",
    "Dangerous code execution": "Avoid exec(). Use safer structured execution paths.",
    "Hardcoded credential": "Move credentials into environment variables or config files excluded from Git.",
    "Possible secret": "Verify whether this value is sensitive and remove it from source control if needed.",
    "Possible token": "Store tokens outside the repository.",
    "Possible API key": "Store API keys outside source code."
}

def review(findings):
    for finding in findings:
        finding["recommendation"] = RECOMMENDATIONS.get(
            finding["description"],
            "Review this finding manually."
        )

    return findings
