---
title: /decompose-task
---

# /decompose-task

Decompose a large task (epic or large story) into well-defined, actionable subtasks. This is a critical Scrum planning activity that ensures large work items are properly broken down into sprint-sized tasks.

| | |
|---|---|
| **Frequency** | Per epic/large task (before sprint planning) |
| **Prerequisites** | Large task (epic or story) with sufficient detail |

---

## What It Does

Breaks down large tasks into smaller, manageable subtasks that are:
- Appropriately sized (1-2 days, 1-2 sprint points)
- Well-defined with clear acceptance criteria
- Independent and can be developed standalone
- Ready for team estimation

**Intelligent Analysis:** Before decomposition, the command validates that the task has sufficient information. If information is missing or vague, it asks specific questions rather than creating incomplete subtasks.

---

## ASDLC

- **Patterns**: [The PBI](https://asdlc.io/patterns/the-pbi/), [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Factory Architecture, Quality Control (information-density gate)

---

## Usage

```bash
/decompose-task TASK-123
```

**Examples:**

```bash
# Decompose an epic
/decompose-task EPIC-100

# Decompose a large story
/decompose-task STORY-50
```

---

## Example

```
You: /decompose-task EPIC-200

AI:
✓ MCP status validation passed
✓ Fetching EPIC-200: Add payment processing for subscription plans
✓ Analyzing task information...
⚠ Some information is missing. To ensure a complete breakdown:

1. Which user personas need this? (e.g., new subscribers, existing customers upgrading)
2. What are the acceptance criteria? (e.g., support credit cards, handle refunds, PCI compliance)
3. Are there technical constraints? (e.g., must use Stripe, integrate with existing billing system)

Proceeding with breakdown, but will note assumptions made.

✓ Analyzing task scope...
✓ Generating subtasks...
✓ Validating breakdown quality...
✓ Prioritizing tasks...
✓ Creating 5 subtasks in tracker...
✓ Linking subtasks to parent epic...
✓ Documenting breakdown in EPIC-200 comments...

Breakdown complete. Created 5 subtasks:
- EPIC-200-1: Implement Stripe payment integration
- EPIC-200-2: Create subscription management UI
- EPIC-200-3: Add payment method management
- EPIC-200-4: Implement refund processing
- EPIC-200-5: Write integration tests for payment flow

Breakdown documented in EPIC-200.
```

---

## Key Features

### Intelligent Validation

Before decomposition, validates task information using pattern recognition:
- Detects vague language ("improve", "enhance" without specifics)
- Assesses information density (requires 3+ of: goals, scope, users, criteria, constraints)
- Generates context-aware questions for missing information

### Quality Criteria

Each generated subtask must meet:
- Clear acceptance criteria (3-5 per task)
- Appropriate size (1-2 days, 1-2 sprint points)
- Independence (can be developed standalone)
- User or technical value
- Testability

### Breakdown Patterns

Supports multiple decomposition approaches:
- **Feature-based**: Break into major features
- **User journey-based**: Tasks for each journey step
- **Technical component**: Tasks for each component
- **MVP vs Enhancement**: Separate core from enhancements

---

## When to Use

Use `/decompose-task` when:
- An epic needs to be broken into stories
- A large story needs to be split into smaller tasks
- Work items are too large for a single sprint
- You need to identify dependencies and sequencing
- Preparing for sprint planning

**Best Practice:** Decompose tasks during backlog refinement, before sprint planning, to ensure all work is properly sized and ready for estimation.

---

## Related Commands

- **[`/create-task`](create-task.md)** - Create the parent epic or story before decomposition
- **[`/create-plan`](create-plan.md)** - Create technical plans for decomposed subtasks
- **[`/refine-task`](refine-task.md)** - Refine tasks with story points and acceptance criteria

---

**[View full skill (source)](https://github.com/fancy-bread/sdlc-workflow-skills/blob/main/skills/decompose-task/SKILL.md)**

