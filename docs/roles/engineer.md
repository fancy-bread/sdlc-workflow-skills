---
title: Software Engineer
---

# Software Engineer Guide

**Write code, build features, maintain quality.**

---

## Your Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-task-plan`](../commands/create-task-plan.md) | Every story | Design implementation |
| [`/start-task`](../commands/start-task.md) | Daily | Begin implementation |
| [`/complete-task`](../commands/complete-task.md) | Daily | Commit, push, create PR |
| [`/verify-task`](../commands/verify-task.md) | As needed | Pre-completion checks |
| [`/sync-task`](../commands/sync-task.md) | After merge | Update issue status |
| [`/create-unit-tests`](../commands/create-unit-tests.md) | Weekly | Generate unit tests |
| [`/create-integration-tests`](../commands/create-integration-tests.md) | Weekly | Generate integration tests |
| [`/review-code`](../commands/review-code.md) | Daily | AI-assisted code review |

[See all commands →](../commands/by-role.md)

---

## Typical Day

```bash
# Plan
/create-task-plan for PROJ-456

# Build
/start-task PROJ-456
/create-unit-tests for NewClass

# Ship
/verify-task PROJ-456
/complete-task PROJ-456

# Close
/sync-task PROJ-456
```

---

## Getting Started

### 1. Plan Implementation

```bash
/create-task-plan for TASK-123
```

### 2. Build

```bash
/start-task TASK-123
```

### 3. Ship

```bash
/complete-task TASK-123
```

---

## Best Practices

- **Plan first** - `/create-task-plan` before coding
- **Test thoroughly** - Unit, integration, and E2E tests
- **Verify before shipping** - `/verify-task` catches issues
- **Review code** - Use `/review-code` for quality
- **Keep PRs focused** - One story per PR

---

## Resources

- **[All Commands](../commands/index.md)** - Complete reference
- **[Quick Reference](../commands/quick-reference.md)** - Cheat sheet
- **[Getting Started](../getting-started.md)** - Setup guide
- **[How It Works](../getting-started.md#how-it-works)** - Core concepts

