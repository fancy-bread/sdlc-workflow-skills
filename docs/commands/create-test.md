---
title: /create-test
---

# /create-test

Generate unit tests for code components. Adapts to backend or frontend and to the project's test framework and conventions.

| | |
|---|---|
| **Prerequisites** | Component exists, test framework detectable |

---

## What It Does

Finds the component, detects codebase type and test framework, reads Spec Contract scenarios when present, and generates unit tests that follow existing patterns (AAA, naming, placement).

---

## Usage

```bash
/create-test --type=unit for AuthService
/create-test for src/services/payment.ts
```

---

## Example

```
You: /create-test --type=unit for OAuthService

AI:
✓ Component found: src/auth/OAuthService.ts
✓ Framework: Jest (existing *.test.ts)
✓ Spec scenarios: 3 (authentication spec)
✓ Generated: src/auth/OAuthService.test.ts
✓ Tests follow AAA and project patterns
```

---

## ASDLC

- **Patterns**: [The Spec](https://asdlc.io/patterns/the-spec/), [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Quality Control, Standardized Parts (Contract scenarios)

---

## At a glance

- **Prerequisites:** Component exists in codebase; test framework and naming detectable (or user specifies).
- **Steps:** Optionally read Spec Contract scenarios → detect codebase type and framework → analyze component → generate tests (from spec scenarios or code) in the right place with project patterns.

---

## Full command (source)

[commands/create-test.md](https://github.com/fancybread-com/agentic-software-development/blob/main/commands/create-test.md)

## Related Commands

**During work:** [`/start-task`](start-task.md), [`/complete-task`](complete-task.md)

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
