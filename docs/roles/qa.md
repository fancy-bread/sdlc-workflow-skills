---
title: QA Engineer
---

# QA Engineer Guide

**Verify quality, write tests, catch bugs before production.**

---

## Your Primary Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-test`](../commands/create-test.md) | Daily | Generate unit tests (adapts for backend/frontend) |
| [`/start-task`](../commands/start-task.md) | Occasional | Test automation work |

[See all commands for your role →](../commands/by-role.md#qa-engineer)

---

## Your Typical Day

```bash
# Write tests for new features
/create-test --type=unit for PaymentService
/create-test --type=unit for UserRegistration

# Test automation tasks
/start-task TEST-123
/complete-task TEST-123
```

---

## How You Work with AI

**Intelligent test generation:**

You: `/create-test --type=unit for CheckoutService`

AI:

- Detects backend/frontend context
- Analyzes code structure
- Generates comprehensive unit tests
- Adds appropriate mocks
- Includes edge cases

**Focus on what to test, AI handles how.**

---

## Getting Started

### 1. Write Unit Tests

```bash
/create-test --type=unit for ClassName
```

AI detects backend/frontend context and generates comprehensive unit tests with appropriate mocks and edge cases.

---

## Testing Workflows

### New Feature Testing

```bash
# Understand feature
# Read acceptance criteria

# Write comprehensive tests
/create-test --type=unit for UserService
/create-test --type=unit for PaymentUtils
```

### Bug Investigation

```bash
# Add regression tests
/create-test --type=unit for bug scenario
```

### Coverage Improvement

```bash
# Identify gaps in test coverage
/create-test --type=unit for uncovered code
```

---

## Best Practices

- **Test comprehensively** - Use `/create-test` for unit test coverage
- **Test edge cases** - Focus on boundary conditions and error scenarios
- **Test early** - Write tests before features ship
- **Test continuously** - Add regression tests for every bug


