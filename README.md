# Five Eyes

Five Eyes is a local-first code review pipeline.

It uses five simple review stages:

1. Structure
2. Rules
3. Patterns
4. Scoring
5. Reporting

The goal is to turn source files into structured findings before any large model or human reviewer needs to inspect them.

## Run

```bash
python3 scanner.py test_project


Development Timeline

v0.0.1 — Architecture Foundation

- Repository established
- Project philosophy documented
- Architecture documented
- Roadmap documented
- Initial release notes created

v0.0.2 — Eye One Prototype

- File discovery implemented
- Line counting implemented
- Extension classification implemented
- First executable scanner released

v0.0.3 — Rule Detection Prototype

- Basic rule engine implemented
- Detection patterns added:
  - eval(
  - exec(
  - innerHTML
  - password
  - secret
  - token
  - api_key
- First security findings generated

v0.0.4 — Eye One Modular Architecture

Status: Complete

Achievements

- Reviewer architecture established
- Eye One extracted into independent module
- Scanner converted into orchestration layer
- Foundation established for Eyes Two through Five

Evidence

Screenshot:
screenshots/fiveeyesone.jpg

Tag:
#eyeone

Output

Files Scanned: 6

Total Lines: 154

Lesson Learned

Stable reviewers should be added, not repeatedly rewritten.

New capabilities should arrive as new Eyes rather than by continuously modifying existing Eyes.

Current Status

Eye One: Complete ✓

Eye Two: Next

