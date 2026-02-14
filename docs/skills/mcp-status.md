---
title: MCP Status Command
---

# `/mcp-status`

Verify authentication status of all configured MCP servers.

| | |
|---|---|
| **Frequency** | As needed (start of work, troubleshooting) |
| **Prerequisites** | None |

---

## What It Does

Verifies the authentication status of all configured MCP servers (Jira, GitHub, ASDLC, ADO, etc.). Discovers servers from **user-level** config (`~/.cursor/mcp.json`), optional **project-level** config (`.cursor/mcp.json` at workspace root), and **extension-exposed** MCPs (e.g. Agent Context Explorer) when present. Tests each server connection and reports which are connected and which need reconnection, with the **source** (user / project / extension) for each. Provides specific guidance for fixing authentication issues.

---

## ASDLC

- **Patterns**: [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Quality Control

---

## Configuration sources

Servers are discovered from:

| Source | Location | When used |
|--------|----------|-----------|
| **User** | `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows) | Always (or common server names as fallback) |
| **Project** | `.cursor/mcp.json` at workspace root | When the file exists in the project |
| **Extension** | MCPs exposed by VS Code/Cursor extensions (e.g. Agent Context Explorer) | When the extension is enabled and exposes tools |

Output labels each server with its source: **(user)**, **(project)**, or **(extension)**. Reconnection steps apply to user- and project-configured servers.

---

## Example Output

**All connected (with sources):**
```
🔌 MCP Server Status

User config:
  ✅ atlassian - Connected (user)
  ✅ github - Connected (user)

Project config:
  (none)

Extensions:
  ✅ extension-ace - Connected (extension)

All systems operational!
```

**Action needed:**
```
🔌 MCP Server Status

User config:
  ❌ atlassian - Needs authentication (user)
  ✅ github - Connected (user)

⚠️ To reconnect:
Cursor: Settings → Features → Model Context Protocol → Connect for the failing server, then run /mcp-status again.
```

## When to Use

| Scenario | Why |
|----------|-----|
| **Start of work** | Verify connections before running commands |
| **After idle time** | MCP servers disconnect after inactivity |
| **Troubleshooting** | Diagnose authentication failures |
| **Before critical work** | Ensure integrations ready for `/start-task`, etc. |

---

**[View full skill (source)](https://github.com/fancybread-com/sdlc-workflow-skills/blob/main/skills/mcp-status/SKILL.md)**

---

## Usage

```bash
/mcp-status
```

No arguments needed. Returns status of all configured MCP integrations.

---

## Related Commands

- **[`/setup-asdlc`](setup-asdlc.md)** - Initialize repository for ASDLC adoption

---

[:octicons-arrow-left-24: Back to Commands](index.md)

