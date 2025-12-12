---
title: Product Manager
---

# Product Manager Guide

**Define product vision, create user stories, plan initiatives.**

---

## Your Primary Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-task`](../commands/create-task.md) | Daily | Create user stories, bugs, and other tasks with AI-generated content |
| [`/create-task`](../commands/create-task.md) | Weekly | Create epics from plan documents |
| [`/breakdown-tasks`](../commands/breakdown-tasks.md) | Per epic/large task | Break down large tasks into well-defined subtasks |

[See all commands for your role →](../commands/by-role.md#product-manager)

---

## Your Typical Day

```bash
# Morning: Define work
/create-task --type=story for new feature requests
/create-task --type=story for customer feedback
/create-task --type=bug [bug description]

# Weekly: Plan major initiatives
/create-task --type=epic from product-plan.md
/breakdown-tasks EPIC-123

# Continuous: Keep backlog groomed and ready
```

---

## How You Work with AI

**Natural language, contextual execution:**

You: `/create-task --type=story for user login with email and password`

AI:
- Reads your project context
- Generates comprehensive story with acceptance criteria
- Creates in Jira/ADO
- Links to parent epic if applicable

**No scripts. No templates. Just instructions.**

---

## Getting Started

### 1. Create Your First Story

```bash
/create-task --type=story for [feature description]
```

AI will generate title, description, acceptance criteria, and create it in your issue tracker.

### 2. Plan an Epic

```bash
/create-task --type=epic from requirements.md
```

AI reads your plan document and generates epic.

### 3. Break Down Large Task into Subtasks

```bash
/breakdown-tasks TASK-123
```

AI analyzes the task and generates well-defined subtasks following INVEST criteria. This is critical for proper sprint planning.

---

## Best Practices

✅ **Be specific** - Detailed feature descriptions get better stories
✅ **Document** - Write epic plans before `/create-task --type=epic`
✅ **Break down tasks** - Use `/breakdown-tasks` to ensure proper task decomposition before sprint planning

---

## Working with Other Roles

**With Scrum Master:**
- You prioritize, they facilitate

**With Engineers:**
- Review implementation plans
- Clarify acceptance criteria

**With Stakeholders:**
- Translate requests to stories
- Show prioritization rationale

---

## Resources

- **[All Commands](../commands/index.md)** - Complete reference
- **[Quick Reference](../commands/quick-reference.md)** - Cheat sheet
- **[Getting Started](../getting-started.md)** - Setup guide
- **[How It Works](../getting-started.md#how-it-works)** - Core concepts

