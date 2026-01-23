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

**MCP combinations:** **GitHub + Jira** or **ADO**. [Full MCP setup →](mcp-setup.md) (Option A or B).

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
    "atlassian": {
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

[Detailed MCP setup →](mcp-setup.md)

---

## Step 2: Install Commands

Command files live in **`commands/`** (in the repo or in the release archive). Download the latest release and copy them into Cursor's commands directory.

[**View installation instructions →**](releases.md#installation)

**Quick summary:**

1. Download the latest release from the [Releases page](releases.md)
2. Extract the archive
3. Copy `commands/*` to `~/.cursor/commands/` (global) or `.cursor/commands/` (per-project). **Cursor Team/Enterprise:** [Dashboard → Team Content → Commands](https://cursor.com/dashboard?tab=team-content&section=commands) — create team commands from `commands/`; they sync to your team.
4. Restart Cursor

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

- Specs in `specs/` folder (permanent feature contracts)
- Plans in `.plans/` folder (transient task implementation)
- PRs link to stories
- Commits include story IDs

[See the product flow diagram →](index.md#how-it-works)

---

## Next Steps

- **[View All Commands](commands/index.md)** - Browse 9 available commands
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

**Integration error:**

- Verify credentials and permissions in MCP settings.

**Plan not found:**

- Run `/create-plan` before `/start-task`.

**Story missing detail:**

- Commands will ask for clarification when information is insufficient.

