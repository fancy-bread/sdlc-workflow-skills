# Feature: mcps/ (MCP Tool Schema Directory)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)
> **Status**: Active
> **Last Updated**: 2026-01-18

---

## Blueprint

### Context

Commands reference MCP tools (e.g. `mcp_atlassian_getJiraIssue`, `mcp_github_list_commits`). Pattern-only validation catches malformed refs but not **typos, wrong names, or deprecated tools**. We need a **source of truth**—`mcps/<server>/tools/*.json`—so validators can confirm each `mcp_Server_ToolName` in a command corresponds to a real tool in our configured MCP set. This ensures **commands invoke the correct MCP tool**.

**Problem:** AGENTS.md and validators referred to `mcps/<server>/tools/` as the place to read tool schemas, but the directory did not exist.

**Solution:** `mcps/` at repo root with `mcps/<server>/tools/<tool>.json` per MCP tool. Each file conforms to `schemas/mcp-tool.schema.json` (MCP-aligned: `name`, `inputSchema` required). Validators and FB-20/FB-21 use it to resolve `mcp_Server_ToolName` and validate that the tool exists.

### Architecture

- **Layout:** `mcps/<server>/tools/<tool>.json`
  - `<server>`: MCP server id as in the `mcp_` prefix (e.g. `atlassian`, `github`, `asdlc`, `ado`). Align with Cursor MCP config and `mcp_Server_Tool` tokens in commands. **MCP combinations:** GitHub+Jira or GitHub+ADO (issue tracker); ASDLC optional.
  - `<tool>`: Tool name segment (e.g. `getJiraIssue`, `list_commits`). Filename `getJiraIssue.json`; `name` inside JSON may be the tool id or the full `mcp_Server_Tool` depending on resolver needs.
- **Schema:** Each `mcps/<server>/tools/*.json` must validate against `schemas/mcp-tool.schema.json` (required: `name`, `inputSchema`; optional: `description`, `title`, `outputSchema`, `annotations`).
- **Resolve rule:** `mcp_Server_Tool` → `mcps/Server/tools/Tool.json`. Resolver normalizes the ref, finds the file, and (optionally) validates the file against `mcp-tool.schema.json`.
- **Dependencies:**
  - **Inbound:** `schemas/mcp-tool.schema.json`, AGENTS.md (directory_map, MCP rules), MCP server tool definitions (for exporting or hand-authoring).
  - **Outbound:** FB-20 (CI: validate MCP refs against mcps/), FB-21 (markdown/MCP validator), `schemas/validate.py` or future extensions (mcpRefs lookup).

### Anti-Patterns

- **Don’t put tool files outside `mcps/<server>/tools/`** — the layout is the contract for resolvers.
- **Don’t use a tool file that fails `mcp-tool.schema.json`** — validators and CI must be able to assume conformance.
- **Don’t hardcode server or tool names in validators** — derive from `mcp_Server_Tool` and path conventions.
- **Don’t skip `mcps/README.md`** — it documents the layout, the schema, and how to add or update tools.
- **Don’t add a tool to `mcps/` unless it is referenced in `skills/*/SKILL.md` or `skills/mcp-status/SKILL.md`** — we curate for tool limits. With multiple MCP servers, developers can hit IDE caps; only tools used by skills or mcp-status belong in the list of record.

---

## Contract

### Definition of Done

- [ ] `mcps/` exists with `mcps/<server>/tools/` for each MCP server we validate (Atlassian, GitHub, ASDLC, ADO as a minimum).
- [ ] Every `mcps/<server>/tools/*.json` validates against `schemas/mcp-tool.schema.json`.
- [ ] `mcps/README.md` documents layout, `schemas/mcp-tool.schema.json`, how to add/update tool files, and how validators use mcps/.
- [ ] At least one script or validator can resolve `mcp_Server_ToolName` to a file in `mcps/<server>/tools/` and verify that file against `mcp-tool.schema.json`.
- [ ] `schemas/mcp-tool.schema.json` exists and is used as the conformance target for mcps/ tool files.

### Regression Guardrails

- **Resolve consistency** — `mcp_Server_Tool` must map deterministically to `mcps/Server/tools/Tool.json` (or equivalent once convention is fixed).
- **Schema conformance** — Any new or edited `mcps/**/*.json` must pass validation against `schemas/mcp-tool.schema.json`.
- **AGENTS.md alignment** — `directory_map` and MCP rules that reference `mcps/` must stay consistent with the layout and schema.

### Scenarios

**Scenario: Resolve MCP ref to tool file**
- **Given:** `mcp_atlassian_getJiraIssue` and `mcps/atlassian/tools/getJiraIssue.json` exists
- **When:** Resolver parses the ref and looks up `mcps/atlassian/tools/getJiraIssue.json`
- **Then:** File is found and validates against `schemas/mcp-tool.schema.json`

**Scenario: Validator rejects unknown MCP ref**
- **Given:** A command contains `mcp_atlassian_getJiraIssue` and `mcps/atlassian/tools/getJiraIssue.json` does not exist
- **When:** Validator resolves `mcp_Server_Tool` to `mcps/…/tools/…`
- **Then:** Resolver reports missing tool file (and optionally suggests nearest match)

**Scenario: New tool file must conform to schema**
- **Given:** A contributor adds `mcps/github/tools/new_tool.json`
- **When:** Validation runs (local script or CI)
- **Then:** The file must pass `schemas/mcp-tool.schema.json` (required `name`, `inputSchema`) or validation fails
