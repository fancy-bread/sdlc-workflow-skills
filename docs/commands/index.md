---
title: Commands Reference
---

# Command Reference

**All 12 commands for AI-assisted development.**

Quick access to every command with usage examples and previews of actual command files.

[:octicons-person-24: View by Role](by-role.md){ .md-button }
[:octicons-zap-24: Quick Reference](quick-reference.md){ .md-button }

---

## Product (2 commands)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-story`](create-story.md)** | Product Manager | Create user stories with AI-generated acceptance criteria |
| **[`/create-epic`](create-epic.md)** | Product Manager | Create epics from plan documents |

---

## Development (5 commands)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-task-plan`](create-task-plan.md)** | Engineer | Create technical implementation design |
| **[`/start-task`](start-task.md)** | Engineer | Begin implementation with branch and context |
| **[`/verify-task`](verify-task.md)** | Engineer | Pre-completion verification |
| **[`/complete-task`](complete-task.md)** | Engineer | Commit, push, create PR |
| **[`/sync-task`](sync-task.md)** | Engineer | Update issue after PR merge |

---

## Quality (4 commands)

| Command | Used By | What It Does |
|---------|---------|--------------|
| **[`/create-unit-tests`](create-unit-tests.md)** | Engineer, QA | Generate unit tests |
| **[`/create-integration-tests`](create-integration-tests.md)** | Engineer, QA | Generate integration tests |
| **[`/create-e2e-tests`](create-e2e-tests.md)** | QA | Generate end-to-end tests |
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
