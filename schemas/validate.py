#!/usr/bin/env python3
"""
Validates a Cursor command markdown file against schemas/command.schema.json.

Usage: python schemas/validate.py <path-to-command.md>
Example: python schemas/validate.py commands/create-plan.md

Parses ## Overview, ## Definitions, ## Prerequisites, ## Steps, ## Tools, ## Guidance,
extracts step numbers from Steps, and MCP refs (mcp_Server_ToolName) from the full doc.
"""

import json
import re
import sys
from pathlib import Path

from jsonschema import Draft7Validator

SECTION_NAMES = ["Overview", "Definitions", "Prerequisites", "Steps", "Tools", "Guidance"]
MCP_REF_PATTERN = re.compile(r"mcp_[A-Za-z0-9-]+_[a-zA-Z0-9_]+")


def parse_command_md(md: str) -> dict:
    chunks = re.split(r"\r?\n## ", md)
    found = {}

    for i in range(1, len(chunks)):
        part = chunks[i]
        idx = part.find("\n")
        name = (part[:idx] if idx >= 0 else part).strip()
        body = part[idx + 1 :].strip() if idx >= 0 else ""
        if name in SECTION_NAMES:
            found[name] = body

    steps_content = found.get("Steps", "")
    steps_numbers = [int(m.group(1)) for m in re.finditer(r"(\d+)\.", steps_content)]

    mcp_refs = list(dict.fromkeys(MCP_REF_PATTERN.findall(md)))

    parsed = {
        "overview": found.get("Overview", ""),
        "definitions": found.get("Definitions", ""),
        "prerequisites": found.get("Prerequisites", ""),
        "steps": {"content": steps_content, "numbers": steps_numbers},
        "tools": found.get("Tools", ""),
        "guidance": found.get("Guidance", ""),
    }
    if mcp_refs:
        parsed["mcpRefs"] = mcp_refs

    return parsed


def main() -> None:
    md_path = sys.argv[1] if len(sys.argv) > 1 else "commands/create-plan.md"
    schema_path = Path(__file__).parent / "command.schema.json"

    if not Path(md_path).exists():
        print(f"File not found: {md_path}", file=sys.stderr)
        sys.exit(1)

    md = Path(md_path).read_text(encoding="utf-8")
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    parsed = parse_command_md(md)

    validator = Draft7Validator(schema)
    errors = list(validator.iter_errors(parsed))

    if errors:
        print(f"Validation failed for {md_path}:", file=sys.stderr)
        for e in errors:
            print(f"  {e.json_path}: {e.message}", file=sys.stderr)
        sys.exit(1)

    print(f"OK: {md_path} validates against command.schema.json")
    sys.exit(0)


if __name__ == "__main__":
    main()
