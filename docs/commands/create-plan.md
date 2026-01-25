---
title: /create-plan
---

# /create-plan

Create a detailed technical implementation plan for a story by analyzing requirements, reviewing the codebase, and generating a structured plan document.

| | |
|---|---|
| **Frequency** | Weekly (every story) |
| **Prerequisites** | Story with acceptance criteria, MCP integrations configured |

---

## What It Does

Fetches story from issue tracker, analyzes codebase for similar implementations and patterns, designs technical approach, and generates a structured plan document with file changes, test strategy, and implementation steps. Posts plan summary to the issue.

---

## Usage

```bash
/create-plan for TASK-123
```

---

## Example

```
You: /create-plan for FB-6

AI:
✓ MCP validation passed
✓ Fetching story FB-6: File watching for workspace commands
✓ Story has 5 acceptance criteria
✓ Analyzing codebase for similar implementations...
✓ Plan saved: .plans/FB-6-file-watching.plan.md
✓ Posting plan summary to issue...
✓ Plan created successfully
```

---

## ASDLC

- **Patterns**: [The Spec](https://asdlc.io/patterns/the-spec/), [The PBI](https://asdlc.io/patterns/the-pbi/)
- **Pillars**: Standardized Parts (spec/plan as State vs Delta)

---

## At a glance

- **Prerequisites:** MCP, story exists, story has 3–5 acceptance criteria.
- **Steps:** Analyze story → analyze codebase → design implementation → generate plan at `.plans/{TASK_KEY}-*.plan.md` → post summary to issue.

---

## Full command (source)

[commands/create-plan.md](https://github.com/fancybread-com/agentic-software-development/blob/main/commands/create-plan.md)

---

## Related Commands

**Execute:** [`/start-task`](start-task.md) — Begin implementation using the plan  
**Complete:** [`/complete-task`](complete-task.md) — Finish and create PR (uses plan summary)

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
