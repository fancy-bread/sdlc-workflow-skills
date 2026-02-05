# PBI 4-part anatomy

Use this structure when generating **Stories** and **Epics**. Populate from user input and `{feature-domain}`; link to `specs/{feature-domain}/spec.md` (Blueprint and Contract). If spec is missing, use placeholders and warn.

---

## 1. Directive

What to do, with explicit scope boundaries (constrained instruction, not a request).

- **Scope:** In scope: [included]; Out of scope: [excluded].
- **Constraints:** Technical/business constraints; dependencies.

## 2. Context Pointer

See `specs/{feature-domain}/spec.md#blueprint` for: Why, Architecture, Anti-Patterns.

If spec missing: placeholder + note to create via `/create-plan {TASK_KEY}`.

## 3. Verification Pointer

See `specs/{feature-domain}/spec.md#contract` for: DoD, Regression Guardrails, Test Scenarios.

If spec missing: placeholder; note that AC must be defined in spec.

## 4. Refinement Rule

If implementation diverges from Spec: STOP, document divergence; update spec in same commit (Same-Commit Rule); flag for review if architectural boundaries affected.
