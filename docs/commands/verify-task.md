---
title: /verify-task
---

# /verify-task

Pre-completion verification to catch issues before PR.

| | |
|---|---|
| **Roles** | All Engineers, QA |
| **Frequency** | Weekly (before completing tasks) |
| **Prerequisites** | Task implementation complete |

---

## What It Does

Runs tests, checks linting, verifies acceptance criteria met, suggests fixes.

---

## Usage

```bash
/verify-task TASK-123
```

---

## Example

```
You: /verify-task AUTH-456

AI:
✓ Running tests... All passed
✓ Checking linting... 2 issues found
✓ Verifying acceptance criteria...
  ✓ Email/password login works
  ✓ Error handling present
  ✗ "Forgot password" link missing

Fix needed:
- Add forgot password link to login form
- Fix linting: remove unused imports
```

---

## Command Definition

```markdown
# Verify Task

## Overview
Pre-completion verification to ensure task meets all requirements.

## Steps
1. **Run tests**
   - Execute full test suite
   - Verify all tests pass
   - Check coverage thresholds

2. **Check code quality**
   - Run linter
   - Check formatting
   - Verify no warnings

3. **Verify acceptance criteria**
   - Read story acceptance criteria
   - Test each criterion
   - Document any gaps

4. **Report findings**
   - List what passes
   - Identify issues
   - Suggest fixes
   - Estimate completion

## Verification Checklist
- [ ] All tests passing
- [ ] No linting errors
- [ ] Code formatted
- [ ] Acceptance criteria met
- [ ] Ready for PR
```

**[View Full Command →](../implementations/cursor/commands/verify-task.md)**

---

## Used By

- **[All Engineers](../roles/engineer.md)** - Before completing tasks
- **[QA Engineer](../roles/qa.md)** - Verification workflow

---

## Related Commands

**Before:** [`/start-task`](start-task.md) - Begin work
**After:** [`/complete-task`](complete-task.md) - Create PR
**Test:** [`/create-unit-tests`](create-unit-tests.md) - Add tests

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

