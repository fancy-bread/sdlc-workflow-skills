# Agentic Software Development

**Standardize SDLC operations with natural language commands for Cursor IDE.**

[![Documentation](https://img.shields.io/badge/docs-live-blue)](https://fancybread-com.github.io/agentic-software-development)
[![Schema Validation](https://github.com/fancybread-com/agentic-software-development/actions/workflows/command-validation.yml/badge.svg)](https://github.com/fancybread-com/agentic-software-development/actions/workflows/command-validation.yml)
[![ASDLC](https://img.shields.io/badge/ASDLC-aligned-5e35b1)](https://asdlc.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What This Is

Standardized common Software Development Lifecycle commands that work across teams and projects.

Built on [ASDLC.io](https://asdlc.io/) principles for industrial-grade agentic software development. Implements Factory Architecture with specialized command stations, schema-enforced Standardized Parts, and automated Quality Control gates. Demonstrates Level 3 Conditional Autonomy where agents execute workflows with human oversight at decision points. See [ASDLC Alignment](docs/asdlc-alignment.md) for detailed pattern mapping.

**Built on:**
- Cursor IDE (AI-powered development)
- MCP (connects to Jira, Azure DevOps, GitHub)
- Natural language commands (markdown instructions)

---

## Quick Start

### 1. Configure MCP

**Cursor Settings → Features → Model Context Protocol:**

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

### 2. Install Commands

```bash
cp -r commands/* ~/.cursor/commands/
```

### 3. Use Commands

```
/create-task --type=story for user authentication
/create-plan for PROJ-123
/start-task PROJ-123
/complete-task PROJ-123
```

[Full setup guide →](https://fancybread-com.github.io/agentic-software-development/getting-started/) | [Try a Development Workflow →](https://fancybread-com.github.io/agentic-software-development/getting-started/#try-a-development-workflow)

---

## Available Commands

- **Product (2):** `/create-task`, `/decompose-task`
- **Planning (2):** `/refine-task`, `/create-plan`
- **Development (2):** `/start-task`, `/complete-task`
- **Quality (2):** `/create-test`, `/review-code`
- **Utilities (1):** `/mcp-status`

[View all commands →](https://fancybread-com.github.io/agentic-software-development/commands/)

---

## How It Works

Commands connect you to AI agents that interact with Jira, GitHub, and your codebase. The AI reads your project context and executes operations consistently across projects.

[Full explanation →](https://fancybread-com.github.io/agentic-software-development/#how-it-works)

---

## Documentation

📚 **[Full Documentation](https://fancybread-com.github.io/agentic-software-development)**

- [Getting Started](https://fancybread-com.github.io/agentic-software-development/getting-started/) - 3-step setup
- [Commands Reference](https://fancybread-com.github.io/agentic-software-development/commands/) - All commands
- [Methodology](https://fancybread-com.github.io/agentic-software-development/getting-started/#how-it-works) - Core principles

---

## Requirements

- **Cursor IDE** - [Download](https://cursor.com)
- **Jira or Azure DevOps** - Issue tracking
- **GitHub** - Version control
- **GitHub token** - For MCP access

---

## License

MIT License - See [LICENSE](LICENSE) for details

-
