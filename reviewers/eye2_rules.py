from pathlib import Path

RULES = {
    "eval(": "Dangerous dynamic execution",
    "exec(": "Dangerous code execution",
    "innerHTML": "Potential XSS sink",
    "password": "Hardcoded credential",
    "secret": "Possible secret",
    "token": "Possible token",
    "api_key": "Possible API key"
}

SUPPORTED = {
    ".py",
    ".js",
    ".html",
    ".htm"
}

def review(folder="."):

    findings = []

    for path in Path(folder).rglob("*"):

        if not path.is_file():
            continue

        if path.suffix.lower() not in SUPPORTED:
            continue

        try:

            text = path.read_text(
                encoding="utf-8",
                errors="ignore"
            )

            lower = text.lower()

            for pattern, description in RULES.items():

                if pattern.lower() in lower:

                    findings.append(
                        {
                            "file": path.name,
                            "pattern": pattern,
                            "description": description
                        }
                    )

        except Exception:
            pass

    return findings

