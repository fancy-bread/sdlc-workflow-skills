---
title: /start-task
---

# /start-task

Begin implementation of a task with AI assistance.

| | |
|---|---|
| **Roles** | All Engineers, QA |
| **Frequency** | Daily (every task) |
| **Prerequisites** | Implementation plan, story in "In Progress" |

---

## What It Does

Creates feature branch, reads implementation plan, starts implementing code with tests.

---

## Usage

```bash
/start-task TASK-123
```

---

## Example

```
You: /start-task AUTH-456

AI:
✓ Story AUTH-456: Add OAuth login
✓ Plan: .plans/AUTH-456-oauth-login.plan.md
✓ Creating branch: auth-456
✓ Reading plan...
✓ Implementing OAuth service...
✓ Writing tests...
✓ Ready for your review
```

---

## Command Definition

Preview of actual command:

```markdown
# Start Task

## Overview
Begin development on a task with proper setup and pre-flight checks.

## Steps
1. **Pre-flight checks**
   - Verify integrations are authorized
   - Read plan from `.plans/{TASK_KEY}-*.plan.md`
   - Verify story is in "In Progress"
   - Confirm story is assigned to current user

2. **Set up development environment**
   - Create feature branch `{task-key}`
   - Check out branch locally
   - Add work checklist comment to issue

3. **Begin implementation**
   - Review plan and understand requirements
   - Analyze existing codebase
   - Start implementing changes
   - Create/modify files per plan
   - Write tests alongside code

## Pre-flight Checklist
- [ ] All integrations authorized
- [ ] Plan file exists and is readable
- [ ] Story status is "In Progress"
- [ ] Story assigned to current user
- [ ] Feature branch created
- [ ] Branch checked out locally
- [ ] Work checklist posted to issue
```

**[View Full Command →](../implementations/cursor/commands/start-task.md)**

---

## Used By

- **[IC Engineer](../roles/engineer.md)** - Every task (primary)
- **[Senior Engineer](../roles/engineer.md)** - Complex features
- **[QA Engineer](../roles/qa.md)** - Test automation work

---

## Related Commands

**Before:** [`/create-plan`](create-plan.md) - Create plan first
**After:** [`/complete-task`](complete-task.md) - Finish and create PR

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

