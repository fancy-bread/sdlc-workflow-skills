---
title: Commands by Role
---

# Commands by Role

Find commands relevant to your role.

[:octicons-list-unordered-24: All Commands](index.md){ .md-button }
[:octicons-zap-24: Quick Reference](quick-reference.md){ .md-button }

---

## Product Manager

**Daily:**
- [`/create-task`](create-task.md) - Create user stories, bugs, and other tasks

**Weekly:**
- [`/create-task`](create-task.md) - Create epics from plan documents
- [`/decompose-task`](decompose-task.md) - Decompose large tasks into subtasks (before sprint planning)
- [`/refine-task`](refine-task.md) - Refine tasks to meet Definition of Ready (during backlog refinement)

[View role guide →](../roles/product-manager.md)

---

## Software Engineer (IC)

**Daily:**
- [`/start-task`](start-task.md) - Begin implementation
- [`/complete-task`](complete-task.md) - Create PR

**Weekly:**
- [`/refine-task`](refine-task.md) - Refine tasks during backlog refinement
- [`/create-plan`](create-plan.md) - Design before coding
- [`/create-test`](create-test.md) - Add test coverage

[View role guide →](../roles/engineer.md)

---

## Senior Engineer

**All IC commands, plus:**

**Daily:**
- [`/review-code`](review-code.md) - Review PRs with AI assistance

**Weekly:**
- [`/create-test`](create-test.md) - Unit test coverage

[View role guide →](../roles/engineer.md)

---

## Staff / Principal Engineer

**All Senior commands, plus:**

**Weekly:**
- [`/create-task`](create-task.md) - Technical initiatives (epics)
- [`/create-plan`](create-plan.md) - System design

**Occasional:**
- Cross-team coordination using most commands
- Architecture and standards work

[View role guide →](../roles/engineer.md)

---

## QA Engineer

**Daily:**
- [`/create-test`](create-test.md) - Unit test coverage

**Weekly:**
- [`/create-test`](create-test.md) - Additional test coverage

**Occasional:**
- [`/start-task`](start-task.md) - Test automation work
- [`/complete-task`](complete-task.md) - Submit test code

[View role guide →](../roles/qa.md)

---

## Command Matrix

| Command | PM | IC | Senior | Staff+ | QA |
|---------|----|----|--------|--------|----|
| `/create-task` | ●●● | ●● | ●● | ●●● | ●● |
| `/decompose-task` | ●● | - | - | ●● | - |
| `/refine-task` | ●● | ●● | ●● | - | - |
| `/create-plan` | - | ●●● | ●●● | ●●● | - |
| `/start-task` | - | ●●● | ●●● | ●●● | ●● |
| `/complete-task` | - | ●●● | ●●● | ●●● | ●● |
| `/create-test` | - | ●●● | ●●● | ●●● | ●●● |
| `/review-code` | - | - | ●●● | ●●● | - |
| `/mcp-status` | ○ | ○ | ○ | ○ | ○ |

**Legend:** ●●● Daily | ●● Weekly | ○ Occasional | - Not typical

---

[:octicons-arrow-left-24: Back to Commands](index.md)
