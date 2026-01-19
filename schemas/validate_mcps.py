#!/usr/bin/env python3
"""
Validate mcps/<server>/tools/*.json against schemas/mcp-tool.schema.json.

mcps/ is the list of record: the set of MCP tools we support. Use --list to enumerate.

Usage:
  python schemas/validate_mcps.py
    → Validate all mcps/**/*.json; exit 0 only if all pass.

  python schemas/validate_mcps.py --list [--json]
    → List all tools from mcps/ (list of record). Default: TSV (server, tool, ref, path). --json: JSON array.

  python schemas/validate_mcps.py mcp_Server_Tool
    → Resolve ref to mcps/Server/tools/Tool.json, validate that file, print path or error.
"""

import json
import sys
from pathlib import Path

from jsonschema import Draft7Validator

# Known MCP server ids
KNOWN_SERVERS = ["atlassian", "github", "asdlc", "ado"]

REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = REPO_ROOT / "schemas" / "mcp-tool.schema.json"
MCPS_ROOT = REPO_ROOT / "mcps"


def load_schema():
    return json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))


def list_tools() -> list[dict]:
    """Enumerate mcps/**/*.json. Returns list of {server, tool, ref, path} (path relative to repo root)."""
    out = []
    for p in sorted(MCPS_ROOT.rglob("*.json")):
        rel = p.relative_to(REPO_ROOT)
        parts = rel.parts  # e.g. ("mcps", "github", "tools", "list_commits.json")
        if len(parts) >= 4 and parts[2] == "tools":
            server = parts[1]
            tool = p.stem
            try:
                data = json.loads(p.read_text(encoding="utf-8"))
                tool = data.get("name", tool)
            except Exception:
                pass
            ref = f"mcp_{server}_{tool}"
            out.append({"server": server, "tool": tool, "ref": ref, "path": str(rel)})
    return out


def get_valid_refs() -> set[str]:
    """Return the set of valid MCP tool refs (mcp_<server>_<tool>) from mcps/."""
    return {t["ref"] for t in list_tools()}


def resolve(ref: str) -> Path | None:
    """Resolve mcp_Server_Tool to mcps/Server/tools/Tool.json. Returns Path or None if not found."""
    if not ref.startswith("mcp_"):
        return None
    rest = ref[4:]  # after "mcp_"
    for server in KNOWN_SERVERS:
        prefix = server + "_"
        if rest.startswith(prefix):
            tool = rest[len(prefix) :]
            if not tool:
                return None
            p = MCPS_ROOT / server / "tools" / f"{tool}.json"
            return p if p.exists() else None
    return None


def validate_file(path: Path, validator: Draft7Validator) -> list[str]:
    errs = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        for e in validator.iter_errors(data):
            errs.append(f"{path}: {e.json_path} {e.message}")
    except Exception as ex:
        errs.append(f"{path}: {ex}")
    return errs


def main() -> None:
    # --list: enumerate mcps/ (list of record)
    if len(sys.argv) >= 2 and sys.argv[1] in ("--list", "-l"):
        as_json = "--json" in sys.argv
        tools = list_tools()
        if as_json:
            print(json.dumps(tools, indent=2))
        else:
            print("server\ttool\tref\tpath")
            for t in tools:
                print(f"{t['server']}\t{t['tool']}\t{t['ref']}\t{t['path']}")
        sys.exit(0)

    schema = load_schema()
    Draft7Validator.check_schema(schema)
    validator = Draft7Validator(schema)

    if len(sys.argv) > 1:
        # Resolve-one mode
        ref = sys.argv[1]
        p = resolve(ref)
        if p is None:
            print(f"Resolver: no file found for {ref}", file=sys.stderr)
            sys.exit(1)
        errs = validate_file(p, validator)
        if errs:
            for e in errs:
                print(e, file=sys.stderr)
            sys.exit(1)
        print(p)
        sys.exit(0)

    # Validate-all mode
    all_errs = []
    for j in sorted(MCPS_ROOT.rglob("*.json")):
        all_errs.extend(validate_file(j, validator))

    if all_errs:
        print("Validation failed:", file=sys.stderr)
        for e in all_errs:
            print(f"  {e}", file=sys.stderr)
        sys.exit(1)

    n = len(list(MCPS_ROOT.rglob("*.json")))
    print(f"OK: all {n} mcps/**/*.json validate against mcp-tool.schema.json")
    sys.exit(0)


if __name__ == "__main__":
    main()
