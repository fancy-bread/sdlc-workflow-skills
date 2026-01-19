# Agentic Software Development

**Standardize SDLC operations with natural language commands for Cursor IDE.**

[![Documentation](https://img.shields.io/badge/docs-live-blue)](https://fancybread-com.github.io/agentic-software-development)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What This Is

A proposal to standardize common Software Development Lifecycle operations into well-defined commands that work across teams and projects.

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

[Full setup guide →](https://fancybread-com.github.io/agentic-software-development/getting-started/)

---

## Available Commands

**9 essential commands:**

- **Product (2):** Create tasks and decompose large tasks
- **Planning (2):** Refine tasks and create technical implementation plans
- **Development (2):** Build and ship features
- **Quality (2):** Write tests and review code
- **Utilities (1):** Check MCP status

[View all commands →](https://fancybread-com.github.io/agentic-software-development/commands/)

---

## How It Works

```
You → /command → Cursor AI → MCP → Services (Jira, GitHub)
```

1. You invoke a command (e.g., `/start-task PROJ-123`)
2. Cursor AI reads the command instruction
3. AI uses MCP to interact with Jira, GitHub, filesystem
4. AI executes contextually based on your project

**Result:** Consistent operations across projects and tech stacks.

---

## Documentation

📚 **[Full Documentation](https://fancybread-com.github.io/agentic-software-development)**

- [Getting Started](https://fancybread-com.github.io/agentic-software-development/getting-started/) - 3-step setup
- [Commands Reference](https://fancybread-com.github.io/agentic-software-development/commands/) - All 9 commands
- [Role Guides](https://fancybread-com.github.io/agentic-software-development/roles/) - Product Manager, Engineer, QA
- [Methodology](https://fancybread-com.github.io/agentic-software-development/core/methodology/) - Core principles

---

## Requirements

- **Cursor IDE** - [Download](https://cursor.com)
- **Jira or Azure DevOps** - Issue tracking
- **GitHub** - Version control
- **GitHub token** - For MCP access

---

## License

MIT License - See [LICENSE](LICENSE) for details

---

## Contributing

This is a proposal and reference implementation. Feedback and improvements welcome via issues and pull requests.
