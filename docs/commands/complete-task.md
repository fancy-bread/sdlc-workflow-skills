---
title: /complete-task
---

# /complete-task

Commit changes, push to remote, create pull request, and transition issue to "Code Review" status.

| | |
|---|---|
| **Roles** | All Engineers, QA |
| **Frequency** | Daily (every task) |
| **Prerequisites** | Changes complete, tests passing locally, branch matches format |

---

## What It Does

Validates prerequisites (MCP status, branch format, tests), commits with conventional commit format, pushes to remote, creates PR with extracted plan summary, and transitions issue to "Code Review". CI/CD runs automatically as a gate after PR creation.

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
✓ MCP status validation passed
✓ Current branch: feat/FB-6
✓ All tests passing locally
✓ Plan file found: .plans/FB-6-file-watching.plan.md
✓ Fixing linting errors...
✓ Staging changes...
✓ Creating commit: feat: add file watching (FB-6)
✓ Pushing to origin/feat/FB-6...
✓ Getting commit SHA...
✓ Extracting plan summary...
✓ Creating pull request...
✓ PR created: #42
✓ CI/CD checks running (as PR gate)
✓ Adding completed checklist to issue...
✓ Transitioning FB-6 to Code Review
✓ Issue updated successfully
```

---

## Definitions

- **{TASK_KEY}**: Story/Issue ID from the issue tracker (e.g., `FB-6`, `PROJ-123`, `KAN-42`)
- **Branch Name Format**: Use short format `{type}/{TASK_KEY}` (e.g., `feat/FB-6`, `fix/PROJ-123`)
  - Short format is recommended: `feat/FB-6` (not `feat/FB-6-file-watching-workspace-commands`)
  - **Important**: Be consistent within a project - use the same format for all branches
- **Plan Summary**: Content extracted from `.plans/{TASK_KEY}-*.plan.md` for PR body
  - Extracts: Story, Context, Scope, Acceptance Criteria, Implementation Steps summary
- **CI/CD as PR Gate**: CI/CD runs automatically after PR creation. Local tests must pass before creating PR.

---

## Prerequisites

Before proceeding, the command verifies:

1. **MCP Status Validation**: All MCP servers (Atlassian, GitHub) are connected and authorized
2. **Branch Verification**: Current branch matches format `{type}/{TASK_KEY}`
3. **Test Verification**: All tests pass locally (required before committing)
4. **Plan File**: Plan document exists at `.plans/{TASK_KEY}-*.plan.md` (uses most recently modified if multiple match)

---

## Steps

1. **Prepare commit**
   - Fix linting errors (STOP if cannot be fixed automatically)
   - Run all tests locally (STOP if any fail)
   - Stage all changes
   - Create conventional commit message: `{type}: {description} ({TASK_KEY})`

2. **Commit and push changes**
   - Commit with conventional format
   - Push to remote branch (STOP if push fails)
   - Get latest commit SHA for CI/CD tracking

3. **Create pull request**
   - Extract plan summary sections (Story, Context, Scope, Acceptance Criteria, Implementation Steps)
   - Check if PR already exists (update if found)
   - Create completed checklist comment on issue
   - Create PR with plan summary in body
   - Note: CI/CD will run automatically as a gate on the PR

4. **Update issue**
   - Add PR link as comment to issue
   - Transition issue to "Code Review" status
   - Verify transition succeeded

---

## Tools

The command uses explicit MCP and filesystem tools:

- **MCP Atlassian**: Get issue, get transitions, transition issue, add comments (with CloudId acquisition guidance)
- **MCP GitHub**: List branches, get commit, list commits, create PR, get PR status
- **Filesystem**: Read plan files, check linting
- **Terminal**: Git commands (status, branch, add, commit, push, rev-parse), test commands, lint commands

---

## Key Features

- **Prerequisite validation**: MCP status, branch format, tests, plan file
- **Plan summary extraction**: Automatically extracts key sections from plan for PR body
- **CI/CD as gate**: Creates PR first, then CI/CD runs automatically (local tests are prerequisite)
- **Error handling**: Clear STOP conditions with specific error messages
- **PR conflict detection**: Checks for existing PRs before creating
- **Short branch format**: Consistent `{type}/{TASK_KEY}` naming

---

## Command Definition

Preview of actual command:

```markdown
# Complete Task

## Overview
Commit changes, push to remote, create pull request, and transition issue to "Code Review" status.

## Definitions
- {TASK_KEY}: Story/Issue ID
- Branch Name Format: Short format {type}/{TASK_KEY}
- Plan Summary: Extracted sections from plan file
- CI/CD as PR Gate: Runs automatically after PR creation

## Prerequisites
- MCP status validation
- Branch format verification
- Local tests passing
- Plan file exists

## Steps
1. Prepare commit (linting, tests, staging)
2. Commit and push changes
3. Create pull request (with plan summary extraction)
4. Update issue (PR link, transition to Code Review)

## Tools
- MCP Tools (Atlassian, GitHub)
- Filesystem Tools
- Terminal Tools

## Guidance
- Role: Software engineer
- Instruction: Execute completion workflow
- Context: Task tracking, plan documents, CI/CD gates
- Examples: PR titles, PR bodies, completed checklists
- Constraints: Tests must pass, conventional commits, branch naming
- Output: Committed changes, PR, issue transition
```

**[View Full Command →](../implementations/cursor/commands/complete-task.md)**

---

## Used By

- **[IC Engineer](../roles/engineer.md)** - Every task (primary)
- **[Senior Engineer](../roles/engineer.md)** - Every task
- **[QA Engineer](../roles/qa.md)** - Test automation

---

## Related Commands

**Before:** [`/start-task`](start-task.md) - Begin implementation
**See also:** [`/create-plan`](create-plan.md) - Create implementation plan

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
