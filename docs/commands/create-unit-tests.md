---
title: /create-unit-tests
---

# /create-unit-tests

Generate unit tests for code components.

| | |
|---|---|
| **Roles** | All Engineers, QA |
| **Frequency** | Weekly |
| **Prerequisites** | Code to test |

---

## What It Does

Analyzes code, generates comprehensive unit tests with edge cases, mocks dependencies.

---

## Usage

```bash
/create-unit-tests for ClassName
```

---

## Example

```
You: /create-unit-tests for OAuthService

AI:
✓ Analyzing OAuthService...
✓ Identifying test cases...
✓ Creating test file...

Generated: oauth-service.test.ts
  - Happy path tests (3)
  - Error handling (2)
  - Edge cases (2)
  - Mock setup for HTTP client
  Coverage: 95%
```

---

## Command Definition

```markdown
# Write Unit Tests

## Overview
Generate comprehensive unit tests for code components.

## Steps
1. **Analyze code**
   - Read class/function
   - Identify methods
   - Find dependencies
   - Understand behavior

2. **Identify test cases**
   - Happy path scenarios
   - Error conditions
   - Edge cases
   - Boundary conditions

3. **Generate tests**
   - Create test file
   - Write test cases
   - Mock dependencies
   - Add assertions

4. **Verify tests**
   - Run test suite
   - Check coverage
   - Validate behavior

## Test Checklist
- [ ] Code analyzed
- [ ] Test cases identified
- [ ] Tests generated
- [ ] Mocks created
- [ ] Tests passing
- [ ] Coverage adequate
```

**[View Full Command →](../implementations/cursor/commands/create-unit-tests.md)**

---

## Used By

- **[All Engineers](../roles/engineer.md)** - Weekly (with code)
- **[QA Engineer](../roles/qa.md)** - Test automation

---

## Related Commands

**Scale up:** [`/create-integration-tests`](create-integration-tests.md) - Integration tests
**E2E:** [`/create-e2e-tests`](create-e2e-tests.md) - End-to-end tests
**Review:** [`/review-code`](review-code.md) - Code review

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

