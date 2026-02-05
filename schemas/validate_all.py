#!/usr/bin/env python3
"""
Run skill, mcps, and MCP ref validation. Exit 0 only if all pass.

Usage: python schemas/validate_all.py

- Skills: runs schemas/validate.py on every skills/*/SKILL.md.
- Mcps: runs schemas/validate_mcps.py (validates all mcps/**/*.json).
- MCP refs: runs schemas/validate_mcp_refs.py (validates mcp_<server>_<tool> in skills and docs against mcps/).

Use before commit; CI will run this single entry point.
"""

import subprocess
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCHEMAS_DIR.parent
SKILLS_DIR = REPO_ROOT / "skills"


def main() -> None:
    validate_py = SCHEMAS_DIR / "validate.py"
    validate_mcps_py = SCHEMAS_DIR / "validate_mcps.py"

    skill_files = sorted(SKILLS_DIR.glob("*/SKILL.md"))

    failures: list[tuple[Path, str]] = []
    for p in skill_files:
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

    validate_mcp_refs_py = SCHEMAS_DIR / "validate_mcp_refs.py"
    mcp_refs_failed = False
    mcp_refs_stderr = ""
    r = subprocess.run(
        [sys.executable, str(validate_mcp_refs_py)],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if r.returncode != 0:
        mcp_refs_failed = True
        mcp_refs_stderr = r.stderr or ""

    if failures:
        print("Validation failed (skills):", file=sys.stderr)
        for rel, err in failures:
            snippet = (err.strip() or "(no stderr)").split("\n")[0]
            print(f"  {rel}: {snippet}", file=sys.stderr)
    if mcps_failed:
        print("Validation failed (mcps):", file=sys.stderr)
        print(mcps_stderr, file=sys.stderr)
    if mcp_refs_failed:
        print("Validation failed (mcp refs):", file=sys.stderr)
        print(mcp_refs_stderr, file=sys.stderr)

    if failures or mcps_failed or mcp_refs_failed:
        sys.exit(1)

    n = len(skill_files)
    print(f"OK: all skills ({n}), mcps, and mcp refs validate.")
    sys.exit(0)


if __name__ == "__main__":
    main()
