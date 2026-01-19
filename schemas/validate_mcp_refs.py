#!/usr/bin/env python3
"""
Validate MCP tool refs in command files against mcps/ (list of record).

Extracts mcp_<server>_<tool> from commands/*.md and docs/commands/*.md,
validates against get_valid_refs() from validate_mcps, reports invalid refs
with fuzzy suggestions. Exit 1 if any invalid.

Usage: python schemas/validate_mcp_refs.py

Use before commit; validate_all.py runs this after validate_mcps.
"""

import difflib
import re
import sys
from pathlib import Path

SCHEMAS_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCHEMAS_DIR.parent
COMMANDS_DIR = REPO_ROOT / "commands"
DOCS_COMMANDS_DIR = REPO_ROOT / "docs" / "commands"

# Allow importing validate_mcps when run as script
if str(SCHEMAS_DIR) not in sys.path:
    sys.path.insert(0, str(SCHEMAS_DIR))

from validate_mcps import get_valid_refs

# Match mcp_<server>_<tool>; server/tool can have alphanumeric, -, _
MCP_REF_RE = re.compile(r"mcp_([a-zA-Z0-9-]+)_([a-zA-Z0-9_]+)")


def _line_no(text: str, pos: int) -> int:
    return text[:pos].count("\n") + 1


def _scan_file(path: Path, valid: set[str]) -> list[tuple[Path, int, str]]:
    text = path.read_text(encoding="utf-8")
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
    files: list[Path] = []
    for p in sorted(COMMANDS_DIR.glob("*.md")):
        if p.name != "README.md":
            files.append(p)
    if DOCS_COMMANDS_DIR.exists():
        files.extend(sorted(DOCS_COMMANDS_DIR.glob("*.md")))

    all_invalid: list[tuple[Path, int, str]] = []
    for p in files:
        all_invalid.extend(_scan_file(p, valid))

    if not all_invalid:
        print("OK: all MCP tool refs in commands validate.")
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
