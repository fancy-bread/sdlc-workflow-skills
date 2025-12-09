---
title: /create-e2e-tests
---

# /create-e2e-tests

Generate end-to-end tests for user journeys.

| | |
|---|---|
| **Roles** | QA, Senior Engineer |
| **Frequency** | Weekly |
| **Prerequisites** | Complete user flow |

---

## What It Does

Analyzes user journey, generates E2E tests with browser automation, adds assertions.

---

## Usage

```bash
/create-e2e-tests for [user journey description]
```

---

## Example

```
You: /create-e2e-tests for user registration and first login

AI:
✓ Analyzing user journey...
  1. Visit registration page
  2. Fill form
  3. Submit and verify email
  4. Login with new account
  5. See dashboard

✓ Generating E2E test...

Generated: user-registration.e2e.test.ts
  - Navigation tests
  - Form interaction
  - Email verification flow
  - Login validation
  - Dashboard load check
```

---

## Command Definition

```markdown
# Write E2E Tests

## Overview
Generate end-to-end tests for complete user journeys.

## Steps
1. **Analyze journey**
   - Understand user flow
   - Identify steps
   - Map UI interactions
   - Note assertions

2. **Plan test**
   - Define test data
   - Identify selectors
   - Plan assertions
   - Handle waits/timing

3. **Generate test**
   - Create E2E test file
   - Set up browser automation
   - Write step-by-step test
   - Add comprehensive assertions

4. **Verify test**
   - Run E2E test
   - Check reliability
   - Validate assertions
   - Fix flakiness

## E2E Test Checklist
- [ ] Journey analyzed
- [ ] Test planned
- [ ] Test generated
- [ ] Selectors stable
- [ ] Assertions comprehensive
- [ ] Test reliable
```

**[View Full Command →](../../implementations/cursor/commands/quality/create-e2e-tests.md)**

---

## Used By

- **[QA Engineer](../../roles/qa.md)** - Primary (daily)
- **[Senior Engineer](../../roles/engineer.md)** - Critical paths

---

## Related Commands

**Unit:** [`/create-unit-tests`](create-unit-tests.md) - Component tests
**Integration:** [`/create-integration-tests`](create-integration-tests.md) - Integration tests
**Review:** [`/review-code`](review-code.md) - Code review

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

