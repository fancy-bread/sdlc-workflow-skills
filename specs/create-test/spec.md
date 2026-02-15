# Feature: /create-test (Generate Unit Tests for a Component)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Developers need tests generated from a component and, when available, from the Spec’s Contract scenarios. Manually writing tests is slow and can miss edge cases. `/create-test` locates the component, detects codebase type (backend/frontend) and test framework, optionally uses Gherkin scenarios from `specs/{FEATURE_DOMAIN}/spec.md`, and produces tests following existing project patterns (AAA, naming, placement).

### Architecture

- **Skill location**: `skills/create-test/SKILL.md`. Executed as `/create-test` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `{component}` — class name, file path, or component name (e.g. `OAuthService`, `src/services/payment.ts`, `LoginForm`). Test type: unit (primary), integration, e2e. Framework and naming inferred from config and existing tests.
- **Flow**: (1) If spec exists for the feature domain, read Contract Scenarios and derive test cases from Gherkin; else use code analysis; (2) detect codebase type (backend/frontend) and test framework (Jest, Vitest, pytest, xUnit, etc.) and naming (`*.test.ts`, `*_test.py`, etc.); (3) analyze component: inputs, outputs, side effects, mocks; (4) identify test cases (from Spec scenarios or code paths); (5) generate test file following project conventions; (6) place next to component or in test dir per project layout.
- **Dependencies**: `specs/` (Contract Scenarios), codebase layout, test framework config. **Outbound**: New test files are run by the project’s test runner and by `/complete-task` before commit.

### Anti-Patterns

- **Don’t generate without a locatable component** — If the component cannot be found, STOP and report "Component {component} not found in codebase."
- **Don’t assume test framework** — Detect from config and existing tests; if it cannot be determined, STOP and ask the user to specify or add config.
- **Don’t ignore Spec scenarios** — When `specs/{FEATURE_DOMAIN}/spec.md` exists and has Scenarios, use them as the primary source for test cases; fall back to code only when spec is absent or has no Scenarios.

---

## Contract

### Definition of Done

- [ ] Component exists and is analyzed; feature domain and spec (if present) are considered.
- [ ] Test framework and file-naming convention are identified; if not, user is prompted or creation is blocked.
- [ ] Test file generated using Arrange-Act-Assert (or project equivalent), placed according to project layout, and consistent with existing test patterns.
- [ ] If spec has Scenarios: at least one test case is derived from a Gherkin scenario when the component maps to that spec.
- [ ] `python schemas/validate_all.py` passes when skills are changed.

### Regression Guardrails

- **Component must exist** — No test file is created for a non-existent or unreadable component.
- **Framework and placement** — Follow project test framework and directory conventions; do not invent new patterns that conflict with the codebase.

### Scenarios

**Scenario: Tests generated from Spec scenarios**
- **Given**: `specs/user-auth/spec.md` has Contract Scenarios, component `src/services/OAuthService.ts` maps to `user-auth`
- **When**: The user runs `/create-test OAuthService`
- **Then**: The command reads Contract Scenarios, generates a test file (e.g. `OAuthService.test.ts` or colocated) with at least one test derived from a scenario, and places it per project convention.

**Scenario: Component not found — STOP**
- **Given**: No file or export matches `NonExistentComponent`
- **When**: The user runs `/create-test NonExistentComponent`
- **Then**: The command reports "Component NonExistentComponent not found in codebase." and does not create a test file.
