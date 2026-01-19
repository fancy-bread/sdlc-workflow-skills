# MCP Status

## Overview
Check the authentication status of all configured Model Context Protocol (MCP) servers.

## Purpose
MCP servers can disconnect or lose authentication after periods of inactivity. Use this command to verify all integrations are ready before starting work.

## Steps

1. **Get the list of record (configured MCP servers and tools)**
   - Run: `python schemas/validate_mcps.py --list` (or `--list --json` for machine-readable).
   - This enumerates `mcps/<server>/tools/*.json` — the **list of record** for which MCP tools this project supports. Servers are the top-level dirs under `mcps/` (e.g. `atlassian`, `github`, `asdlc`, `ado`).
   - Use this list (not a runtime MCP API) to know which servers and `mcp_<Server>_<Tool>` refs exist.

2. **Test each server connection**
   - For each server in the list of record, call a lightweight read-only tool. Use this mapping (from `mcps/`):
     - **atlassian** → `mcp_atlassian_getAccessibleAtlassianResources` or `mcp_atlassian_atlassianUserInfo`
     - **github** → `mcp_github_list_commits` (args: owner, repo)
     - **asdlc** → `mcp_asdlc_list_articles`
     - **ado** → `mcp_ado_core_list_projects`
   - If a server has no entry above, pick a read-only tool from `python schemas/validate_mcps.py --list` for that server and call it with minimal required args.
   - Record success or failure for each server.

3. **Report status**
   - Display results in a clear, formatted list
   - Show server name and authentication status
   - For disconnected servers, provide reconnection instructions

## Expected Output

### All Connected
```
🔌 MCP Server Status

Configured servers:
  ✅ atlassian - Connected
  ✅ github - Connected
  ✅ filesystem - Connected

All systems operational!
```

### Some Disconnected
```
🔌 MCP Server Status

Configured servers:
  ❌ atlassian - Needs authentication
  ✅ github - Connected
  ✅ filesystem - Connected

⚠️ Action Required:
1. Open Cursor Settings (Cmd+, or Ctrl+,)
2. Navigate to: Tools & MCP
3. Click "Connect" next to: atlassian
4. Run /mcp-status again to verify
```

## When to Use

- **Start of day** - Verify connections before beginning work
- **After inactivity** - MCP servers may disconnect after timeout
- **Before critical commands** - Ensure integrations are ready for commands like `/start-task`, `/create-task`, etc.
- **Troubleshooting** - When other commands fail with authentication errors

## Error Handling

If unable to discover MCP servers:
- Report that no MCP servers are configured
- Provide link to MCP setup documentation

If a server test fails:
- Distinguish between authentication errors (needs reconnect) and other errors
- Provide specific guidance for each failure type

## Notes

- This command performs **read-only** operations only
- No data is modified or created
- Safe to run at any time
- Does not require any parameters or arguments

