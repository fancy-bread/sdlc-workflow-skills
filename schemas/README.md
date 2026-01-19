# Command Structure Schemas

Formal JSON Schema definitions for Cursor command markdown files. Used to validate that commands follow the structure required by **AGENTS.md** §6 and to support deterministic, schema-enforced command contracts (ASDLC "Standardized Parts").

**Story:** FB-18 — Define command structure JSON schemas with Zod/JSON Schema.

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

- **Pattern:** `mcp_ServerName_ToolName` — e.g. `mcp_atlassian_getJiraIssue`, `mcp_github_list_branches`.
- **Rule:** When the document contains MCP references, each must match `mcp_[A-Za-z0-9-]+_[a-zA-Z0-9_]+`.
- **`mcps/` lookup:** `schemas/validate_mcps.py` can resolve `mcp_Server_Tool` to a file. Extending `schemas/validate.py` to check each `mcpRef` in a command exists in `mcps/` is future (see Future Work). For now, validation is pattern-only for mcpRefs in commands.

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

3. **Validate-all (commands + mcps)** — one entry point for both:

   ```bash
   python schemas/validate_all.py
   ```

   Runs (1) `validate.py` on every `commands/*.md` (excluding `commands/README.md`) and (2) `validate_mcps.py` on all `mcps/**/*.json`. Exit 0 only if **both** pass. Use before commit; FB-20 CI will run this.

---

## Files

| File | Purpose |
|------|---------|
| `schemas/command.schema.json` | JSON Schema for the `ParsedCommand` model (overview, definitions, prerequisites, steps, tools, guidance, optional mcpRefs). |
| `schemas/mcp-tool.schema.json` | JSON Schema for `mcps/<server>/tools/*.json` (FB-43). MCP-aligned: required `name`, `inputSchema`; optional `description`, `title`, `outputSchema`, `annotations`. |
| `schemas/validate.py` | Python script: parses `## ` sections, extracts step numbers and MCP refs, validates with `jsonschema` (Draft-07). |
| `schemas/validate_mcps.py` | Validates all `mcps/**/*.json`; `--list` / `--list --json` enumerates `mcps/` as the **list of record** (no MCP calls); resolve-one: `validate_mcps.py mcp_Server_Tool`. |
| `schemas/validate_all.py` | Orchestrates `validate.py` (all `commands/*.md` except README) and `validate_mcps.py`; exit 0 only if both pass. |

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

- **`mcps/` mcpRef lookup:** `schemas/validate_mcps.py` validates all `mcps/**/*.json` and can resolve `mcp_Server_Tool` to a file. Future: extend `schemas/validate.py` to check that each `mcpRef` in a command exists in `mcps/`.
- **FB-20:** CI integration — add a workflow step (e.g. GitHub Actions) that runs `python schemas/validate_all.py` (commands + mcps).
