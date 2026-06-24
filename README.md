Five Eyes

Five Eyes is a local-first security inspection pipeline that analyzes source code and produces actionable findings, risk scores, health assessments, reports, and historical snapshots.

Rather than relying on large cloud-hosted systems, Five Eyes processes projects through a chain of focused review stages ("Eyes"), allowing findings to be collected, classified, scored, and preserved locally.

Features

- Local-first operation
- Multi-stage review pipeline
- Security finding detection
- Risk scoring
- Confidence scoring
- Project health assessment
- Markdown and JSON reports
- Historical scan memory
- No network connection required

Example Workflow

Project
→ Five Eyes
→ Findings
→ Risk Score
→ Health Score
→ Report
→ History Snapshot

Example Findings

- Dangerous dynamic execution
- Potential XSS sink
- Missing project documentation
- Missing project artifacts
- Project health issues

Screenshots

- Empty Project Health Audit
- Live Security Findings
- Architecture Overview
- Generated Report Output

Current Status

Version: v0.2.0

Status: Functional Release Candidate

Capabilities:

- Structure Review
- Rule Review
- Risk Assessment
- Confidence Assessment
- Project Health Analysis
- Report Generation
- Historical Snapshot Storage













# Five Eyes

Five Eyes is a local-first code review and risk analysis pipeline built around independent reviewers ("Eyes").

Each Eye performs a focused task and passes structured findings forward, allowing code to be analyzed incrementally before requiring human review or larger reasoning systems.

---

# Development Timeline

## v0.0.1 — Architecture Foundation

- Repository established
- Philosophy documented
- Architecture documented
- Roadmap documented

---

## v0.0.2 — Eye One Scanner

- File discovery implemented
- Line counting implemented
- Extension classification implemented
- First executable reviewer released

---

## v0.0.3 — Rule Detection Prototype

- Pattern matching implemented
- Detection patterns added
- First security findings generated

---

## v0.0.4 — Eye One Modular Architecture

Status: Complete

### Achievements

- Reviewer architecture established
- Eye One extracted into independent module
- Scanner converted into orchestration layer
- Foundation established for Eyes Two through Five

### Evidence

Screenshot:

![Eye One](screenshots/fiveeyesone.jpg)

Tag:

#eyeone

Output:

- Files Scanned: 6
- Total Lines: 154

### Lesson Learned

Stable reviewers should be added, not repeatedly rewritten.

New capabilities should arrive as new Eyes rather than continuously modifying existing Eyes.

---

# Current Status

- Eye One: Complete ✓
- Eye Two: Next
- Eye Three: Planned
- Eye Four: Planned
- Eye Five: Planned

---

# Vision

Eye One  -> Structure

Eye Two  -> Rules

Eye Three -> Patterns

Eye Four -> Scoring

Eye Five -> Reporting

Each Eye should be independently testable, independently releasable, and independently understandable.

## v0.0.5 — Eye Two Rule Reviewer

Status: Complete

### Achievements

- Independent Eye Two reviewer created
- Rule-based detection implemented
- Dangerous pattern detection added
- Multi-reviewer architecture proven

### Evidence

Screenshot:
screenshots/fiveeyestoo.jpg

Tag:
#eyetoo

### Findings Detected

- Dangerous dynamic execution
- Dangerous code execution
- Potential XSS sink
- Hardcoded credential
- Possible secret
- Possible token
- Possible API key

### Lesson Learned

Reviewers can accidentally review themselves.

Future versions should support scope controls and exclusions.
## v0.0.5 — Eye Two Rule Reviewer

Status: Complete

### Achievements

- Independent Eye Two reviewer created
- Rule-based detection implemented
- Multi-reviewer architecture proven
- Structure reviewer and rule reviewer operating together

### Evidence

Screenshot:

![Eye Two](screenshots/fiveeyestoo.jpg)

Tag:

#eyetoo

### Findings Detected

- Dangerous dynamic execution
- Dangerous code execution
- Potential XSS sink
- Hardcoded credential
- Possible secret
- Possible token
- Possible API key

### Output

Files Scanned: 8

Total Lines: 251

### Lesson Learned

Reviewers can accidentally review themselves.

Future versions should support exclusions and scope controls so Five Eyes can review external projects without generating findings from its own implementation files.

### Current Status

Eye One: Complete ✓

Eye Two: Complete ✓

Eye Three: Next

Eye Four: Planned

Eye Five: Planned
## v0.0.7 — Eye Three Scope Controls

Status: Complete

### Achievements

- Scope controls integrated into pipeline
- Reviewer self-scanning eliminated
- Internal framework files excluded
- Target-focused analysis established

### Evidence

Screenshot:

![Eye Three](screenshots/fiveeyetre.jpg)

Tag:

#eyethree

### Output

Files Scanned: 4

Total Lines: 144

Findings:

- Dangerous dynamic execution
- Potential XSS sink
- Hardcoded credential

### Lesson Learned

A reviewer must understand what not to review.

Effective analysis requires scope selection before analysis begins.
## v0.0.8 — Eye Four Risk Scoring

Status: Complete

### Achievements

- Risk scoring engine implemented
- Findings weighted by severity
- Risk level calculation added
- Executive-style output introduced

### Evidence

Screenshot:

![Eye Four](screenshots/fiveeyesfore.jpg)

Tag:

#eyefour

### Output

Files Scanned: 5

Total Lines: 177

Score: 17

Level: HIGH

### Lesson Learned

Raw findings are useful.

Risk scoring turns findings into prioritization.


## v0.1.0 — First Complete Pipeline

Status: Complete

### Eyes

- Eye One — Structure ✓
- Eye Two — Rules ✓
- Eye Three — Scope Controls ✓
- Eye Four — Risk Scoring ✓
- Eye Five — Reporting ✓

### Evidence

Screenshot:

![Eye Five](screenshots/fiveeyesfive.jpg)

Tag:

#eyefive

### Output

- Files Scanned: 6
- Total Lines: 230
- Risk Score: 17
- Risk Level: HIGH

### Reports Generated

- report.json
- report.md

### Milestone

First end-to-end Five Eyes pipeline completed.

