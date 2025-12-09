---
title: Product Manager
---

# Product Manager Guide

**Define product vision, create user stories, plan initiatives.**

---

## Your Primary Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-story`](../commands/create-story.md) | Daily | Create user stories with AI-generated acceptance criteria |
| [`/create-epic`](../commands/create-epic.md) | Weekly | Create epics from plan documents |

[See all commands for your role →](../commands/by-role.md#product-manager)

---

## Your Typical Day

```bash
# Morning: Define work
/create-story for new feature requests
/create-story for customer feedback

# Weekly: Plan major initiatives
/create-epic from product-plan.md

# Continuous: Keep backlog groomed and ready
```

---

## How You Work with AI

**Natural language, contextual execution:**

You: `/create-story for user login with email and password`

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
/create-story for [feature description]
```

AI will generate title, description, acceptance criteria, and create it in your issue tracker.

### 2. Plan an Epic

```bash
/create-epic from requirements.md
```

AI reads your plan document and generates epic with child stories.

---

## Best Practices

✅ **Be specific** - Detailed feature descriptions get better stories
✅ **Document** - Write epic plans before `/create-epic`

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

