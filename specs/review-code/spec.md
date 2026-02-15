# Feature: /review-code (Adversarial Code Review: Spec + Constitution)

> **ASDLC Pattern**: [The Spec](https://asdlc.io/patterns/the-spec/)  
> **Practice Guide**: [Living Specs](https://asdlc.io/practices/living-specs/)  
> **Status**: Active  
> **Last Updated**: 2026-01-17

---

## Blueprint

### Context

Code changes need review against both the **Spec** (functional contract) and the **Constitution** (AGENTS.md). A single agent that implemented the code may miss its own gaps. `/review-code` uses Builder/Critic separation: the Builder gathers PR or branch diff, spec, and AGENTS.md; the Critic runs in a fresh context to validate against both contracts and produce a structured violation report and gate (PASS/FAIL/WARNING).

### Architecture

- **Skill location**: `skills/review-code/SKILL.md`. Executed as `/review-code` when installed in `.cursor/skills/` or `~/.cursor/skills/`.
- **Inputs**: `{PR_KEY}` (e.g. `#12`, `12`) or `{BRANCH_NAME}` (e.g. `feat/FB-39`). `{FEATURE_DOMAIN}` derived from branch, PR, or user to select `specs/{FEATURE_DOMAIN}/spec.md`.
- **Flow**: **[Builder]** (1) Resolve PR or branch; get changed files and diff (`git diff main...{BRANCH}` or GitHub PR diff); (2) determine feature domain and read Spec Blueprint + Contract if `specs/{FEATURE_DOMAIN}/spec.md` exists; (3) read `AGENTS.md` Operational Boundaries (Tier 1 ALWAYS, Tier 2 ASK, Tier 3 NEVER). **[Critic — fresh context]** (4) Invoke Critic with: Spec Blueprint+Contract, Constitution, full diff, file list; (5) Critic outputs structured violations (Spec and Constitution) and gate: PASS / FAIL (Spec CRITICAL or Tier 3) / WARNING (Spec warnings or Tier 2); (6) return violation report and gate to user.
- **MCP**: GitHub (get_pull_request, get_pull_request_files, list_commits, etc.) for PR/branch and diff. Optionally Atlassian to resolve `{TASK_KEY}` from branch for feature context.
- **Dependencies**: `AGENTS.md`, `specs/`. **Outbound**: Report drives rework before merge; aligns with Constitutional Review in `/complete-task`.

### Anti-Patterns

- **Don’t use the same context for Builder and Critic** — The Critic must run in a fresh context with no implementation bias; it only sees contracts and diff.
- **Don’t skip Constitution** — Every review must validate against AGENTS.md Tier 1/2/3, even when no Spec exists.
- **Don’t treat Spec as optional for functional checks** — When a Spec exists, Critic must validate against Blueprint and Contract; if none, note "No Spec — validate against Constitution only."

---

## Contract

### Definition of Done

- [ ] GitHub MCP validated; PR or branch exists and diff is retrievable.
- [ ] Builder: diff, file list, Spec (if exists), and AGENTS.md are gathered and passed to Critic.
- [ ] Critic runs in a fresh context and produces a structured report: violations (Spec + Constitution), severity, location, remediation.
- [ ] Gate: PASS (no critical), FAIL (Spec CRITICAL or Tier 3), WARNING (Spec warnings or Tier 2).
- [ ] `python schemas/validate_all.py` passes when skills are changed.

### Regression Guardrails

- **Critic in fresh context** — The agent that performs the review must not have built the code under review.
- **Dual-contract** — Both Spec (when present) and AGENTS.md must be evaluated; one is not a substitute for the other.

### Scenarios

**Scenario: PR reviewed — PASS**
- **Given**: PR #12 for `feat/FB-39`, `specs/skill-audit/spec.md` exists, diff has no Tier 3 or Spec CRITICAL violations
- **When**: The user runs `/review-code #12`
- **Then**: Builder retrieves diff and spec and Constitution; Critic returns PASS and a report with no blocking violations.

**Scenario: Tier 3 violation — FAIL**
- **Given**: Diff introduces a change that violates AGENTS.md Tier 3 (NEVER)
- **When**: The user runs `/review-code feat/FB-39`
- **Then**: Critic report shows FAIL, Tier 3 violation with description, impact, remediation, and location; user is directed to fix before merge.
