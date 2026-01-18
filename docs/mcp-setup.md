# MCP Setup for Cursor

Model Context Protocol (MCP) connects Cursor to Jira, Azure DevOps, and GitHub.

---

## Configuration

**Location:** Cursor Settings → Features → Model Context Protocol

Or edit `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows)

### Complete Setup

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer <YOUR_GITHUB_TOKEN>"
      }
    },
    "Atlassian-MCP-Server": {
      "url": "https://mcp.atlassian.com/v1/sse"
    }
  }
}
```

---

## GitHub Setup

**Generate token:** [github.com/settings/tokens](https://github.com/settings/tokens)
**Required scopes:** `repo`, `read:org`

Add token to configuration above, then test: `"List my repositories"`

---

## Atlassian (Jira) Setup

Configuration is already in the setup above. On first use, Cursor prompts for OAuth authorization.

Test: `"Get Jira issues in my current sprint"`

---

## Azure DevOps (Alternative)

Replace the Atlassian MCP config with:

```json
"ado": {
  "command": "npx",
  "args": ["-y", "--registry", "https://registry.npmjs.org/", "@azure-devops/mcp", "your-org-name"]
}
```

Test: `"Get work items in my current sprint"`

All Jira commands work with ADO—AI translates automatically.

---

## Troubleshooting

**MCP not connecting?** Restart Cursor, verify URLs, check internet connection.

**GitHub auth fails?** Verify token has `repo` and `read:org` scopes.

**Atlassian OAuth fails?** Clear browser cookies, try incognito window.

---

[:octicons-arrow-left-24: Back to Getting Started](getting-started.md)
