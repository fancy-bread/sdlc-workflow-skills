# Feature: /mcp-status (MCP Server Status Check)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-19

---

## Blueprint

### Context

MCP servers (Atlassian, GitHub, ASDLC, ADO, etc.) can disconnect or lose authentication after inactivity. Commands like `/start-task`, `/create-task`, and `/complete-task` depend on those integrations. `/mcp-status` verifies connectivity **before** running such commands so users get immediate, actionable feedback instead of cryptic MCP or auth errors.

**Source of configured servers**: The canonical source for which MCP servers are configured is the user's MCP configuration: the `mcpServers` section in `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows), or equivalent via Cursor Settings → Features → Model Context Protocol. The command discovers servers from this configuration (not from project-specific directories or scripts) so it works in any project.

### Architecture

- **Skill location**: `skills/mcp-status/SKILL.md`. Executed as `/mcp-status` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Server discovery**: Read the MCP configuration file and extract `mcpServers` keys. If the config file is not accessible, try common server names (e.g. `github`, `atlassian`, `ado`, `asdlc`, including `user-`-prefixed variants) as fallback.
- **Flow**: (1) Discover configured servers from MCP config; (2) for each server, call one lightweight read-only MCP tool (e.g. `getAccessibleAtlassianResources`, `list_commits` / `list_branches`, `list_articles`, `core_list_projects`, or common `list_*` / `get_*` patterns); (3) report connected / disconnected; for disconnected, provide reconnection steps (Cursor Settings → Features → Model Context Protocol).
- **Dependencies**: MCP configuration (`mcp.json` or Cursor UI), MCP servers configured in Cursor. **Outbound**: commands that require MCP (e.g. `/start-task`) should direct users to run `/mcp-status` when MCP is in doubt.

### Anti-Patterns

- **Don’t assume MCP is OK without checking** — Discover configured servers and test each one; do not trust a cached or assumed state.
- **Don't rely on project-specific server lists** — Use the user's MCP configuration (`mcp.json`), not project-specific `mcps/` or `validate_mcps.py`, so the command works generically across projects.
- **Don’t modify data** — The command is read-only; only call read-only MCP tools. No creates, updates, or deletes.

---

## Contract

### Definition of Done

- [ ] Skill exists at `skills/mcp-status/SKILL.md` and body conforms to the command schema.
- [ ] Command discovers configured servers from the MCP configuration file (`mcp.json`) or, if inaccessible, tries common server names as fallback.
- [ ] For each discovered server, the command calls one lightweight read-only MCP tool (per patterns in the command) and records success or failure.
- [ ] Output clearly reports each server as connected or disconnected; for disconnected, includes reconnection steps (e.g. Cursor Settings → Features → Model Context Protocol).
- [ ] `python schemas/validate_all.py` passes (command file validates against `schemas/command.schema.json`).

### Regression Guardrails

- **Server discovery** — Servers are discovered from the user's MCP configuration (`mcp.json`), not from project-specific `mcps/` or `validate_mcps.py`. The command must remain generic across projects.
- **Read-only** — The command must only perform read-only operations; no MCP or filesystem writes.
- **Reconnection guidance** — When a server test fails, the command must distinguish auth errors (reconnect) from other errors and provide specific guidance.

### Scenarios

**Scenario: All configured MCP servers are connected**
- **Given**: MCP config includes `atlassian`, `github`, and `asdlc`; each of those MCP servers is configured in Cursor and authenticated
- **When**: The user runs `/mcp-status`
- **Then**: The command reports each of atlassian, github, and asdlc as connected (e.g. “✅ atlassian - Connected”) and a summary such as “All systems operational!”

**Scenario: One MCP server is disconnected and needs reconnection**
- **Given**: MCP config includes `atlassian`; the Atlassian MCP server in Cursor has lost authentication
- **When**: The user runs `/mcp-status`
- **Then**: The command reports atlassian as disconnected (e.g. “❌ atlassian - Needs authentication”) and includes reconnection steps (Cursor Settings → Features → Model Context Protocol)
