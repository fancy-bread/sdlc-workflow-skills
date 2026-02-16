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
  <h1>SDLC Workflow Skills</h1>
  <p>SDLC workflow skills (Agent Skills format) that implement ASDLC workflows. Works in any Agent Skills–compatible environment (including Cursor) with MCP. Jira, Azure DevOps, and GitHub.</p>
  <p>
    <a href="getting-started/" class="md-button md-button--primary">Get Started</a>
    <a href="skills/" class="md-button">View Skills</a>
    <a href="https://github.com/fancy-bread/sdlc-workflow-skills" class="md-button">GitHub</a>
  </p>
</div>

---

## What This Is

SDLC Workflow Skills provides skills in Agent Skills format that implement ASDLC workflows. They work across teams and projects in any environment that supports Agent Skills (Cursor IDE is the primary tested environment).

**Built on:**

- **Agent Skills** – Markdown instructions with frontmatter (Cursor and other compatible environments)
- **MCP (Model Context Protocol)** – Connects to Jira, Azure DevOps, GitHub
- **ASDLC** – Principles for industrial-grade agentic software development

---

## How It Works

```mermaid
graph LR
    A[You] -->|/skill| B[AI Agent]
    B -->|invokes| C[MCP Tools]
    C --> D[Jira]
    C --> E[Azure DevOps]
    C --> F[GitHub]
    C --> G[Filesystem]

```

**Flow:**

1. **You invoke a skill** (e.g. `/start-task PROJ-123`)
2. **Your AI agent reads the skill** (markdown instruction file)
3. **AI invokes MCP tools** to interact with:
   - **Jira** - Issue tracking and project management
   - **Azure DevOps** - Work items and boards
   - **GitHub** - Repository and pull requests
   - **Filesystem** - Plans and code
4. **AI executes contextually** based on your project

**Result:** Consistent operations regardless of project, tech stack, or team.

---

[:octicons-zap-24: Quick Reference](skills/quick-reference.md){ .md-button }

---

## Getting Started

### 1. Setup MCP Connections

Connect your IDE or agent to your services (Jira, Azure DevOps, GitHub, filesystem). In Cursor: Settings → Features → Model Context Protocol.

### 2. Install Skills

Recommended: `npx skills add fancy-bread/sdlc-workflow-skills -a cursor` (choose **Copy** for Cursor). Or copy into your environment’s skills directory (e.g. Cursor: `~/.cursor/skills/` or `.cursor/skills/`). See [Getting Started](getting-started.md#step-2-install-skills).

### 3. Start Using

Invoke your first skill: `/create-task --type=story for [your feature]`

[:octicons-arrow-right-24: Full Setup Guide](getting-started.md){ .md-button .md-button--primary }

---

## Learn More

- **[Skills Reference](skills/index.md)** - All skills with previews
- **[How It Works](getting-started.md#how-it-works)** - Core principles
- **[Setup Instructions](mcp-setup.md)** - Detailed configuration
