---
title: Getting Started
---

# Getting Started

## Prerequisites

- **Agent Skills–compatible environment** (e.g. [Cursor IDE](https://cursor.com))
- **Jira or Azure DevOps** – Active account with API access
- **GitHub** – Account with personal access token

---

## Step 1: Configure MCP

**MCP combinations:**
- **GitHub + Jira** — GitHub for repos/PRs, Jira for issue tracking
- **ADO only** — Azure DevOps provides both repo management and issue tracking

[Full MCP setup →](mcp-setup.md) (Option A or B).

Open your environment’s MCP settings (e.g. **Cursor:** Settings → Features → Model Context Protocol) and add:

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
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/mcp"]
    }
  }
}
```

**Get GitHub Token:**

1. Go to [github.com/settings/tokens](https://github.com/settings/tokens)
2. Generate new token (classic)
3. Select scopes: `repo` and `read:org`
4. Copy token into config above

**Authorize Atlassian:**

First time you use Jira, your environment may prompt for OAuth (e.g. Cursor prompts for Atlassian authorization).

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

## Step 2: Install Skills

This repo uses the [Agent Skills](https://agentskills.io) format. The same **`skills/`** layout and **`SKILL.md`** files work for **Cursor**, **Claude**, and **Codex**—each environment loads from its own skills directory (see table below). **Cursor** users can also install directly from GitHub; others copy from a release.

| Environment | Project-level | User-level (global) |
|-------------|----------------|---------------------|
| **Cursor**  | `.cursor/skills/`  | `~/.cursor/skills/`  |
| **Claude**  | `.claude/skills/`  | `~/.claude/skills/`  |
| **Codex**   | `.codex/skills/`   | `~/.codex/skills/`   |

Choose one of the following.

### Option A: Install from GitHub (Cursor)

[Cursor supports loading skills from a GitHub repository](https://cursor.com/docs/context/skills#installing-skills-from-github):

1. Open **Cursor Settings** (e.g. `Cmd+Shift+J` / `Ctrl+Shift+J`) → **Rules**
2. Under **Project Rules**, click **Add Rule**
3. Select **Remote Rule (Github)**
4. Enter this repository URL:
   ```text
   https://github.com/fancybread-com/sdlc-workflow-skills
   ```

Skills are loaded from the repo; you get updates when Cursor refreshes. No need to download or copy files.

**Layout (Cursor, Claude, Codex)**

The same layout works for all three: a top-level **`skills/`** directory; each skill is a subfolder containing **`SKILL.md`** with YAML frontmatter **`name`** (matching the folder name) and **`description`**. See [Cursor: Agent Skills](https://cursor.com/docs/context/skills#skillmd-file-format) and [agentskills.io](https://agentskills.io).

To verify locally:

```bash
python scripts/verify_github_install.py
```

If it prints `OK: repo ready for Cursor/Claude/Codex (N skills).`, the layout is correct. This check also runs in CI on every pull request. To confirm in Cursor: add the repo as a Remote Rule (Github), then open **Settings → Rules** and check that skills appear under **Agent Decides**.

### Option B: Download release and copy

Skills live in **`skills/`** (in the repo or in the release archive). Copy them into your environment’s skills directory.

[**Full installation details →**](releases.md#installation)

**Summary:**

1. Download the latest release from the [Releases page](releases.md)
2. Extract the archive
3. Copy `skills/*` to your environment’s skills directory (see table above: Cursor `.cursor/skills/` or `~/.cursor/skills/`, Claude `.claude/skills/` or `~/.claude/skills/`, Codex `.codex/skills/` or `~/.codex/skills/`). **Cursor Team/Enterprise:** Use Dashboard → Team Content → Skills to create team skills from `skills/`; they sync to your team.
4. Restart your IDE or agent

---

## Step 3: Run Your First Skill

Open your agent chat (e.g. **Cursor:** `Cmd/Ctrl + L`) and run:

```
/create-task --type=story for user profile page with avatar upload
```

AI will:

1. Read the command instruction
2. Connect to Jira via MCP
3. Create story with title, acceptance criteria, and labels
4. Return story ID (e.g., `PROJ-123`)

**That's it!** You're using agentic skills.

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

- **[View All Skills](skills/index.md)** - Browse available skills
- **[Quick Reference](skills/quick-reference.md)** - Skill cheat sheet
- **[Cursor: Agent Skills](https://cursor.com/docs/context/skills)** - Skill format, GitHub install, Cursor/Claude/Codex skill directories
- **[Claude: Extend with skills](https://code.claude.com/docs/en/skills)** - Claude Code skills (`.claude/skills/`)
- **[agentskills.io](https://agentskills.io)** - Agent Skills open standard

---

## Troubleshooting

**Skills don't appear:**

- Verify skill folders in your environment’s skills directory (e.g. Cursor: `~/.cursor/skills/` or `.cursor/skills/`)
- Restart your IDE or agent completely

**MCP authorization fails:**

- Check Settings → MCP shows "Connected"
- Verify GitHub token has `repo` and `read:org` scopes
- Re-authorize Atlassian MCP

**Skill fails:**

- Check error message (AI explains the issue)
- Verify story/repo exists and you have permissions
- Ensure you're in a git repository

**Integration error:**

- Verify credentials and permissions in MCP settings.

**Plan not found:**

- Run `/create-plan` before `/start-task`.

**Story missing detail:**

- Commands will ask for clarification when information is insufficient.

