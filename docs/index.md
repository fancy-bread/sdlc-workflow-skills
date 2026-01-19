---
title: Home
hide:
  - navigation
  - toc
---

<style>
.hero {
  text-align: center;
  padding: 4rem 2rem;
  margin: -2rem -2rem 3rem -2rem;
  background: linear-gradient(135deg, #5e35b1 0%, #4527a0 100%);  /* Deep purple gradient */
  color: white;
}

.hero h1 {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
  color: white;
  border: none;
  text-shadow: 0 2px 4px rgba(0,0,0,0.2);  /* Improved readability on purple */
}

.hero p {
  font-size: 1.25rem;
  margin-bottom: 2rem;
  color: white;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.6;
  text-shadow: 0 1px 2px rgba(0,0,0,0.2);
}

.hero .md-button {
  margin: 0.5rem;
  font-size: 1rem;
  padding: 0.75rem 2rem;
  box-shadow: 0 2px 4px rgba(0,0,0,0.3);
}

.hero .md-button--primary {
  background-color: white;
  color: #4527a0;  /* Deep purple text on white */
  border: none;
  font-weight: 500;
}

.hero .md-button--primary:hover {
  background-color: #f5f5f5;
  color: #311b92;  /* Darker purple on hover */
}

.hero .md-button:not(.md-button--primary) {
  background-color: rgba(255,255,255,0.1);
  color: white;
  border: 2px solid rgba(255,255,255,0.3);
}

.hero .md-button:not(.md-button--primary):hover {
  background-color: rgba(255,255,255,0.2);
  border-color: rgba(255,255,255,0.5);
}

@media screen and (max-width: 768px) {
  .hero h1 {
    font-size: 2rem;
  }
  .hero p {
    font-size: 1.1rem;
  }
}
</style>

<div class="hero">
  <h1>Agentic Software Development</h1>
  <p>Standardize your SDLC with natural language commands. Built for Cursor IDE and MCP tools. Works with Jira, Azure DevOps, and GitHub.</p>
  <p>
    <a href="getting-started.md" class="md-button md-button--primary">Get Started</a>
    <a href="commands/" class="md-button">View Commands</a>
    <a href="https://github.com/fancybread-com/agentic-software-development" class="md-button">GitHub</a>
  </p>
</div>

---

## What This Is

A standardized approach to Software Development Lifecycle operations using well-defined, organized commands that work across teams and projects.

**Built on:**

- **Cursor IDE** - AI-powered development environment
- **MCP (Model Context Protocol)** - Connects to Jira, Azure DevOps, GitHub
- **Natural language commands** - Markdown instructions for AI agents

---

## How It Works

```mermaid
graph LR
    A[You] -->|/command| B[Cursor AI]
    B -->|invokes| C[MCP Tools]
    C --> D[Jira]
    C --> E[Azure DevOps]
    C --> F[GitHub]
    C --> G[Filesystem]

```

**Flow:**

1. **You invoke a command** (e.g., `/start-task PROJ-123`)
2. **Cursor AI reads the command** (markdown instruction file)
3. **AI invokes MCP tools** to interact with:
   - **Jira** - Issue tracking and project management
   - **Azure DevOps** - Work items and boards
   - **GitHub** - Repository and pull requests
   - **Filesystem** - Plans and code
4. **AI executes contextually** based on your project

**Result:** Consistent operations regardless of project, tech stack, or team.

---

## Find Your Commands

<div class="grid cards" markdown>

-   **Product Manager**

    Create and prioritize features

    [:octicons-arrow-right-24: View](roles/product-manager.md)

-   **Software Engineer**

    Development and quality

    [:octicons-arrow-right-24: View](roles/engineer.md)

-   **QA Engineer**

    Testing and verification

    [:octicons-arrow-right-24: View](roles/qa.md)

</div>

[:octicons-person-24: View by Role](commands/by-role.md){ .md-button }
[:octicons-zap-24: Quick Reference](commands/quick-reference.md){ .md-button }

---

## Getting Started

### 1. Setup MCP Connections

Connect Cursor to your services (Jira, Azure DevOps, GitHub, filesystem).

### 2. Install Commands

Add command library to your Cursor workspace.

### 3. Start Using

Invoke your first command: `/create-task --type=story for [your feature]`

[:octicons-arrow-right-24: Full Setup Guide](getting-started.md){ .md-button .md-button--primary }

---

## Learn More

- **[Commands Reference](commands/index.md)** - All 9 commands with previews
- **[Role Guides](roles/index.md)** - Commands organized by role
- **[How It Works](getting-started.md#how-it-works)** - Core principles
- **[Setup Instructions](mcp-setup.md)** - Detailed configuration
