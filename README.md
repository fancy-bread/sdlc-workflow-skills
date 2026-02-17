# SDLC Workflow Skills

**Agent Skills that implement ASDLC workflows.**

[![Documentation](https://img.shields.io/badge/docs-live-blue)](https://fancy-bread.github.io/sdlc-workflow-skills)
[![Schema Validation](https://github.com/fancy-bread/sdlc-workflow-skills/actions/workflows/skill-validation.yml/badge.svg)](https://github.com/fancy-bread/sdlc-workflow-skills/actions/workflows/skill-validation.yml)
[![ASDLC](https://img.shields.io/badge/ASDLC-aligned-5e35b1)](https://asdlc.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What This Is

SDLC Workflow Skills provides [Agent Skills](https://agentskills.io) that implement [ASDLC](https://asdlc.io/) workflows. They work in any environment that supports Agent Skills and across teams and projects.

Built on ASDLC principles: Factory Architecture (specialized command stations), Standardized Parts (schema-enforced structure), and Quality Control (automated gates). See [ASDLC Alignment](https://fancy-bread.github.io/sdlc-workflow-skills/reference/asdlc-alignment/) for pattern mapping.

**Built on:**
- **Agent Skills** – Markdown instructions with frontmatter (supported by Cursor and other Agent Skills–compatible environments)
- **MCP** – Jira, Azure DevOps, GitHub
- **Cursor IDE** – Primary tested environment; others may work where the format is supported

---

## Quick Start

### 1. Configure MCP

Configure MCP in your IDE or agent (e.g. **Cursor:** Settings → Features → Model Context Protocol). Example for **GitHub + Jira**:

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
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://mcp.atlassian.com/v1/mcp"]
    }
  }
}
```

GitHub token: [github.com/settings/tokens](https://github.com/settings/tokens) (scopes: `repo`, `read:org`). Jira: your environment will prompt for Atlassian OAuth on first use. [Full MCP setup →](https://fancy-bread.github.io/sdlc-workflow-skills/reference/mcp-setup/)

### 2. Install Skills

**Recommended:** Install with the [skills CLI](https://github.com/vercel-labs/skills) (Cursor, Claude, Codex):

```bash
npx skills add fancy-bread/sdlc-workflow-skills -a cursor
```

Choose **Copy** when prompted (symlinks can prevent Cursor from listing skills).

**Or** copy the repo's `skills/` folder into your environment's skills directory:

| Environment | User-level | Project-level |
|-------------|------------|---------------|
| **Cursor**  | `~/.cursor/skills/`  | `.cursor/skills/`  |
| **Claude**  | `~/.claude/skills/`  | `.claude/skills/`  |
| **Codex**   | `~/.codex/skills/`   | `.codex/skills/`   |

**Or** use a [packaged release](https://github.com/fancy-bread/sdlc-workflow-skills/releases): download the `.tar.gz` or `.zip` for the latest version, extract it, and copy the `skills/` folder into your environment's directory (see table above).

[Full installation options →](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/#step-2-install-skills) (npx, packaged releases, Cursor Remote Rule)

### 3. Use Skills (slash commands)

```
/create-task --type=story for user authentication
/create-plan for PROJ-123
/start-task PROJ-123
/complete-task PROJ-123
```

[Full setup guide →](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/) | [Try a Development Workflow →](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/#try-a-development-workflow)

---

## Available Skills

- **Product (2):** `/create-task`, `/decompose-task`
- **Planning (2):** `/refine-task`, `/create-plan`
- **Development (2):** `/start-task`, `/complete-task`
- **Quality (2):** `/create-test`, `/review-code`
- **Utilities (2):** `/mcp-status`, `/setup-asdlc`

[View all skills →](https://fancy-bread.github.io/sdlc-workflow-skills/skills/)

---

## How It Works

Skills connect you to AI agents that interact with Jira, GitHub, and your codebase. The AI reads your project context and executes workflows consistently across projects.

[Full explanation →](https://fancy-bread.github.io/sdlc-workflow-skills/#how-it-works)

---

## Documentation

📚 **[Full Documentation](https://fancy-bread.github.io/sdlc-workflow-skills)**

- [Getting Started](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/) — 3-step setup
- [Skills Reference](https://fancy-bread.github.io/sdlc-workflow-skills/skills/) — All skills
- [MCP Setup](https://fancy-bread.github.io/sdlc-workflow-skills/reference/mcp-setup/) — Configure GitHub, Jira, ADO
- [Methodology](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/#how-it-works) — Core principles

---

## Requirements

- **Agent Skills–compatible environment** (e.g. [Cursor IDE](https://cursor.com))
- **Jira or Azure DevOps** – Issue tracking (Jira uses OAuth on first use)
- **GitHub** – Version control
- **GitHub token** – For MCP (scopes: `repo`, `read:org`)

---

## License

MIT License — See [LICENSE](LICENSE) for details.
