---
title: /create-task
---

# /create-task

Create tasks in the issue tracker with specified type (epic, story, bug, task, etc.).

| | |
|---|---|
| **Frequency** | Daily |
| **Prerequisites** | Feature request, bug report, or plan document |

---

## What It Does

Creates tasks in the issue tracker with type-specific workflows. Supports epics, stories, bugs, tasks, and other task types. Adapts behavior based on the specified type.

**Intelligent Validation:** Before creating a task, the command validates that sufficient information has been provided. If information is missing or vague, it asks specific, type-aware questions rather than creating incomplete tasks.

---

## ASDLC

- **Patterns**: [The PBI](https://asdlc.io/patterns/the-pbi/), [Agent Constitution](https://asdlc.io/patterns/agent-constitution/)
- **Pillars**: Factory Architecture, Standardized Parts

---

## Usage

The command supports two syntax styles:

### Explicit Flag Style (Recommended)
```bash
/create-task --type=[type] [description or source]
```

### Natural Language Style
```bash
/create-task [type] [description or source]
```

**Examples:**

```bash
# Create a story
/create-task --type=story for user authentication
/create-task story for user authentication

# Create an epic from a plan
/create-task --type=epic from phase-one.md
/create-task epic from phase-one.md

# Create a bug
/create-task --type=bug login fails with OAuth
/create-task bug: login fails with OAuth

# Create a task
/create-task --type=task refactor auth service
/create-task task: refactor auth service
```

---

## Examples

### Successful Creation

```
You: /create-task --type=story for user login with email and password

AI:
✓ Parsing command: story type detected
✓ Validating task information...
✓ Sufficient information provided
✓ Analyzing feature request...
✓ Generating story details...
✓ Creating story PROJ-123: User Login
  - Description: Allow users to log in using email and password
  - Acceptance Criteria:
    * User can enter email and password
    * System validates credentials
    * User is redirected to dashboard on success
    * Error message shown on invalid credentials
✓ Story created in "To Do" status
```

### Insufficient Information (Asks for Clarification)

```
You: /create-task story for better UX

AI:
✓ Parsing command: story type detected
✓ Analyzing provided information...

Analysis:
- Description: "better UX" (vague, undefined)
- Missing: user persona, acceptance criteria, value proposition, scope
- Information density: 0/5 elements

⚠ Insufficient information. To create a proper story, I need:

1. Which user persona is this for? (e.g., new users, power users, mobile users)
2. What specific UX problems are we solving? (e.g., confusing navigation, slow load times)
3. What are the acceptance criteria? (e.g., user can complete task in < 30 seconds)
4. What value does this deliver? (e.g., reduce user frustration, increase conversions)

Please provide this information so I can create a well-defined story.
```

### Incomplete Bug Report

```
You: /create-task bug: login broken

AI:
✓ Parsing command: bug type detected
✓ Analyzing provided information...

Analysis:
- Description: "login broken" (too vague)
- Missing: reproduction steps, expected vs actual, environment
- Information density: 1/5 elements

⚠ Insufficient information. To create a proper bug report, I need:

1. What are the reproduction steps? (e.g., go to /login, enter credentials, click submit)
2. What was the expected behavior? (e.g., user should be logged in and redirected)
3. What actually happened? (e.g., error message appears, no redirect)
4. What environment? (e.g., Chrome 120, macOS, production)

Please provide this information so I can create a complete bug report.
```

---

## Supported Task Types

### Epic
High-level initiative that contains multiple stories. Can be created from plan documents.

```bash
/create-task --type=epic from [plan-file.md]
```

**Workflow:**

- Reads plan document (if provided)
- Creates epic with description
- Optionally generates child stories
- Links stories to epic

### Story
User story or feature request with acceptance criteria.

```bash
/create-task --type=story for [feature]
```

**Workflow:**

- Analyzes feature request
- Generates acceptance criteria
- Creates story in tracker
- Links to epic if applicable

### Bug
Defect or issue that needs to be fixed.

```bash
/create-task --type=bug [description]
```

**Workflow:**

- Analyzes bug report
- Documents reproduction steps
- Sets severity and priority
- Links to related tasks if applicable

### Task
Technical work item or chore.

```bash
/create-task --type=task [description]
```

**Workflow:**

- Analyzes technical requirements
- Creates task with description
- Links to epic if applicable

### Other Types
Supports any task type your tracker supports (subtask, improvement, spike, technical-debt, etc.).

---

## Type Detection

The command supports flexible type specification:

**Priority:**

1. `--type=` flag (most explicit)
2. Type as first word before "for", "from", or colon
3. Prompt user if no type specified

**Features:**

- Case-insensitive matching (`--type=BUG` = `--type=bug`)
- Typo detection and suggestions
- Validates against tracker's supported types

---

## Intelligent Information Validation

The command validates task information before creation using type-specific analysis:

**Type-Specific Requirements:**

- **Epic:** Goals, scope, success criteria, major milestones
- **Story:** User persona, acceptance criteria, value proposition
- **Bug:** Reproduction steps, expected vs actual, environment
- **Task:** Technical requirements, scope, success criteria

**Validation Logic:**

- Analyzes information density (0-5 elements)
- Detects vague language patterns
- Generates contextual questions if information is missing
- < 3 elements: STOP and ask (insufficient)
- 3-4 elements: Proceed with caution, note assumptions
- 5+ elements: Proceed confidently

**If information is missing:**

- Command **stops** and asks type-specific questions
- Waits for user response before proceeding
- **Never** creates tasks with incomplete information

## Command Definition

```markdown
# Create Task

## Overview
Create a task in the issue tracker with a specified type (epic, story, bug, task, etc.).
The command adapts its workflow based on the task type.

## Steps
1. Parse command arguments
   - Extract task type from command
   - Extract description or source file
   - Validate task type is supported

2. Gather context (if applicable)
   - Read source file if provided
   - Check for related tasks/epics
   - Review project conventions

3. Validate task information (Intelligent Analysis)
   - Analyze provided information
   - Check type-specific requirements
   - If insufficient: STOP and ask questions
   - If sufficient: Proceed to creation

4. Execute type-specific workflow
   - Follow workflow for specified task type
   - Generate appropriate content
   - Create task in tracker

5. Verify creation
   - Confirm task was created
   - Display task key/ID
   - Provide link to created task
```

**[View full skill (source)](https://github.com/fancy-bread/sdlc-workflow-skills/blob/main/skills/create-task/SKILL.md)**

---

## Related Commands

**For Epics:** [`/decompose-task`](decompose-task.md) - Decompose epic into stories

**For Development:** [`/create-plan`](create-plan.md) - Plan implementation

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

