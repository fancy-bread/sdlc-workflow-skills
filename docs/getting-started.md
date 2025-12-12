---
title: Getting Started
---

# Getting Started

## Prerequisites

- **Cursor IDE** - [Download](https://cursor.com)
- **Jira or Azure DevOps** - Active account with API access
- **GitHub** - Account with personal access token

---

## Step 1: Configure MCP

Open **Cursor Settings → Features → Model Context Protocol** and add:

```json
{
  "mcpServers": {
    "github": {
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer <TOKEN>"
      }
    },
    "Atlassian-MCP-Server": {
      "url": "https://mcp.atlassian.com/v1/sse"
    },
  }
}
```

**Get GitHub Token:**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Generate new token (classic)
3. Select scopes: `repo` and `read:org`
4. Copy token into config above

**Authorize Atlassian:**

First time you use Jira commands, Cursor will prompt OAuth authorization.

!!! tip "Azure DevOps Alternative"
    For Azure DevOps instead of Jira, use this configuration:

    ```json
    "ado": {
      "command": "npx",
      "args": [
        "-y",
        "--registry",
        "https://registry.npmjs.org/",
        "@azure-devops/mcp",
        "your-organization-name"
      ]
    }
    ```

    Replace `your-organization-name` with your ADO organization.

[Detailed MCP setup →](implementations/cursor/mcp-setup.md)

---

## Step 2: Install Commands

Copy command files to Cursor:

**Global (all projects):**

```bash
cd /path/to/this/repo
cp -r implementations/cursor/commands/* ~/.cursor/commands/
```

**Per-project:**

```bash
cd /path/to/your/project
mkdir -p .cursor/commands
cp -r /path/to/this/repo/implementations/cursor/commands/* .cursor/commands/
```

**Restart Cursor** after installing.

---

## Step 3: Run Your First Command

Open Cursor Chat (`Cmd/Ctrl + L`) and run:

```
/create-task --type=story for user profile page with avatar upload
```

AI will:

1. Read the command instruction
2. Connect to Jira via MCP
3. Create story with title, acceptance criteria, and labels
4. Return story ID (e.g., `PROJ-123`)

**That's it!** You're using agentic commands.

---

## Try a Development Workflow

```bash
# Plan
/create-plan for PROJ-123

# Build
/start-task PROJ-123

# Ship
/complete-task PROJ-123
```

---

## How It Works

**AI agents handle routine tasks:**

- Story and epic creation
- Implementation planning
- Branch and PR creation
- Test generation
- Issue updates

**You control decisions:**

- Plan approval
- Code review
- Work selection
- Architecture

**Full transparency:**

- Plans in `.plans/` folder
- PRs link to stories
- Commits include story IDs

---

## Next Steps

- **[View All Commands](commands/index.md)** - Browse 11 available commands
- **[Find Your Role](roles/index.md)** - See which commands you need
- **[Quick Reference](commands/quick-reference.md)** - Command cheat sheet

---

## Troubleshooting

**Commands don't appear:**

- Verify files in `~/.cursor/commands/` or `.cursor/commands/`
- Restart Cursor completely

**MCP authorization fails:**

- Check Settings → MCP shows "Connected"
- Verify GitHub token has `repo` and `read:org` scopes
- Re-authorize Atlassian MCP

**Command fails:**

- Check error message (AI explains the issue)
- Verify story/repo exists and you have permissions
- Ensure you're in a git repository

