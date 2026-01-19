# MCP Setup for Cursor

Model Context Protocol (MCP) connects Cursor to GitHub and to an issue tracker (Jira or Azure DevOps).

**MCP combinations:** **GitHub + Jira** or **GitHub + ADO**. GitHub is used for repositories and pull requests; choose either Jira (Atlassian) or Azure DevOps for work items. ASDLC is optional.

---

## Configuration

**Location:** Cursor Settings → Features → Model Context Protocol

Or edit `~/.cursor/mcp.json` (macOS/Linux) or `%USERPROFILE%\.cursor\mcp.json` (Windows)

---

## Option A: GitHub + Jira

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer <YOUR_GITHUB_TOKEN>"
      }
    },
    "atlassian": {
      "url": "https://mcp.atlassian.com/v1/sse"
    }
  }
}
```

**GitHub:** [github.com/settings/tokens](https://github.com/settings/tokens) — scopes: `repo`, `read:org`

**Jira:** On first use, Cursor prompts for Atlassian OAuth. Test: *"Get Jira issues in my current sprint"*

---

## Option B: GitHub + Azure DevOps (ADO)

```json
{
  "mcpServers": {
    "ado": {
      "command": "npx",
      "args": ["-y", "@azure-devops/mcp", "your-org-name"]
    }
  }
}
```

Replace `your-org-name` with your Azure DevOps organization (e.g. `contoso` for `https://dev.azure.com/contoso`).

**ADO auth:** On first use, @azure-devops/mcp prompts for Microsoft sign-in. For unattended or CI, set `AZURE_DEVOPS_PAT` (and optionally `AZURE_DEVOPS_ORG_URL`) in the server’s `env` if your MCP or Cursor config supports it.

Test: *"Get work items in my current sprint"*

---

## Troubleshooting

**MCP not connecting?** Restart Cursor, verify URLs, check internet connection.

**GitHub auth fails?** Verify token has `repo` and `read:org` scopes.

**Atlassian OAuth fails?** Clear browser cookies, try incognito window.

---

[:octicons-arrow-left-24: Back to Getting Started](getting-started.md)
