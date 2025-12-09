---
title: /complete-task
---

# /complete-task

Commit changes, push, create PR, transition issue to review.

| | |
|---|---|
| **Roles** | All Engineers, QA |
| **Frequency** | Daily (every task) |
| **Prerequisites** | Changes complete, tests passing |

---

## What It Does

Commits with conventional commit message, pushes to remote, creates PR with plan summary, transitions issue to "Code Review".

---

## Usage

```bash
/complete-task TASK-123
```

---

## Example

```
You: /complete-task AUTH-456

AI:
✓ Fixing linting errors...
✓ Staging changes...
✓ Creating commit: feat: add OAuth login (AUTH-456)
✓ Pushing to origin/auth-456...
✓ Creating pull request...
✓ Transitioning AUTH-456 to Code Review
✓ PR created: #123
```

---

## Command Definition

Preview of actual command:

```markdown
# Complete Task

## Overview
Commit changes, push to remote, create pull request, and transition issue to "Code Review" status.

## Steps
1. **Prepare commit**
   - Check for linting errors and fix
   - Stage all changes
   - Create conventional commit message
   - Format: `{type}: {description} ({TASK_KEY})`
   - Types: feat, fix, refactor, docs, test, chore

2. **Push changes**
   - Commit staged changes
   - Push to remote branch
   - Wait for automated verification (build, tests, coverage)

3. **Create pull request**
   - Add completed checklist comment to issue
   - Create PR with plan summary
   - Include verification status in PR body
   - Link PR to issue

4. **Update issue**
   - Transition issue to "Code Review" status
   - Add PR link comment to issue

## Completion Checklist
- [ ] Linting errors fixed
- [ ] Changes staged
- [ ] Commit message follows convention
- [ ] Changes committed
- [ ] Pushed to remote
```

**[View Full Command →](../implementations/cursor/commands/complete-task.md)**

---

## Used By

- **[IC Engineer](../roles/engineer.md)** - Every task (primary)
- **[Senior Engineer](../roles/engineer.md)** - Every task
- **[QA Engineer](../roles/qa.md)** - Test automation

---

## Related Commands

**Before:** [`/verify-task`](verify-task.md) - Pre-completion verification
**After:** [`/sync-task`](sync-task.md) - Update after PR merge
**See also:** [`/start-task`](start-task.md) - Begin work

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

