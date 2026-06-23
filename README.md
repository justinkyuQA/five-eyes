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
