---
title: Skills Reference
---

# Skills Reference

**SDLC workflow skills (Agent Skills format) for AI-assisted development.**

The canonical skill definitions live in **`skills/`** at the repo root (each skill is `skills/<name>/SKILL.md`). This documentation describes what each skill does. For full instruction content, see the [repository `skills/` folder](https://github.com/fancy-bread/sdlc-workflow-skills/tree/main/skills). Skills are validated with `python schemas/validate.py skills/<name>/SKILL.md` (see [schemas/README](https://github.com/fancy-bread/sdlc-workflow-skills/blob/main/schemas/README.md)).

[:octicons-zap-24: Quick Reference](quick-reference.md){ .md-button }

---

## Product

| Command | What It Does |
|---------|--------------|
| **[`/create-task`](create-task.md)** | Create tasks with specified type (epic, story, bug, task, etc.) |
| **[`/decompose-task`](decompose-task.md)** | Decompose large tasks into well-defined subtasks |


---

## Planning

| Command | What It Does |
|---------|--------------|
| **[`/refine-task`](refine-task.md)** | Refine tasks to meet Definition of Ready with clear acceptance criteria |
| **[`/create-plan`](create-plan.md)** | Create technical implementation design |

---

## Development

| Command | What It Does |
|---------|--------------|
| **[`/start-task`](start-task.md)** | Begin implementation with branch and context |
| **[`/complete-task`](complete-task.md)** | Commit, push, create PR |

---

## Quality

| Command | What It Does |
|---------|--------------|
| **[`/create-test`](create-test.md)** | Generate unit tests (adapts for backend/frontend) |
| **[`/review-code`](review-code.md)** | AI-assisted code review |

---

## Utilities

| Command | What It Does |
|---------|--------------|
| **[`/mcp-status`](mcp-status.md)** | Check MCP server authentication status |
| **[`/setup-asdlc`](setup-asdlc.md)** | Initialize repository for ASDLC adoption |

---

## Navigation

- **[Quick Reference](quick-reference.md)** - Copy-paste cheat sheet

---

## How Skills Work

Skills are Agent Skills (markdown with frontmatter) that tell AI agents what to achieve. The AI reads your project structure, issue tracker, implementation plans, and team conventions, then executes contextually—same skill, different projects, intelligent adaptation.

Each skill aligns with specific [ASDLC](https://asdlc.io) patterns and pillars (Factory Architecture, Standardized Parts, Quality Control); see [Agentic SDLC](https://asdlc.io/concepts/agentic-sdlc/) section 5. Strategic Pillars for details.

[See the full product flow →](../index.md#how-it-works)
