---
title: Software Engineer
---

# Software Engineer Guide

**Write code, build features, maintain quality.**

---

## Your Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-plan`](../commands/create-plan.md) | Every story | Design implementation |
| [`/start-task`](../commands/start-task.md) | Daily | Begin implementation |
| [`/complete-task`](../commands/complete-task.md) | Daily | Commit, push, create PR |
| [`/create-test`](../commands/create-test.md) | Weekly | Generate unit tests |
| [`/review-code`](../commands/review-code.md) | Daily | AI-assisted code review |

[See all commands →](../commands/by-role.md)

---

## Typical Day

```bash
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

### 1. Plan Implementation

```bash
/create-plan for TASK-123
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

- **Plan first** - `/create-plan` before coding
- **Test thoroughly** - Unit, integration, and E2E tests
- **Review code** - Use `/review-code` for quality
- **Keep PRs focused** - One story per PR

---

## Resources

- **[All Commands](../commands/index.md)** - Complete reference
- **[Quick Reference](../commands/quick-reference.md)** - Cheat sheet
- **[Getting Started](../getting-started.md)** - Setup guide
- **[How It Works](../getting-started.md#how-it-works)** - Core concepts

