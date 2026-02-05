---
title: /complete-task
---

# /complete-task

Commit changes, push to remote, create pull request (optional), and transition issue to "Code Review" status.

| | |
|---|---|
| **Prerequisites** | Branch `{type}/{TASK_KEY}`, tests passing, MCP (Atlassian, GitHub) |

---

## What It Does

Runs Constitutional Review against AGENTS.md, commits with conventional format, pushes, optionally creates a PR with spec/plan summary, and transitions the story to "Code Review".

---

## Usage

```bash
/complete-task TASK-123
```

---

## Example

```
You: /complete-task FB-6

AI:
✓ MCP validation passed
✓ Branch feat/FB-6 verified
✓ Tests passing
✓ Constitutional Review: PASSED
✓ Committed, pushed
✓ PR #42 created (spec + plan in body)
✓ Story transitioned to "Code Review"
```

---

## ASDLC

- **Patterns**: [Constitutional Review](https://asdlc.io/patterns/constitutional-review/), [The Spec](https://asdlc.io/patterns/the-spec/), [The PBI](https://asdlc.io/patterns/the-pbi/), [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Quality Control (Review Gate), Standardized Parts (Constitution)

---

## At a glance

- **Prerequisites:** MCP, branch `{type}/{TASK_KEY}`, tests pass, spec/plan checked.
- **Steps:** Lint and test → Constitutional Review → commit → push → (optional) PR with spec/plan + review report → transition to "Code Review".

---

## Full command (source)

[skills/complete-task/SKILL.md](https://github.com/fancybread-com/sdlc-workflow-skills/blob/main/skills/complete-task/SKILL.md)

## Related Commands

**Before:** [`/start-task`](start-task.md) — Implement the work  
**After:** [`/review-code`](review-code.md) — Review the PR

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
