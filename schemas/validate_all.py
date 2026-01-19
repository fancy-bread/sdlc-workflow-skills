#!/usr/bin/env python3
"""
Run both command and mcps schema validation. Exit 0 only if both pass.

Usage: python schemas/validate_all.py

- Commands: runs schemas/validate.py on every commands/*.md (excludes commands/README.md).
- Mcps: runs schemas/validate_mcps.py (validates all mcps/**/*.json).

Use before commit; FB-20 CI will run this single entry point.
"""

import subprocess
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCHEMAS_DIR.parent
COMMANDS_DIR = REPO_ROOT / "commands"


def main() -> None:
    validate_py = SCHEMAS_DIR / "validate.py"
    validate_mcps_py = SCHEMAS_DIR / "validate_mcps.py"

    command_files = [
        p
        for p in sorted(COMMANDS_DIR.glob("*.md"))
        if p.name != "README.md"
    ]

    failures: list[tuple[Path, str]] = []
    for p in command_files:
        rel = p.relative_to(REPO_ROOT)
        r = subprocess.run(
            [sys.executable, str(validate_py), str(rel)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            failures.append((rel, r.stderr or "validation failed"))

    mcps_failed = False
    mcps_stderr = ""
    r = subprocess.run(
        [sys.executable, str(validate_mcps_py)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        mcps_failed = True
        mcps_stderr = r.stderr or ""

    if failures:
        print("Validation failed (commands):", file=sys.stderr)
        for rel, err in failures:
            snippet = (err.strip() or "(no stderr)").split("\n")[0]
            print(f"  {rel}: {snippet}", file=sys.stderr)
    if mcps_failed:
        print("Validation failed (mcps):", file=sys.stderr)
        print(mcps_stderr, file=sys.stderr)

    if failures or mcps_failed:
        sys.exit(1)

    n = len(command_files)
    print(f"OK: all commands ({n}) and mcps validate.")
    sys.exit(0)


if __name__ == "__main__":
    main()
