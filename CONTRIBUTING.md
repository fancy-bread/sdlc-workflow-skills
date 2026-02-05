# Contributing

## Creating a new spec

1. Copy `specs/TEMPLATE.md` to `specs/{feature-domain}/spec.md` (use kebab-case for the feature domain, e.g. `user-authentication`, `payment-processing`).
2. Replace all placeholders with your feature’s context, architecture, anti-patterns, definition of done, regression guardrails, and Gherkin scenarios.
3. See `specs/README.md` for **when to create** a spec, **when to update** it, and the **Same-Commit Rule**: if code changes behavior or contracts, update the spec in the same commit.

## Pre-commit hooks

Pre-commit hooks automatically validate changes before committing:

1. **Set up virtual environment and install dependencies:**
   ```bash
   ./start-mkdocs.sh setup
   ```
   This creates a virtual environment and installs all dependencies (including pre-commit).

   **Alternative (if virtual environment already exists):**
   ```bash
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Install hooks (from within virtual environment):**
   ```bash
   source venv/bin/activate  # Activate virtual environment first
   pre-commit install
   ```
   
   **Important:** Install pre-commit hooks from within the activated virtual environment. The hooks are configured to use the virtual environment's Python, so they'll have access to all dependencies (like `jsonschema`).

3. **Hooks run automatically** on `git commit`:
   - Schema validation for `skills/` and `mcps/` files
   - Link checking for markdown documentation files
   - Fast execution (<10 seconds) on changed files only

4. **Bypass hooks (if needed):**
   ```bash
   git commit --no-verify
   ```
   Note: CI/CD will still run full validation on pull requests.

## Schema validation

If you change files in `skills/` or `mcps/`, run before committing:

```bash
python scripts/verify_github_install.py   # Layout for Cursor GitHub install
python schemas/validate_all.py
```

CI runs both on pull requests; passing locally avoids validation failures.

**Note:** Pre-commit hooks automatically run schema validation on changed files. You can still run `validate_all.py` manually to validate all files.

## Pull requests

- Link PRs to the relevant Jira or GitHub issue.
- When behavior or contracts change, **update the spec in the same commit** as the code (see `specs/README.md`).
- Ensure `python schemas/validate_all.py` passes when `skills/` or `mcps/` are modified.
