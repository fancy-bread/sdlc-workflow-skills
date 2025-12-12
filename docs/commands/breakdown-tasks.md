---
title: /breakdown-tasks
---

# /breakdown-tasks

Break down a large task (epic or large story) into well-defined, actionable tasks. Critical Scrum planning activity.

| | |
|---|---|
| **Roles** | Product Manager, Scrum Master |
| **Frequency** | Per epic/large task (before sprint planning) |
| **Prerequisites** | Epic or large task with clear goals and scope |

---

## What It Does

Reads a large task (epic or large story), analyzes its scope, and generates well-defined tasks following INVEST criteria. Creates tasks in the tracker and links them to the parent task.

---

## Usage

```bash
/breakdown-tasks TASK-123
```

---

## Example

### Successful Breakdown

```
You: /breakdown-tasks PROJ-100

AI:
✓ Reading task PROJ-100: User Authentication System
✓ Validating task information...
✓ Task has sufficient detail
✓ Analyzing scope...
✓ Identifying work areas...
✓ Generating tasks...

Created 6 tasks:
  - PROJ-101: As a user, I want to register with email
  - PROJ-102: As a user, I want to login with credentials
  - PROJ-103: As a user, I want to reset my password
  - PROJ-104: As a user, I want OAuth login options
  - PROJ-105: As a user, I want two-factor authentication
  - PROJ-106: As a user, I want to manage my session

✓ Tasks linked to parent PROJ-100
✓ Prioritized and sequenced
✓ Ready for team estimation
```

### Insufficient Information (Intelligent Detection)

```
You: /breakdown-tasks EPIC-50

AI:
✓ Reading EPIC-50: Improve User Experience

Analysis:
- Description: 8 words (insufficient length)
- Vague terms detected: "improve", "user experience" (undefined)
- Missing: scope, personas, success criteria, constraints
- Information density: 1/5 elements

⚠ Insufficient information detected. To create a proper breakdown, I need:

1. What specific user experience problems are we solving? (e.g., slow load times, confusing navigation, mobile usability)
2. Which user personas are affected? (e.g., new users, power users, mobile users)
3. What are the success criteria? (e.g., reduce bounce rate by 20%, increase task completion by 30%)
4. What's in scope vs out of scope? (e.g., only mobile app, or also web?)

Please provide this information so I can generate well-defined tasks.
```

### Partially Defined (Proceeds with Caution)

```
You: /breakdown-tasks EPIC-200

AI:
✓ Reading EPIC-200: Add payment processing for subscription plans

Analysis:
- Description: Clear action and object
- Missing: user context, success criteria, technical constraints
- Information density: 2/5 elements

⚠ Some information is missing. To ensure a complete breakdown:

1. Which user personas need this? (e.g., new subscribers, existing customers upgrading)
2. What are the acceptance criteria? (e.g., support credit cards, handle refunds, PCI compliance)
3. Are there technical constraints? (e.g., must use Stripe, integrate with existing billing system)

Proceeding with breakdown, but will note assumptions made.
```

---

## Why This Matters

Task breakdown is often rushed or skipped, leading to:

- Vague tasks that confuse developers
- Tasks that are too large for sprints
- Missing dependencies and sequencing
- Poor sprint planning

This command ensures proper task decomposition with:

- **Information validation** - Asks for clarification if task lacks detail
- INVEST-compliant tasks
- Clear acceptance criteria
- Proper prioritization
- Dependency identification

## Intelligent Information Validation

The command uses intelligent analysis to validate task information:

**Pattern Recognition:**

- Detects vague language ("improve", "enhance" without specifics)
- Analyzes information density (description length, detail level)
- Identifies missing critical elements (scope, users, criteria, constraints)
- Scores completeness (0-5 elements, needs 3+ to proceed)

**Smart Question Generation:**

- Questions are contextual to task type (user-facing vs technical)
- Focuses on critical gaps, not nice-to-haves
- Generates 3-5 specific, actionable questions
- Prioritizes most important questions first

**Decision Logic:**

- **< 3 elements present**: STOP and ask (insufficient)
- **3-4 elements present**: Proceed with caution, note assumptions
- **5+ elements present**: Proceed confidently

**If information is missing:**

- Command **stops** and asks specific, contextual questions
- Waits for user response before proceeding
- **Never** makes assumptions or proceeds with incomplete information

---

## Command Definition

```markdown
# Breakdown Tasks

## Overview
Break down a large task into well-defined, actionable tasks.

## Steps
1. Read the task
2. Validate task information
   - Check if task has sufficient detail
   - If insufficient, ask user for clarification
   - Do NOT proceed with assumptions
3. Analyze task scope
4. Validate breakdown quality
5. Generate subtasks
6. Prioritize tasks
7. Create tasks in tracker
8. Document breakdown
```

**[View Full Command →](../implementations/cursor/commands/breakdown-tasks.md)**

---

## Used By

- **[Product Manager](../roles/product-manager.md)** - Epic refinement
- **[Scrum Master](../roles/index.md)** - Sprint planning preparation

---

## Related Commands

**Before:** [`/create-task --type=epic`](create-task.md) - Create epic first
**After:** Team estimation and sprint planning

---

## INVEST Criteria

Tasks generated follow INVEST:

- **I**ndependent - Can be developed in any order
- **N**egotiable - Details can be refined
- **V**aluable - Delivers user value
- **E**stimable - Can be sized
- **S**mall - Completable in a sprint
- **T**estable - Has clear acceptance criteria

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

