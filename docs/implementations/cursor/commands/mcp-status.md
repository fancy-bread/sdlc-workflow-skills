# `/mcp-status` - MCP Server Status Check

**Implementation:** Cursor AI Command

## Command File

**[View Full Command →](../../../implementations/cursor/commands/mcp-status.md)**

## What It Does

Checks authentication status of all configured MCP (Model Context Protocol) servers and reports which ones need reconnection.

## How It Works

1. **Discovery**: Lists all MCP servers configured in Cursor
2. **Testing**: Attempts a lightweight read operation on each server
3. **Reporting**: Shows connection status and reconnection steps if needed

## Used By

- **[All Roles](../../../roles/engineer.md)** - Before starting work session

## Example Usage

```
User: /mcp-status

AI: 🔌 MCP Server Status

Configured servers:
  ✅ Atlassian-MCP-Server - Connected
  ✅ github - Connected

All systems operational!
```

## When MCP Disconnects

MCP servers can lose authentication after periods of inactivity. This command helps you:
- Identify which server needs reconnection
- Get clear steps to reconnect in Cursor Settings
- Verify the fix worked

[:octicons-arrow-left-24: Back to Commands](../../../commands/index.md)

