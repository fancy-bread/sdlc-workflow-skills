---
title: Software Engineer
---

# Software Engineer Guide

**Write code, build features, maintain quality.**

---

## Your Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/refine-task`](../commands/refine-task.md) | Per task (backlog refinement) | Refine tasks to meet Definition of Ready |
| [`/create-plan`](../commands/create-plan.md) | Every story | Design implementation |
| [`/start-task`](../commands/start-task.md) | Daily | Begin implementation |
| [`/complete-task`](../commands/complete-task.md) | Daily | Commit, push, create PR |
| [`/create-test`](../commands/create-test.md) | Weekly | Generate unit tests |
| [`/review-code`](../commands/review-code.md) | Daily | AI-assisted code review |

[See all commands →](../commands/by-role.md)

---

## Typical Day

```bash
# Backlog refinement (weekly)
/refine-task PROJ-456

# Plan
/create-plan for PROJ-456

# Build
/start-task PROJ-456
/create-test --type=unit for NewClass

# Ship
/complete-task PROJ-456
```

---

## Getting Started

See the [**Typical Day**](#typical-day) workflow above for a complete example. For detailed setup, see the [Getting Started guide](../getting-started.md).

---

## Best Practices

- **Plan first** - `/create-plan` before coding
- **Test thoroughly** - Unit, integration, and E2E tests
- **Review code** - Use `/review-code` for quality
- **Keep PRs focused** - One story per PR


