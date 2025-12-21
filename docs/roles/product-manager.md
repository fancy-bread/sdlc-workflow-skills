---
title: Product Manager
---

# Product Manager Guide

**Define product vision, create user stories, plan initiatives.**

---

## Your Primary Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-task`](../commands/create-task.md) | Daily/Weekly | Create user stories, bugs, tasks (daily) or epics from plan documents (weekly) |
| [`/decompose-task`](../commands/decompose-task.md) | Per epic/large task | Decompose large tasks into well-defined subtasks |
| [`/refine-task`](../commands/refine-task.md) | Per task (backlog refinement) | Refine tasks to meet Definition of Ready with story points |

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
/decompose-task EPIC-123

# Backlog refinement: Prepare tasks for sprint planning
/refine-task TASK-123
/refine-task TASK-124
```

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
/decompose-task TASK-123
```

AI analyzes the task and generates well-defined subtasks following INVEST criteria. This is critical for proper sprint planning.

---

## Best Practices

- **Be specific** - Detailed feature descriptions get better stories
- **Document** - Write epic plans before `/create-task --type=epic`
- **Decompose tasks** - Use `/decompose-task` to ensure proper task decomposition before sprint planning
- **Refine backlog** - Use `/refine-task` during backlog refinement to ensure all tasks meet Definition of Ready before sprint planning


