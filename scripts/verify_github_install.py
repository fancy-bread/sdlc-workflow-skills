#!/usr/bin/env python3
"""
Verify this repo is ready for Agent Skills–compatible install (Cursor GitHub, Claude, Codex).

The same layout works for Cursor (Remote Rule / Github), Claude, and Codex:
- A top-level skills/ directory.
- Each skill is a subdirectory of skills/ containing SKILL.md.
- SKILL.md has YAML frontmatter with:
  - name (required): lowercase letters, numbers, hyphens only; must match parent folder name.
  - description (required).

See: https://cursor.com/docs/context/skills#installing-skills-from-github
     https://agentskills.io

Usage: python scripts/verify_github_install.py
Exit: 0 if OK, 1 if layout/frontmatter invalid.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# Cursor: "Lowercase letters, numbers, and hyphens only"
NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9-]*[a-z0-9]$|^[a-z0-9]$")


def _parse_frontmatter(text: str) -> tuple[str, dict]:
    """Return (body_after_frontmatter, frontmatter_dict). Frontmatter must be first."""
    text = text.strip()
    if not text.startswith("---"):
        return text, {}
    parts = text.split("---", 2)
    if len(parts) < 3:
        return text, {}
    fm = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip().lower()] = value.strip()
    return parts[2].lstrip("\n"), fm


def main() -> int:
    errors: list[str] = []

    if not SKILLS_DIR.is_dir():
        errors.append(f"Missing top-level directory: skills/")
        for e in errors:
            print(e, file=sys.stderr)
        return 1

    # Only consider skill subdirectories (each must contain SKILL.md)
    skill_dirs = sorted(d for d in SKILLS_DIR.iterdir() if d.is_dir())
    if not skill_dirs:
        errors.append("skills/ has no subdirectories (no skills found)")

    for skill_dir in skill_dirs:
        name_dir = skill_dir.name
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.is_file():
            errors.append(f"skills/{name_dir}/: missing SKILL.md")
            continue
        raw = skill_md.read_text(encoding="utf-8")
        _, fm = _parse_frontmatter(raw)
        name_fm = fm.get("name")
        desc = fm.get("description")
        if not name_fm:
            errors.append(f"skills/{name_dir}/SKILL.md: frontmatter missing 'name'")
        elif not isinstance(name_fm, str):
            errors.append(f"skills/{name_dir}/SKILL.md: frontmatter 'name' must be a string")
        elif name_fm != name_dir:
            errors.append(f"skills/{name_dir}/SKILL.md: frontmatter name '{name_fm}' must match folder name '{name_dir}'")
        elif not NAME_PATTERN.match(name_fm):
            errors.append(f"skills/{name_dir}/SKILL.md: name must be lowercase letters, numbers, hyphens only")
        if desc is None:
            errors.append(f"skills/{name_dir}/SKILL.md: frontmatter missing 'description'")
        elif not isinstance(desc, str) or not desc.strip():
            errors.append(f"skills/{name_dir}/SKILL.md: frontmatter 'description' must be a non-empty string")

    if errors:
        print("GitHub install verification failed:", file=sys.stderr)
        for e in errors:
            print(f"  {e}", file=sys.stderr)
        return 1
    print(f"OK: repo ready for Cursor/Claude/Codex ({len(skill_dirs)} skills).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
