---
title: MCP Status Command
---

# `/mcp-status` - Check MCP Server Connections

**Verify authentication status of all configured MCP servers.**

## Quick Start

```bash
/mcp-status
```

No arguments needed. Returns status of all configured MCP integrations.

## What It Does

Checks each configured MCP server (Jira, GitHub, etc.) to verify:
- ✅ Server is reachable
- ✅ Authentication is valid
- ⚠️ Which servers need reconnection

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

## Used By

- **All Engineers** - Before starting work
- **All Roles** - When encountering MCP errors

---

## Related Commands

**Other utility commands:**
- Coming soon: Additional MCP management commands

---

[:octicons-arrow-left-24: Back to Commands](index.md)

