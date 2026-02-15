# Feature: /mcp-status (MCP Server Status Check)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-02-14

---

## Blueprint

### Context

MCP servers (Atlassian, GitHub, ASDLC, ADO, etc.) can disconnect or lose authentication after inactivity. Commands like `/start-task`, `/create-task`, and `/complete-task` depend on those integrations. `/mcp-status` verifies connectivity **before** running such commands so users get immediate, actionable feedback instead of cryptic MCP or auth errors.

**Sources of configured servers**: The command discovers servers from three sources: (1) **User-level** MCP configuration: `mcpServers` in `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows), or via Cursor Settings → Features → Model Context Protocol. (2) **Project-level** (when present): `mcpServers` in `.cursor/mcp.json` at the workspace root. (3) **Extension-exposed** (when present): MCP servers provided by VS Code/Cursor extensions (e.g. Agent Context Explorer / extension-ace). Output distinguishes each server's source (user / project / extension) so users see where each integration comes from.

### Architecture

- **Skill location**: `skills/mcp-status/SKILL.md`. Executed as `/mcp-status` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Server discovery**: (1) User-level: read `~/.cursor/mcp.json` (or Windows equivalent) and extract `mcpServers` keys; if inaccessible, try common server names. (2) Project-level: if workspace root is available, read `.cursor/mcp.json` at workspace root and extract `mcpServers`; if file is missing, skip. (3) Extension-exposed: when the agent has access to extension MCP tools (e.g. extension-ace), call one read-only tool per known extension server and tag as (extension). Deduplicate by server name when same server appears in both user and project config; report with combined source (e.g. "user, project").
- **Flow**: (1) Discover servers from user, project, and extension sources; (2) for each server, call one lightweight read-only MCP tool; (3) report connected / disconnected with **source** (user / project / extension); for disconnected, provide reconnection steps (Cursor Settings → Features → Model Context Protocol).
- **Dependencies**: User and optional project MCP configuration; extension MCPs when present. **Outbound**: commands that require MCP (e.g. `/start-task`) should direct users to run `/mcp-status` when MCP is in doubt.

### Anti-Patterns

- **Don’t assume MCP is OK without checking** — Discover configured servers and test each one; do not trust a cached or assumed state.
- **Don’t ignore project or extension MCPs when present** — If project `.cursor/mcp.json` exists or extension-exposed tools are available, include them in discovery and report with the correct source (project / extension).
- **Don’t modify data** — The command is read-only; only call read-only MCP tools. No creates, updates, or deletes.

---

## Contract

### Definition of Done

- [ ] Skill exists at `skills/mcp-status/SKILL.md` and body conforms to the skill schema (schemas/skill.schema.json).
- [ ] Command discovers servers from user-level `mcp.json`, project-level `.cursor/mcp.json` at workspace root (when present), and extension-exposed MCPs (when the agent has access to their tools). If user config is inaccessible, tries common server names as fallback.
- [ ] For each discovered server, the command calls one lightweight read-only MCP tool and records success or failure with **source** (user / project / extension).
- [ ] Output clearly reports each server as connected or disconnected and distinguishes source (user / project / extension); for disconnected, includes reconnection steps (Cursor Settings → Features → Model Context Protocol).
- [ ] MkDocs docs for mcp-status (e.g. `docs/skills/mcp-status.md`) describe project-level config, extension-exposed MCPs, and example output with sources; updated in same commit as skill/spec (Same-Commit Rule).
- [ ] `python schemas/validate_all.py` passes (skill file validates against `schemas/skill.schema.json`).

### Regression Guardrails

- **Server discovery** — Servers are discovered from user-level `mcp.json`, optional project-level `.cursor/mcp.json` at workspace root, and extension-exposed MCPs when present. Discovery sources and output format are documented in the spec and user docs.
- **Docs in sync** — Skill, spec, and user docs (`docs/skills/mcp-status.md`) must stay in sync per AGENTS.md (Same-Commit Rule when behavior changes).
- **Read-only** — The command must only perform read-only operations; no MCP or filesystem writes.
- **Reconnection guidance** — When a server test fails, the command must distinguish auth errors (reconnect) from other errors and provide specific guidance.

### Scenarios

**Scenario: All configured MCP servers are connected (user config only)**
- **Given**: User MCP config includes `atlassian`, `github`; no project config; no extension MCPs
- **When**: The user runs `/mcp-status`
- **Then**: The command reports each of atlassian, github as connected with source (e.g. (user)) and a summary such as All systems operational!

**Scenario: Mixed sources (user + project + extension)**
- **Given**: User config has `atlassian`; project `.cursor/mcp.json` has `asdlc`; extension-ace is available
- **When**: The user runs `/mcp-status`
- **Then**: The command reports atlassian (user), asdlc (project), and extension-ace (extension) with status and source labels; output groups or labels by source

**Scenario: One MCP server is disconnected and needs reconnection**
- **Given**: MCP config includes `atlassian`; the Atlassian MCP server in Cursor has lost authentication
- **When**: The user runs `/mcp-status`
- **Then**: The command reports atlassian as disconnected and includes reconnection steps (Cursor Settings → Features → Model Context Protocol), with source (user) when applicable

**Scenario: Project-only or extension-only present**
- **Given**: No user config or empty; project `.cursor/mcp.json` has one server, or only extension MCPs are available
- **When**: The user runs `/mcp-status`
- **Then**: The command discovers and reports project or extension servers with (project) or (extension) source; no error for missing user config if other sources yield servers
