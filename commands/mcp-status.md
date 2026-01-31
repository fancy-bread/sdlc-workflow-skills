# MCP Status

## Overview
Check the authentication status of all configured Model Context Protocol (MCP) servers.

## Definitions

- **MCP server**: A configured Model Context Protocol server in Cursor (e.g. github, atlassian, ado, asdlc).
- **MCP configuration**: The `mcpServers` section in `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows), or configured via Cursor Settings → Features → Model Context Protocol.

## Prerequisites

- **None required.** Run anytime to check status. If no MCP servers are configured, the command reports that.
- **MCP Tool Usage Standards**: MCP tool usage should follow best practices (check schema files, validate parameters, handle errors gracefully). These standards are documented in AGENTS.md §3 Operational Boundaries if AGENTS.md exists, but apply universally regardless.

## Purpose
MCP servers can disconnect or lose authentication after periods of inactivity. Use this command to verify all integrations are ready before starting work.

## Steps

1. **Discover configured MCP servers**
   - Read the MCP configuration file: `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows).
   - Extract the `mcpServers` object keys to get the list of configured server names (e.g. `github`, `atlassian`, `ado`, `asdlc`).
   - If the config file is not accessible, try common server names: `github`, `atlassian`, `ado`, `asdlc`, `user-github`, `user-atlassian`, `user-ado`, `user-asdlc` (with and without `user-` prefix).
   - Note: Server names in the config may differ from tool prefixes (e.g., config has `github` but tools use `mcp_github_*` or `mcp_user-github_*`).

2. **Test each server connection**
   - For each discovered server, attempt to call a lightweight read-only tool to verify connectivity and authentication.
   - Use common tool patterns for known server types:
     - **github** / **user-github** → Try `list_commits` (may require owner/repo args) or `list_branches`
     - **atlassian** / **user-atlassian** → Try `getAccessibleAtlassianResources` or `atlassianUserInfo`
     - **ado** / **user-ado** → Try `core_list_projects`
     - **asdlc** / **user-asdlc** → Try `list_articles`
   - For unknown server types, try common tool names like `list_*`, `get_*`, or `*_info` with minimal or empty args.
   - Record success or failure for each server. Handle "server not found" vs "authentication error" vs "tool not found" differently.

3. **Report status**
   - Display results in a clear, formatted list
   - Show server name and authentication status
   - For disconnected servers, provide reconnection instructions

## Tools

### Filesystem
- Read MCP configuration: `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows)
- Parse JSON to extract `mcpServers` keys

### MCP (per discovered server)
- **github** / **user-github** → Try `list_commits`, `list_branches`, or other read-only tools
- **atlassian** / **user-atlassian** → Try `getAccessibleAtlassianResources`, `atlassianUserInfo`
- **ado** / **user-ado** → Try `core_list_projects`
- **asdlc** / **user-asdlc** → Try `list_articles`
- **Other servers**: Try common read-only tool patterns (`list_*`, `get_*`, `*_info`) with minimal or empty args
- Note: Tool names may be prefixed with `mcp_<server>_` or `mcp_user-<server>_` depending on configuration

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
- If config file is not accessible, try common server names as fallback
- If no servers respond, report that no MCP servers are configured or accessible
- Provide link to MCP setup documentation (e.g., `docs/mcp-setup.md` if present, or general MCP setup instructions)

If a server test fails:
- **Server not found**: Server name doesn't exist in MCP configuration
- **Authentication error**: Server exists but needs reconnection/authentication
- **Tool not found**: Server exists but the tested tool isn't available (try a different tool)
- **Network/connection error**: Server unreachable or connection failed
- Provide specific guidance for each failure type, especially authentication errors which require user action

## Notes

- This command performs **read-only** operations only
- No data is modified or created
- Safe to run at any time
- Does not require any parameters or arguments

## Guidance

### Role
Act as a **developer** checking that MCP integrations are ready before running commands that depend on them.

### Instruction
Read the MCP configuration file (`~/.cursor/mcp.json` or Windows equivalent) to discover configured servers. For each server, attempt to call a lightweight read-only MCP tool to verify connectivity and authentication. Report connected / disconnected status; for disconnected servers, provide reconnection steps (Cursor Settings → Features → Model Context Protocol).

### Context
- MCP servers can disconnect or lose auth after inactivity. Use at start of day, after inactivity, or before critical commands.
- Discover servers from the MCP configuration file, not from project-specific directories or scripts.
- If config file is not accessible, try common server names and test connectivity.
- **ASDLC patterns**: [Context Gates](asdlc://context-gates)
- **ASDLC pillars**: **Quality Control** (pre-flight validation for other commands)

### Examples

**ASDLC**: [Context Gates](asdlc://context-gates) — MCP checks act as an input gate before running commands that depend on them.

### Constraints

**Rules (Must Follow):**
1. **Operational Standards Compliance**: This command follows operational standards (documented in AGENTS.md if present, but apply universally):
   - **MCP Tool Usage**: Check schema files, validate parameters, handle errors gracefully
   - **AGENTS.md Optional**: Commands work without AGENTS.md. Standards apply regardless of whether AGENTS.md exists.
   - See AGENTS.md §3 Operational Boundaries (if present) for detailed standards
2. **Read-only Operations**: This command performs read-only operations only; no data is modified or created.
3. **Error Handling**: If a server test fails, distinguish authentication errors (needs reconnect) from other errors and provide specific guidance.

