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

Verifies the authentication status of all configured MCP servers (Jira, GitHub, ASDLC, ADO, etc.). Tests each server connection and reports which servers are connected and which need reconnection, providing specific guidance for fixing authentication issues.

---

## ASDLC

- **Patterns**: [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Quality Control

---

## Example Output

**All connected:**
```
🔌 MCP Server Status

Configured servers:
  ✅ atlassian - Connected
  ✅ github - Connected

All systems operational!
```

**Action needed:**
```
🔌 MCP Server Status

Configured servers:
  ❌ atlassian - Needs authentication
  ✅ github - Connected

⚠️ To reconnect:
Settings → Tools & MCP → Click "Connect"
```

## When to Use

| Scenario | Why |
|----------|-----|
| **Start of work** | Verify connections before running commands |
| **After idle time** | MCP servers disconnect after inactivity |
| **Troubleshooting** | Diagnose authentication failures |
| **Before critical work** | Ensure integrations ready for `/start-task`, etc. |

---

**[View full command (source)](https://github.com/fancybread-com/agentic-software-development/blob/main/commands/mcp-status.md)**

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

