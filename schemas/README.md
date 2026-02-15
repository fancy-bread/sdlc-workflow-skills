# Skill Structure Schemas

Formal JSON Schema definitions for Agent Skills markdown (e.g. used by Cursor and compatible environments). Used to validate that skills (body of `skills/*/SKILL.md`) follow the structure required by **AGENTS.md** §6 and to support deterministic, schema-enforced contracts (ASDLC "Standardized Parts").

**Story:** FB-18 — Define skill structure JSON schemas with Zod/JSON Schema.

---

## Required Sections

Per AGENTS.md §6 Skill Structure Standards, every skill (body) must include:

| Section | Purpose |
|---------|---------|
| **Overview** | Brief description of the skill goal |
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
- **`mcps/` lookup:** `schemas/validate_mcps.py` can resolve `mcp_Server_Tool` to a file. Extending `schemas/validate.py` to check each `mcpRef` in a skill exists in `mcps/` is future (see Future Work). For now, validation is pattern-only for mcpRefs in skills.

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

2. **Run the validator** on a skill file (e.g. skills/<name>/SKILL.md):

   ```bash
   python schemas/validate.py skills/create-plan/SKILL.md
   ```

   On success: `OK: skills/create-plan/SKILL.md validates against skill.schema.json`.
   On failure: JSON Schema errors are printed and the process exits with code 1.
   For `skills/*/SKILL.md`, frontmatter is stripped and the body is validated.

3. **Validate-all (skills + mcps + mcp refs)** — one entry point:

   ```bash
   python schemas/validate_all.py
   ```

   Runs (1) `validate.py` on every `skills/*/SKILL.md`, (2) `validate_mcps.py` on all `mcps/**/*.json`, and (3) `validate_mcp_refs.py` to check that every `mcp_<server>_<tool>` in skills and docs exists in `mcps/`. Exit 0 only if **all** pass. Use before commit; CI runs this.

---

## Files

| File | Purpose |
|------|---------|
| `schemas/skill.schema.json` | JSON Schema for the `ParsedSkill` model (overview, definitions, prerequisites, steps, tools, guidance, optional mcpRefs). |
| `schemas/mcp-tool.schema.json` | JSON Schema for `mcps/<server>/tools/*.json` (FB-43). MCP-aligned: required `name`, `inputSchema`; optional `description`, `title`, `outputSchema`, `annotations`. |
| `schemas/validate.py` | Python script: parses `## ` sections, extracts step numbers and MCP refs, validates with `jsonschema` (Draft-07). Supports `skills/*/SKILL.md` (strips frontmatter). |
| `schemas/validate_mcps.py` | Validates all `mcps/**/*.json`; `get_valid_refs()` returns the set of `mcp_<server>_<tool>`; `--list` / `--list --json` enumerates `mcps/`; resolve-one: `validate_mcps.py mcp_Server_Tool`. |
| `schemas/validate_mcp_refs.py` | Validates that every `mcp_<server>_<tool>` in `skills/*/SKILL.md` (body) and `docs/skills/` exists in `mcps/`; reports invalid refs with fuzzy suggestions. |
| `schemas/validate_all.py` | Orchestrates `validate.py` (on all `skills/*/SKILL.md`), `validate_mcps.py`, and `validate_mcp_refs.py`; exit 0 only if all pass. |

The `jsonschema` library is in `requirements.txt`; the validator runs in the same Python environment as MkDocs.

---

## Valid and Invalid Examples

- **Valid:** `skills/create-plan/SKILL.md` (body) — has all six sections, numbered steps, and MCP refs matching the pattern.
- **Invalid (would fail):**
  - Missing section (e.g. no `## Prerequisites`).
  - **Steps** with no `1.`, `2.`, etc.
  - MCP-like token that doesn’t match the pattern (e.g. `getJiraIssue` without the `mcp_Server_` prefix, or malformed `mcp_Invalid`).

Skills in `skills/` are the canonical source; the schema validates the body of each `SKILL.md` (frontmatter is stripped before validation).

---

## Future Work

- **FB-20:** CI integration — `skill-validation.yml` runs `python schemas/validate_all.py` (skills + mcps + mcp refs) and lychee. **FB-21:** `validate_mcp_refs.py` checks that each `mcpRef` in skills exists in `mcps/` (implemented).
