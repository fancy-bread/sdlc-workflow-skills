---
title: Commands Reference
---

# Command Reference

**Commands for AI-assisted development.**

The canonical command definitions (the markdown files Cursor executes) live in **`commands/`** at the repo root; those files are the source of truth. This documentation describes what each command does. For full instruction content, see the [repository `commands/` folder](https://github.com/fancybread-com/agentic-software-development/tree/main/commands). Command files are plain markdown with structured sections; validate with `python schemas/validate.py commands/<name>.md` (see [schemas/README](https://github.com/fancybread-com/agentic-software-development/blob/main/schemas/README.md)).

[:octicons-person-24: View by Role](by-role.md){ .md-button }
[:octicons-zap-24: Quick Reference](quick-reference.md){ .md-button }

---

## Product

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-task`](create-task.md)** | Product Manager, Engineer, QA | Create tasks with specified type (epic, story, bug, task, etc.) |
| **[`/decompose-task`](decompose-task.md)** | Product Manager, Scrum Master | Decompose large tasks into well-defined subtasks |


---

## Planning

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/refine-task`](refine-task.md)** | Product Manager, Scrum Master | Refine tasks to meet Definition of Ready with story points |
| **[`/create-plan`](create-plan.md)** | Engineer | Create technical implementation design |

---

## Development

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/start-task`](start-task.md)** | Engineer | Begin implementation with branch and context |
| **[`/complete-task`](complete-task.md)** | Engineer | Commit, push, create PR |

---

## Quality

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-test`](create-test.md)** | Engineer, QA | Generate unit tests (adapts for backend/frontend) |
| **[`/review-code`](review-code.md)** | Senior Engineer | AI-assisted code review |

---

## Utilities

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/mcp-status`](mcp-status.md)** | All Roles | Check MCP server authentication status |
| **[`/setup-asdlc`](setup-asdlc.md)** | All Roles | Initialize repository for ASDLC adoption |

---

## Navigation

- **[By Role](by-role.md)** - Commands organized by who uses them
- **[Quick Reference](quick-reference.md)** - Copy-paste cheat sheet
- **[Role Guides](../roles/index.md)** - Brief role overviews

---

## How Commands Work

Commands are markdown files that tell AI agents what to achieve. The AI reads your project structure, issue tracker, implementation plans, and team conventions, then executes contextually - same command, different projects, intelligent adaptation.

Each command aligns with specific [ASDLC](https://asdlc.io) patterns and pillars (Factory Architecture, Standardized Parts, Quality Control); see individual command pages for details.

[See the full product flow →](../index.md#how-it-works)
