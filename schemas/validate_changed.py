#!/usr/bin/env python3
"""
Validate only changed skill and MCP files (for pre-commit hooks).

Usage: python schemas/validate_changed.py [file1] [file2] ...
       Or via pre-commit: automatically receives changed file paths

This script validates only the files passed as arguments, unlike validate_all.py
which validates all files. Used by pre-commit hooks to validate only changed files.
"""

import subprocess
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCHEMAS_DIR.parent
SKILLS_DIR = REPO_ROOT / "skills"
MCPS_DIR = REPO_ROOT / "mcps"

validate_py = SCHEMAS_DIR / "validate.py"
validate_mcps_py = SCHEMAS_DIR / "validate_mcps.py"


def main() -> None:
    if len(sys.argv) < 2:
        # No files provided - nothing to validate
        print("No files to validate")
        sys.exit(0)

    # Get file paths from command line arguments
    file_paths = [Path(arg) for arg in sys.argv[1:]]
    
    # Separate into skills and mcps
    skill_files = []
    mcp_files = []
    
    for file_path in file_paths:
        rel_path = file_path if file_path.is_absolute() else REPO_ROOT / file_path
        rel = rel_path.relative_to(REPO_ROOT)
        
        if str(rel).startswith("skills/") and rel.name == "SKILL.md":
            skill_files.append(rel)
        elif str(rel).startswith("mcps/") and rel.suffix == ".json":
            mcp_files.append(rel)

    failures: list[tuple[Path, str]] = []
    
    # Validate skill files
    for rel in skill_files:
        r = subprocess.run(
            [sys.executable, str(validate_py), str(rel)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            failures.append((rel, r.stderr or "validation failed"))

    # Validate MCP files (validate_mcps.py validates all mcps, but we can check if files exist)
    if mcp_files:
        # Run full MCP validation if any MCP files changed
        r = subprocess.run(
            [sys.executable, str(validate_mcps_py)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if r.returncode != 0:
            failures.append((Path("mcps"), r.stderr or "MCP validation failed"))

    if failures:
        print("Validation failed:", file=sys.stderr)
        for rel, err in failures:
            snippet = (err.strip() or "(no stderr)").split("\n")[0]
            print(f"  {rel}: {snippet}", file=sys.stderr)
        sys.exit(1)

    if skill_files or mcp_files:
        print(f"OK: validated {len(skill_files)} skill(s) and {len(mcp_files)} MCP file(s)")
    else:
        print("No files to validate")
    sys.exit(0)


if __name__ == "__main__":
    main()
