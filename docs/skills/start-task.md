---
title: /start-task
---

# /start-task

Begin implementation of a task with proper setup, pre-flight checks, and standardized workflow.

| | |
|---|---|
| **Frequency** | Daily (every task) |
| **Prerequisites** | Implementation plan, story in "In Progress" |

---

## What It Does

Performs MCP validation, reads implementation plan, creates feature branch with standardized naming, automatically transitions story to "In Progress" if needed, and begins implementing code with tests following the plan.

---

## Usage

```bash
/start-task TASK-123
```

---

## Example

```
You: /start-task FB-6

AI:
✓ MCP status validation passed
✓ Story FB-6: File watching for workspace commands
✓ Plan: .plans/FB-6-file-watching.plan.md
✓ Story transitioned to "In Progress"
✓ Creating branch: feat/FB-6
✓ Branch created and checked out
✓ Work checklist posted to issue
✓ Reading plan...
✓ Analyzing codebase...
✓ Implementing file watching service...
✓ Writing tests...
✓ Committed: feat: add file watching (FB-6)
✓ Ready for continued development
```

---

## Definitions

- **{TASK_KEY}**: Story/Issue ID from the issue tracker (e.g., `FB-6`, `PROJ-123`, `KAN-42`)
- **Branch Name Format**: Use short format `{type}/{TASK_KEY}` (e.g., `feat/FB-6`, `fix/PROJ-123`)
  - Short format is recommended: `feat/FB-6` (not `feat/FB-6-file-watching-workspace-commands`)
  - **Important**: Be consistent within a project - use the same format for all branches

---

## ASDLC

- **Patterns**: [The Spec](https://asdlc.io/patterns/the-spec/), [The PBI](https://asdlc.io/patterns/the-pbi/), [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Factory Architecture, Quality Control

---

## Prerequisites

Before proceeding, the command verifies:

1. **MCP Status Validation**: All MCP servers (Atlassian, GitHub) are connected and authorized
2. **Plan File**: Plan document exists at `.plans/{TASK_KEY}-*.plan.md`
3. **Story Status**: Story can be transitioned to "In Progress" (auto-transitioned if needed)
4. **Story Assignment**: Story is assigned to current user

---

## Steps

1. **Pre-flight checks**
   - Validates MCP server connections (Atlassian, GitHub)
   - Reads plan from `.plans/{TASK_KEY}-*.plan.md` (uses most recently modified if multiple match)
   - Automatically transitions story to "In Progress" if not already there
   - Verifies story assignment

2. **Set up development environment**
   - Determines branch type prefix (feat/fix/chore/refactor) based on task type
   - Checks if branch already exists (asks user if found)
   - Creates branch with short format: `{type}/{TASK_KEY}` (e.g., `feat/FB-6`)
   - Posts work checklist comment to issue immediately after branch creation

3. **Implement according to plan**
   - Reads and understands complete plan
   - Analyzes existing codebase for patterns
   - Implements changes following plan specifications
   - Writes tests alongside code
   - Commits logical units of work as progress is made

---

## Tools

The command uses explicit MCP and filesystem tools:

- **MCP Atlassian**: Get issue, transitions, transition issue, add comments (with CloudId acquisition guidance)
- **MCP GitHub**: List branches, create branch
- **Filesystem**: Read plan files, create/modify code files
- **Codebase**: Search for similar implementations, grep for patterns
- **Terminal**: Git commands for branch management and commits

---

## Key Features

- **Auto-transition**: Automatically moves story to "In Progress" if not already there
- **Branch existence check**: Detects existing branches and handles conflicts
- **Plan file selection**: Uses most recently modified plan if multiple exist
- **Short branch format**: Consistent `{type}/{TASK_KEY}` naming
- **Incremental commits**: Commits logical units as work progresses
- **Error handling**: Clear STOP conditions with specific error messages

---

## Command Definition

Preview of actual command:

```markdown
# Start Task

## Overview
Begin development on a task with proper setup and pre-flight checks.

## Definitions
- {TASK_KEY}: Story/Issue ID
- Branch Name Format: Short format {type}/{TASK_KEY}

## Prerequisites
- MCP status validation
- Plan file exists
- Story can be transitioned to "In Progress"

## Steps
1. Pre-flight checks (MCP validation, plan file, story status)
2. Set up development environment (branch creation, issue updates)
3. Implement according to plan (with detailed sub-steps)

## Tools
- MCP Tools (Atlassian, GitHub)
- Filesystem Tools
- Codebase Tools
- Terminal Tools

## Guidance
- Role: Software engineer
- Instruction: Execute workflow steps
- Context: Task tracking, plan documents, MCP integrations
- Examples: Branch names, commit messages, issue comments
- Constraints: Unit tests required, conventional commits, branch naming
- Output: Development work with incremental commits
```

**[View full skill (source)](https://github.com/fancy-bread/sdlc-workflow-skills/blob/main/skills/start-task/SKILL.md)**

---

## Related Commands

**Before:** [`/create-plan`](create-plan.md) - Create plan first
**After:** [`/complete-task`](complete-task.md) - Finish and create PR

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
