---
title: /create-integration-tests
---

# /create-integration-tests

Generate integration tests for component interactions.

| | |
|---|---|
| **Roles** | Engineers, QA |
| **Frequency** | Weekly |
| **Prerequisites** | Integrated components |

---

## What It Does

Analyzes component interactions, generates tests for integration points, sets up test data.

---

## Usage

```bash
/create-integration-tests for FeatureName
```

---

## Example

```
You: /create-integration-tests for OAuth authentication

AI:
✓ Analyzing OAuth flow...
✓ Identifying integration points...
  - OAuth provider API
  - User database
  - Session storage

✓ Creating integration tests...

Generated: oauth-integration.test.ts
  - Full OAuth flow test
  - Token refresh test
  - Database integration
  - Session handling
```

---

## Command Definition

```markdown
# Write Integration Tests

## Overview
Generate tests for component interactions and integrations.

## Steps
1. **Analyze integrations**
   - Identify components
   - Map interactions
   - Find integration points
   - Review data flow

2. **Plan test scenarios**
   - End-to-end flows
   - Data persistence
   - External APIs
   - Error propagation

3. **Generate tests**
   - Create test file
   - Set up test data
   - Write integration tests
   - Handle cleanup

4. **Verify integrations**
   - Run tests
   - Verify behavior
   - Check data integrity

## Integration Test Checklist
- [ ] Integrations analyzed
- [ ] Scenarios identified
- [ ] Tests generated
- [ ] Test data setup
- [ ] Tests passing
- [ ] Cleanup working
```

**[View Full Command →](../../implementations/cursor/commands/quality/create-integration-tests.md)**

---

## Used By

- **[All Engineers](../../roles/engineer.md)** - Complex features
- **[Senior Engineer](../../roles/engineer.md)** - System integration
- **[QA Engineer](../../roles/qa.md)** - Primary

---

## Related Commands

**Unit:** [`/create-unit-tests`](create-unit-tests.md) - Component tests
**E2E:** [`/create-e2e-tests`](create-e2e-tests.md) - User journey tests
**Review:** [`/review-code`](review-code.md) - Code review

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

