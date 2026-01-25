---
title: /review-code
---

# /review-code

Perform adversarial AI-assisted code review on a pull request or branch using Builder/Critic separation and dual-contract validation (Spec + Constitution).

| | |
|---|---|
| **Prerequisites** | GitHub MCP; PR or branch exists and is accessible |

---

## What It Does

Builder gathers diff, changed files, Spec (if exists), and AGENTS.md Constitution. A fresh Critic session evaluates against both; produces a PASS/FAIL/WARNING report with violations, impact, and remediation.

---

## Usage

```bash
/review-code for PR #42
/review-code for feat/FB-12
```

---

## Example

```
You: /review-code for PR #42

AI (Builder): Retrieving PR #42, changed files, specs/user-auth/spec.md, AGENTS.md...
AI (Critic): Validating against Spec Contract and Constitution...
## Review: WARNING
- Tier 2: ASK — High-risk Logger usage in auth; recommend interface.
- Spec: Scenario "invalid token" not covered by tests.
```

---

## ASDLC

- **Patterns**: [Adversarial Code Review](https://asdlc.io/patterns/adversarial-code-review/), [Constitutional Review](https://asdlc.io/patterns/constitutional-review/), [The Spec](https://asdlc.io/patterns/the-spec/)
- **Pillars**: Quality Control (Review Gate, dual-contract validation)

---

## At a glance

- **Prerequisites:** GitHub MCP; PR ({PR_KEY}) or branch ({BRANCH_NAME}) exists and is readable.
- **Steps:** Builder: get diff and files → resolve feature domain → read Spec (if any) and Constitution → Critic in a fresh context: validate against Spec + Constitution → output structured report (PASS/FAIL/WARNING).

---

## Full command (source)

[commands/review-code.md](https://github.com/fancybread-com/agentic-software-development/blob/main/commands/review-code.md)

## Related Commands

**After:** [`/complete-task`](complete-task.md) — Creates the PR that is reviewed

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
