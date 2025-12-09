---
title: /review-code
---

# /review-code

AI-assisted code review for PRs.

| | |
|---|---|
| **Roles** | Senior Engineer, Eng Manager, DevOps |
| **Frequency** | Daily |
| **Prerequisites** | Pull request to review |

---

## What It Does

Analyzes PR for quality, security, performance; suggests improvements; checks best practices.

---

## Usage

```bash
/review-code for PR #42
```

---

## Example

```
You: /review-code for PR #123

AI:
✓ Analyzing PR #123: Add OAuth login
✓ Reviewing 8 changed files...

Findings:

✅ Good:
  - Clean architecture
  - Comprehensive tests
  - Good error handling

⚠️ Suggestions:
  1. oauth-service.ts:45 - Add timeout to API call
  2. auth-controller.ts:23 - Extract magic string to constant
  3. Missing integration test for token refresh

🔒 Security:
  - Sensitive data in logs (oauth-service.ts:67)

Overall: Approve with minor changes
```

---

## Command Definition

```markdown
# Review Code

## Overview
AI-assisted code review analyzing quality, security, and best practices.

## Steps
1. **Load PR**
   - Fetch PR details
   - Read changed files
   - Review diff
   - Check tests

2. **Analyze code**
   - Check code quality
   - Review architecture
   - Identify bugs
   - Find security issues
   - Check performance
   - Verify best practices

3. **Review tests**
   - Verify test coverage
   - Check test quality
   - Ensure edge cases covered

4. **Provide feedback**
   - Summarize findings
   - Suggest improvements
   - Highlight concerns
   - Recommend approval/changes

## Review Checklist
- [ ] PR loaded
- [ ] Code analyzed
- [ ] Tests reviewed
- [ ] Security checked
- [ ] Feedback provided
- [ ] Recommendation made
```

**[View Full Command →](../../implementations/cursor/commands/quality/review-code.md)**

---

## Used By

- **[Senior Engineer](../../roles/engineer.md)** - Daily reviews
- **[Staff Engineer](../../roles/engineer.md)** - Architecture review

---

## Related Commands

**Create PR:** [`/complete-task`](../development/complete-task.md) - Submit code
**Verify:** [`/verify-task`](../development/verify-task.md) - Pre-review check
**Tests:** [`/create-unit-tests`](create-unit-tests.md) - Add test coverage

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

