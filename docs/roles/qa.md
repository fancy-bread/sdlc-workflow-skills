---
title: QA Engineer
---

# QA Engineer Guide

**Verify quality, write tests, catch bugs before production.**

---

## Your Primary Commands

| Command | Frequency | What It Does |
|---------|-----------|--------------|
| [`/create-e2e-tests`](../commands/create-e2e-tests.md) | Daily | Generate end-to-end tests |
| [`/create-integration-tests`](../commands/create-integration-tests.md) | Weekly | Generate integration tests |
| [`/create-unit-tests`](../commands/create-unit-tests.md) | Weekly | Generate unit tests |
| [`/start-task`](../commands/start-task.md) | Occasional | Test automation work |

[See all commands for your role →](../commands/by-role.md#qa-engineer)

---

## Your Typical Day

```bash
# Write tests for new features
/create-e2e-tests for user registration flow
/create-integration-tests for payment processing
/create-unit-tests for edge cases

# Test automation tasks
/start-task TEST-123
/complete-task TEST-123
```

---

## How You Work with AI

**Intelligent test generation:**

You: `/create-e2e-tests for checkout flow`

AI:
- Analyzes user journey
- Generates complete E2E test
- Handles browser automation
- Adds comprehensive assertions

**Focus on what to test, AI handles how.**

---

## Getting Started

### 1. Write End-to-End Tests

```bash
/create-e2e-tests for [user journey]
```

AI generates complete E2E test with browser automation.

### 2. Write Integration Tests

```bash
/create-integration-tests for FeatureName
```

AI identifies integration points and generates tests.

### 3. Write Unit Tests

```bash
/create-unit-tests for ClassName
```

AI generates comprehensive unit tests with edge cases.

---

## Testing Workflows

### New Feature Testing

```bash
# Understand feature
# Read acceptance criteria

# Write comprehensive tests
/create-e2e-tests for user flow
/create-integration-tests for backend
/create-unit-tests for utilities
```

### Bug Investigation

```bash
# Reproduce bug
/create-e2e-tests to reproduce bug

# Add regression tests
/create-unit-tests for bug scenario
```

### Coverage Improvement

```bash
# Identify gaps in test coverage
/create-unit-tests for uncovered code
/create-integration-tests for missing scenarios
/create-e2e-tests for untested user flows
```

---

## Best Practices

- **Test user journeys** - Focus on `/create-e2e-tests` for critical paths
- **Test integrations** - Use `/create-integration-tests` for system boundaries
- **Test edge cases** - Use `/create-unit-tests` for comprehensive coverage
- **Test early** - Write tests before features ship
- **Test continuously** - Add regression tests for every bug

---

## Working with Other Roles

**With Engineers:**
- Review PRs for testability
- Pair on test strategy
- Share coverage reports

**With Product Manager:**
- Verify acceptance criteria met
- Report quality metrics
- Identify edge cases

**With DevOps:**
- Integrate tests in CI/CD
- Monitor production issues
- Performance testing

---

## Resources

- **[All Commands](../commands/index.md)** - Complete reference
- **[Quick Reference](../commands/quick-reference.md)** - Cheat sheet
- **[Getting Started](../getting-started.md)** - Setup guide
- **[How It Works](../getting-started.md#how-it-works)** - Core concepts

