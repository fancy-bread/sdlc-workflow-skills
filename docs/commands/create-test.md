---
title: /create-test
---

# /create-test

Generate unit tests for code components. Automatically adapts for backend or frontend code.

| | |
|---|---|
| **Roles** | All Engineers, QA |
| **Frequency** | Weekly |
| **Prerequisites** | Code to test |

---

## What It Does

Analyzes code, detects backend vs frontend context, generates comprehensive unit tests with appropriate mocking strategies.

---

## Usage

```bash
/create-test --type=unit for [component]
```

---

## Example

```
You: /create-test --type=unit for OAuthService

AI:
✓ Detected: Backend (Node.js/TypeScript)
✓ Test framework: Jest
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

## Backend vs Frontend Adaptation

The command automatically detects your codebase type and adapts:

**Backend:**
- Mocks external services, databases, APIs
- Tests business logic and data transformations
- Focuses on service methods and API endpoints

**Frontend:**
- Mocks components, hooks, browser APIs
- Tests user interactions and state management
- Focuses on component rendering and behavior

---

## Command Definition

```markdown
# Create Test

## Overview
Generate unit tests for code components. Adapts to backend or frontend automatically.

## Steps
1. Detect codebase type (backend/frontend)
2. Analyze code to test
3. Identify test cases
4. Generate test code with appropriate mocks
5. Create test file
6. Run tests and verify
```

**[View Full Command →](../implementations/cursor/commands/create-test.md)**

---

## Used By

- **[All Engineers](../roles/engineer.md)** - Weekly (with code)
- **[QA Engineer](../roles/qa.md)** - Test automation

---

## Related Commands

**Review:** [`/review-code`](review-code.md) - Code review

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

