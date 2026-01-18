# Command Structure Schemas

Formal JSON Schema definitions for Cursor command markdown files. Used to validate that commands follow the structure required by **AGENTS.md** §6 and to support deterministic, schema-enforced command contracts (ASDLC "Standardized Parts").

**Story:** [FB-18](https://fancybread.atlassian.net/browse/FB-18) — Define command structure JSON schemas with Zod/JSON Schema.

---

## Required Sections

Per AGENTS.md §6 Command Structure Standards, every command must include:

| Section | Purpose |
|---------|---------|
| **Overview** | Brief description of the command goal |
| **Definitions** | Domain terms and variables (e.g. `{TASK_KEY}`, `{FEATURE_DOMAIN}`) |
| **Prerequisites** | Validation checks before execution (e.g. MCP status, story exists) |
| **Steps** | Ordered execution with numbered steps (`1.`, `2.`, …) and MCP/tool calls |
| **Tools** | MCP and other tool documentation (name, parameters, error handling) |
| **Guidance** | Role, Instruction, Context, Examples, Constraints, Output |

The schema validates a *parsed* representation of the markdown: section presence, non-empty content, and at least one numbered step in **Steps**.

---

## MCP Tool References

- **Pattern:** `mcp_ServerName_ToolName` — e.g. `mcp_Atlassian-MCP-Server_getJiraIssue`, `mcp_github_list_branches`.
- **Rule:** When the document contains MCP references, each must match `mcp_[A-Za-z0-9-]+_[a-zA-Z0-9_]+`.
- **`mcps/` lookup:** Not yet implemented. Validation is pattern-only. When an `mcps/` directory exists, future tooling may validate that referenced tools exist in `mcps/<server>/tools/`.

---

## Step Structure

- **Steps** must contain at least one match for `\d+\.` (e.g. `1.`, `2.`).
- Descriptions and tool-call phrasing are not further constrained; the schema checks structure, not prose.

---

## How to Validate

1. **Install dependencies** (once). Use the project venv or any Python env with `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Or, with the project venv: `source venv/bin/activate` (or `. venv/bin/activate`) then `pip install -r requirements.txt`.

2. **Run the validator** on a command file:

   ```bash
   python schemas/validate.py commands/create-plan.md
   ```

   On success: `OK: commands/create-plan.md validates against command.schema.json`.
   On failure: JSON Schema errors are printed and the process exits with code 1.

---

## Files

| File | Purpose |
|------|---------|
| `schemas/command.schema.json` | JSON Schema for the `ParsedCommand` model (overview, definitions, prerequisites, steps, tools, guidance, optional mcpRefs). |
| `schemas/validate.py` | Python script: parses `## ` sections, extracts step numbers and MCP refs, validates with `jsonschema` (Draft-07). |

The `jsonschema` library is in `requirements.txt`; the validator runs in the same Python environment as MkDocs.

---

## Valid and Invalid Examples

- **Valid:** `commands/create-plan.md` — has all six sections, numbered steps, and MCP refs matching the pattern.
- **Invalid (would fail):**
  - Missing section (e.g. no `## Prerequisites`).
  - **Steps** with no `1.`, `2.`, etc.
  - MCP-like token that doesn’t match the pattern (e.g. `getJiraIssue` without the `mcp_Server_` prefix, or malformed `mcp_Invalid`).

Commands such as `mcp-status.md` or `start-task.md` may not yet have all six sections; they will fail until updated to match the refined structure. The schema targets the **refined** command set from Phase 1 (FB-24, FB-37–41).

---

## Future Work

- **`mcps/` validation:** When `mcps/<server>/tools/` exists, the validator could optionally check that each `mcpRef` has a corresponding tool definition.
- **FB-19 / FB-20:** Full `validate-all` CLI and CI integration (e.g. validate every `commands/*.md` in CI) are out of scope for FB-18.
