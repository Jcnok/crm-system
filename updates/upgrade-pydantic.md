Planned update: pydantic

Goal: Upgrade pydantic to the latest patch/minor version compatible with Python ^3.11.

Steps to complete (manual or CI):
1. Run: poetry update pydantic
2. Run tests: poetry run pytest
3. If tests pass, commit updated poetry.lock and open PR.

Notes:
- pydantic is declared with extras in pyproject.toml; ensure extras remain the same (email).
- If the update requires code changes due to validation changes, adjust the code and add tests.
