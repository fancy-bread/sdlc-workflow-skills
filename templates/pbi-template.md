# PBI Template

> **ASDLC Pattern**: [The PBI](https://asdlc.io/patterns/the-pbi/)  
> This template defines the 4-part anatomy for Product Backlog Items

---

## Directive

[What to do, with explicit scope boundaries. Not a request—a constrained instruction.]

**Scope:**
- In scope: [What is included]
- Out of scope: [What is explicitly excluded]

**Constraints:**
- [Any technical or business constraints]
- [Dependencies that must be considered]

---

## Context Pointer

See [Spec Blueprint](../../specs/{feature-domain}/spec.md#blueprint) for:
- **Why this feature exists** (business problem and solution rationale)
- **Architecture** (API contracts, data models, dependencies)
- **Anti-Patterns** (forbidden approaches to avoid)

> **Note**: If spec doesn't exist yet, create one using `/create-plan {TASK_KEY}` to establish permanent context.

---

## Verification Pointer

See [Spec Contract](../../specs/{feature-domain}/spec.md#contract) for:
- **Definition of Done** (observable, testable success criteria)
- **Regression Guardrails** (critical invariants that must never break)
- **Test Scenarios** (Gherkin-style Given/When/Then specifications)

> **Note**: These criteria define exactly what "done" looks like for this change.

---

## Refinement Rule

If implementation diverges from Spec:

1. **STOP** and document the divergence
   - Why is the spec no longer accurate?
   - What changed in requirements or understanding?

2. **Update Spec in same commit** as code changes ([Same-Commit Rule](../../specs/README.md#same-commit-rule))
   - Specs are versioned with code
   - Both Blueprint and Contract sections may need updates
   - Include rationale for changes in commit message

3. **Flag for review** if architectural boundaries are affected
   - Security requirements changed
   - Performance targets adjusted
   - API contracts modified
   - Data models evolved

> **Principle**: The Spec is the source of truth. Keep it current with code, not stale.

---

## Usage Notes

### For Agents Creating Issues

When generating PBI descriptions:

1. **Directive**: Extract from user input, task description, or decomposition
   - Be specific about scope boundaries
   - State what's in/out of scope explicitly
   - Include constraints and dependencies

2. **Context Pointer**: 
   - Determine feature domain from labels, epic, or title
   - Check if `specs/{feature-domain}/spec.md` exists
   - If exists: Link to Blueprint section
   - If missing: Use placeholder, warn user to create spec

3. **Verification Pointer**:
   - Link to Contract section of same spec
   - If spec missing: Note that acceptance criteria need to be defined in spec

4. **Refinement Rule**:
   - Use standard protocol (as shown above)
   - Customize if specific review needs (e.g., "flag security team if auth boundaries change")

### For Developers

When working on PBIs:

- **Read Context Pointer first**: Understand architectural constraints before coding
- **Check Verification Pointer**: Know your target before starting
- **Follow Refinement Rule**: Keep spec and code in sync
- **Update spec when behavior changes**: API contracts, data models, quality targets

### Feature Domain Mapping

Feature domains are conceptual groupings (kebab-case):
- `user-authentication` - Auth/login/session management
- `payment-processing` - Payments, billing, invoices
- `notifications` - Email, SMS, push notifications
- `command-audit` - Command structure validation
- `{your-feature}` - Your feature's domain

---

## Related Patterns

- [The Spec](https://asdlc.io/patterns/the-spec/) - Permanent target that PBIs reference
- [Living Specs](https://asdlc.io/practices/living-specs/) - Same-Commit Rule and maintenance
- [The PBI](https://asdlc.io/patterns/the-pbi/) - This template's conceptual foundation

---

**Status**: Active  
**Last Updated**: 2026-01-17  
**Purpose**: Template for ASDLC-compliant PBI descriptions
