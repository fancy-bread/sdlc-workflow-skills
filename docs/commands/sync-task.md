---
title: /sync-task
---

# /sync-task

Update issue tracker after PR merge.

| | |
|---|---|
| **Roles** | All Engineers |
| **Frequency** | Weekly (after PR merge) |
| **Prerequisites** | PR merged to main |

---

## What It Does

Transitions issue to "Done", adds completion comment, closes issue.

---

## Usage

```bash
/sync-task TASK-123
```

---

## Example

```
You: /sync-task AUTH-456

AI:
✓ Verifying PR merged...
✓ Transitioning AUTH-456 to Done
✓ Adding completion comment...
✓ Closing issue
✓ Task complete!
```

---

## Command Definition

```markdown
# Sync Task

## Overview
Update issue tracker after PR is merged to main branch.

## Steps
1. **Verify PR merged**
   - Check PR status
   - Confirm merge to main
   - Verify CI/CD success

2. **Update issue**
   - Transition to "Done" status
   - Add completion comment
   - Close issue

3. **Cleanup**
   - Note completion time
   - Update project metrics

## Sync Checklist
- [ ] PR merge confirmed
- [ ] Issue transitioned to Done
- [ ] Completion comment added
- [ ] Issue closed
```

**[View Full Command →](../../implementations/cursor/commands/development/sync-task.md)**

---

## Used By

- **[All Engineers](../../roles/engineer.md)** - After PR merge

---

## Related Commands

**Before:** [`/complete-task`](complete-task.md) - Create PR
**See also:** [`/start-task`](start-task.md) - Begin next task

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

