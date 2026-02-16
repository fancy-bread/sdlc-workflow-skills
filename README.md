# SDLC Workflow Skills

**SDLC workflow skills: skills (Agent Skills format) that implement ASDLC workflows.**

[![Documentation](https://img.shields.io/badge/docs-live-blue)](https://fancy-bread.github.io/sdlc-workflow-skills)
[![Schema Validation](https://github.com/fancy-bread/sdlc-workflow-skills/actions/workflows/skill-validation.yml/badge.svg)](https://github.com/fancy-bread/sdlc-workflow-skills/actions/workflows/skill-validation.yml)
[![ASDLC](https://img.shields.io/badge/ASDLC-aligned-5e35b1)](https://asdlc.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What This Is

SDLC Workflow Skills provides **SDLC workflow skills**—skills in [Agent Skills](https://cursor.com/docs/context/skills) format that implement [ASDLC](https://asdlc.io/) workflows. They work in any environment that supports Agent Skills (including Cursor IDE) and across teams and projects.

Built on ASDLC principles: Factory Architecture (specialized command stations), Standardized Parts (schema-enforced structure), and Quality Control (automated gates). See [ASDLC Alignment](docs/reference/asdlc-alignment.md) for pattern mapping.

**Built on:**
- **Agent Skills** – Markdown instructions with frontmatter (supported by Cursor and other Agent Skills–compatible environments)
- **MCP** – Jira, Azure DevOps, GitHub
- **Cursor IDE** – Primary tested environment; others may work where the format is supported

---

## Quick Start

### 1. Configure MCP

Configure MCP in your IDE or agent (e.g. **Cursor:** Settings → Features → Model Context Protocol):

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

### 2. Install Skills

**Cursor:** Install from GitHub: **Settings → Rules → Add Rule → Remote Rule (Github)** and enter `https://github.com/fancy-bread/sdlc-workflow-skills`. See [Installing skills from GitHub](https://cursor.com/docs/context/skills#installing-skills-from-github).

**Or** copy skills into your environment’s skills directory (same layout works for Cursor, Claude, and Codex):

```bash
# Cursor
cp -r skills/* ~/.cursor/skills/

# Claude
cp -r skills/* ~/.claude/skills/

# Codex
cp -r skills/* ~/.codex/skills/
```

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

- [Getting Started](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/) - 3-step setup
- [Skills Reference](https://fancy-bread.github.io/sdlc-workflow-skills/skills/) - All skills
- [Methodology](https://fancy-bread.github.io/sdlc-workflow-skills/getting-started/#how-it-works) - Core principles

---

## Requirements

- **Agent Skills–compatible environment** (e.g. [Cursor IDE](https://cursor.com))
- **Jira or Azure DevOps** – Issue tracking
- **GitHub** – Version control
- **GitHub token** – For MCP access

---

## License

MIT License - See [LICENSE](LICENSE) for details

-
