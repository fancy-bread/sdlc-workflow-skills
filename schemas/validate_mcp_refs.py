#!/usr/bin/env python3
"""
Validate MCP tool refs in skill and doc files against mcps/ (list of record).

Extracts mcp_<server>_<tool> from skills/*/SKILL.md (body only) and docs/skills/*.md;
validates against get_valid_refs() from validate_mcps,
reports invalid refs with fuzzy suggestions. Exit 1 if any invalid.

Usage: python schemas/validate_mcp_refs.py

Use before commit; validate_all.py runs this after validate_mcps.
"""

import difflib
import re
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCHEMAS_DIR.parent
SKILLS_DIR = REPO_ROOT / "skills"
DOCS_SKILLS_DIR = REPO_ROOT / "docs" / "skills"


def _strip_frontmatter(text: str) -> str:
    """If content has YAML frontmatter (--- ... ---), return body only."""
    if not text.strip().startswith("---"):
        return text
    parts = text.split("---", 2)
    return parts[2].lstrip("\n") if len(parts) >= 3 else text

# Allow importing validate_mcps when run as script
if str(SCHEMAS_DIR) not in sys.path:
    sys.path.insert(0, str(SCHEMAS_DIR))

from validate_mcps import get_valid_refs

# Match mcp_<server>_<tool>; server/tool can have alphanumeric, -, _
MCP_REF_RE = re.compile(r"mcp_([a-zA-Z0-9-]+)_([a-zA-Z0-9_]+)")


def _line_no(text: str, pos: int) -> int:
    return text[:pos].count("\n") + 1


def _scan_file(path: Path, valid: set[str], strip_fm: bool = False) -> list[tuple[Path, int, str]]:
    text = path.read_text(encoding="utf-8")
    if strip_fm:
        text = _strip_frontmatter(text)
    invalid: list[tuple[Path, int, str]] = []
    seen: set[str] = set()
    for m in MCP_REF_RE.finditer(text):
        ref = m.group(0)
        if ref in seen or ref in valid:
            continue
        seen.add(ref)
        line = _line_no(text, m.start())
        invalid.append((path, line, ref))
    return invalid


def main() -> None:
    valid = get_valid_refs()
    files: list[tuple[Path, bool]] = []  # (path, strip_frontmatter)
    if SKILLS_DIR.exists():
        for p in sorted(SKILLS_DIR.glob("*/SKILL.md")):
            files.append((p, True))
    if DOCS_SKILLS_DIR.exists():
        for p in sorted(DOCS_SKILLS_DIR.glob("*.md")):
            files.append((p, False))

    all_invalid: list[tuple[Path, int, str]] = []
    for p, strip_fm in files:
        all_invalid.extend(_scan_file(p, valid, strip_fm=strip_fm))

    if not all_invalid:
        print("OK: all MCP tool refs in skills/docs validate.")
        sys.exit(0)

    valid_list = sorted(valid)
    print("Invalid MCP tool ref(s):", file=sys.stderr)
    for path, line, ref in all_invalid:
        rel = path.relative_to(REPO_ROOT)
        suggestions = difflib.get_close_matches(ref, valid_list, n=3, cutoff=0.6)
        suffix = f" [Did you mean: {', '.join(suggestions)}?]" if suggestions else ""
        print(f"  {rel}:{line}: {ref}{suffix}", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
