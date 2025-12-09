---
title: /create-task-plan
---

# /create-task-plan

Create technical implementation design before coding.

| | |
|---|---|
| **Roles** | All Engineers |
| **Frequency** | Weekly (every story) |
| **Prerequisites** | Story with acceptance criteria |

---

## What It Does

Reads story, analyzes codebase, generates detailed implementation plan with file changes, test strategy.

---

## Usage

```bash
/create-task-plan for TASK-123
```

---

## Example

```
You: /create-task-plan for AUTH-456

AI:
✓ Reading AUTH-456: Add OAuth login
✓ Analyzing codebase structure...
✓ Identifying affected files...
✓ Designing implementation...
✓ Plan saved: .plans/AUTH-456-oauth-login.plan.md

Plan includes:
- 3 new files, 5 modified files
- Test strategy (unit + integration)
- Database migrations needed
- API changes documented
```

---

## Command Definition

```markdown
# Generate Implementation Plan

## Overview
Create a detailed technical implementation plan for a story.

## Steps
1. **Analyze story**
   - Read story description
   - Parse acceptance criteria
   - Identify technical requirements

2. **Analyze codebase**
   - Understand existing architecture
   - Identify affected components
   - Find similar implementations
   - Review patterns and conventions

3. **Design implementation**
   - Break down into subtasks
   - Identify files to create/modify
   - Plan database changes
   - Design API changes
   - Plan test strategy

4. **Generate plan document**
   - Write plan to `.plans/{TASK_KEY}-*.plan.md`
   - Include file-by-file changes
   - Document test approach
   - Add verification checklist
   - Post plan summary to issue

## Planning Checklist
- [ ] Story analyzed
- [ ] Codebase reviewed
- [ ] Architecture understood
- [ ] Files identified
- [ ] Tests planned
- [ ] Plan document created
```

**[View Full Command →](../../implementations/cursor/commands/development/create-task-plan.md)**

---

## Used By

- **[IC Engineer](../../roles/engineer.md)** - Every story
- **[Senior Engineer](../../roles/engineer.md)** - Complex features
- **[Staff Engineer](../../roles/engineer.md)** - System design

---

## Related Commands

**Execute:** [`/start-task`](start-task.md) - Begin implementation
**Verify:** [`/verify-task`](verify-task.md) - Pre-completion check

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

