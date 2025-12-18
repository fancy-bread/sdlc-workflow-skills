---
title: Commands Reference
---

# Command Reference

**All 8 commands for AI-assisted development.**

Quick access to every command with usage examples and previews of actual command files.

[:octicons-person-24: View by Role](by-role.md){ .md-button }
[:octicons-zap-24: Quick Reference](quick-reference.md){ .md-button }

---

## Product (2 commands)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-task`](create-task.md)** | Product Manager, Engineer, QA | Create tasks with specified type (epic, story, bug, task, etc.) |
| **[`/breakdown-tasks`](breakdown-tasks.md)** | Product Manager, Scrum Master | Break down large tasks into well-defined subtasks |

*Note: Legacy commands `/create-story` and `/create-epic` have been replaced by `/create-task`. Use `/create-task --type=story` or `/create-task --type=epic` instead.*

---

## Planning (1 command)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-plan`](create-plan.md)** | Engineer | Create technical implementation design |

---

## Development (2 commands)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/start-task`](start-task.md)** | Engineer | Begin implementation with branch and context |
| **[`/complete-task`](complete-task.md)** | Engineer | Commit, push, create PR |

---

## Quality (2 commands)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-test`](create-test.md)** | Engineer, QA | Generate unit tests (adapts for backend/frontend) |
| **[`/review-code`](review-code.md)** | Senior Engineer | AI-assisted code review |

---

## Utilities (1 command)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/mcp-status`](mcp-status.md)** | All Roles | Check MCP server authentication status |

---

## Navigation

- **[By Role](by-role.md)** - Commands organized by who uses them
- **[Quick Reference](quick-reference.md)** - Copy-paste cheat sheet
- **[Role Guides](../roles/index.md)** - Brief role overviews

---

## How Commands Work

Commands are markdown files that tell AI agents what to achieve. The AI reads your:

- Project structure and code
- Issue tracker (Jira/ADO)
- Implementation plans
- Team conventions

Then executes contextually - same command, different projects, intelligent adaptation.

[Learn more about the methodology →](../getting-started.md#how-it-works)
