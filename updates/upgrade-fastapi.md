Planned update: fastapi

Goal: Upgrade FastAPI to the latest patch/minor version compatible with Python ^3.11.

Steps to complete (manual or CI):
1. Run: poetry update fastapi
2. Run tests: poetry run pytest
3. If tests pass, commit updated poetry.lock and open PR (or let Dependabot handle actual version bump). 

Notes:
- Dependabot is enabled and will also open PRs for automated upgrades. This branch records the manual plan for FastAPI.
