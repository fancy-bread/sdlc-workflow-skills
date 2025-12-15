---
title: /create-plan
---

# /create-plan

Create a detailed technical implementation plan for a story by analyzing requirements, reviewing the codebase, and generating a structured plan document.

| | |
|---|---|
| **Roles** | All Engineers |
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
✓ MCP status validation passed
✓ Fetching story FB-6: File watching for workspace commands
✓ Story has 5 acceptance criteria
✓ Analyzing codebase for similar implementations...
✓ Found 3 similar file watching patterns
✓ Reviewing existing test patterns...
✓ Designing implementation approach...
✓ Breaking down into 4 subtasks...
✓ Generating plan document...
✓ Plan saved: .plans/FB-6-file-watching.plan.md
✓ Posting plan summary to issue...
✓ Plan created successfully

Plan includes:
- Story and context
- Scope (in/out)
- 5 acceptance criteria
- Technical design with components
- 4 implementation steps with file changes
- Test strategy (unit + integration)
- Dependencies documented
```

---

## Definitions

- **{TASK_KEY}**: Story/Issue ID from the issue tracker (e.g., `FB-6`, `PROJ-123`, `KAN-42`)
- **Branch Name Format**: Use short format `{type}/{TASK_KEY}` (e.g., `feat/FB-6`, `fix/PROJ-123`)
  - Short format is recommended: `feat/FB-6` (not `feat/FB-6-file-watching-workspace-commands`)
  - **Important**: Be consistent within a project - use the same format for all branches
- **Plan Document**: Technical implementation plan saved at `.plans/{TASK_KEY}-{description}.plan.md`
  - Contains story details, technical design, implementation steps, and testing strategy
- **User Story Format**: Typically follows "As a [user type], I want [goal], so that [benefit]"
- **Acceptance Criteria**: Specific, testable conditions (minimum 3-5 required)

---

## Prerequisites

Before proceeding, the command verifies:

1. **MCP Status Validation**: All MCP servers (Atlassian, GitHub) are connected and authorized
2. **Story Exists**: Story exists in issue tracker and can be fetched
3. **Story Has Sufficient Detail**: Story has clear description, 3-5 acceptance criteria, and context

---

## Steps

1. **Analyze story**
   - Fetch story from issue tracker using MCP tools
   - Parse user story format (persona, goal, benefit)
   - Extract acceptance criteria (STOP if none found)
   - Identify technical requirements
   - Check for missing information (STOP if critical info missing)

2. **Analyze codebase**
   - Search for similar implementations using `codebase_search`
   - Identify affected components and files
   - Review existing patterns (structure, testing, naming, error handling)
   - Review related test files for patterns
   - Note blockers or unclear patterns

3. **Design implementation**
   - Break down into 3-7 logical subtasks
   - Identify files to create/modify (with exact paths)
   - Plan database changes (if applicable)
   - Design API changes (if applicable)
   - Plan test strategy (unit, integration, test data)
   - Document dependencies
   - Plan error handling

4. **Generate plan document**
   - Create plan file at `.plans/{TASK_KEY}-{kebab-case-description}.plan.md`
   - Write plan with required sections: Story, Context, Scope, Acceptance Criteria, Technical Design, Implementation Steps, Testing, Dependencies, Status
   - Verify plan file was created
   - Post plan summary to issue tracker with link and key steps

---

## Tools

The command uses explicit MCP and codebase tools:

- **MCP Atlassian**: Get issue, get remote issue links, add comments (with CloudId acquisition guidance)
- **MCP GitHub**: Get issue, add issue comment
- **Filesystem**: Check for existing plan files, write plan document, read code files
- **Codebase**: Search for similar implementations, grep for patterns, find test files
- **Terminal**: Find commands, git log searches

---

## Key Features

- **Story validation**: Ensures story has sufficient detail before proceeding
- **Codebase analysis**: Finds similar implementations to follow existing patterns
- **Structured plan**: Generates plan with all required sections
- **Plan file naming**: Uses kebab-case format `{TASK_KEY}-{description}.plan.md`
- **Issue integration**: Posts plan summary to issue automatically
- **Error handling**: Clear STOP conditions with specific guidance

---

## Plan Document Structure

The generated plan includes:

1. **Story**: User story format or clear description
2. **Context**: Background, motivation, related issues
3. **Scope**: What's included and explicitly excluded
4. **Acceptance Criteria**: Numbered, testable criteria
5. **Technical Design**: Architecture, components, data model, API design
6. **Implementation Steps**: Ordered subtasks with file changes
7. **Testing**: Unit tests, integration tests, test data
8. **Dependencies**: External and internal dependencies
9. **Status**: Checklist for tracking progress

---

## Command Definition

Preview of actual command:

```markdown
# Create Plan

## Overview
Create a detailed technical implementation plan for a story.

## Definitions
- {TASK_KEY}: Story/Issue ID
- Branch Name Format: Short format {type}/{TASK_KEY}
- Plan Document: Structured markdown plan file
- User Story Format: "As a... I want... So that..."

## Prerequisites
- MCP status validation
- Story exists and has sufficient detail
- Story has 3-5 acceptance criteria

## Steps
1. Analyze story (fetch, parse, extract criteria)
2. Analyze codebase (find similar implementations, review patterns)
3. Design implementation (break down, identify files, plan tests)
4. Generate plan document (create file, post summary)

## Tools
- MCP Tools (Atlassian, GitHub)
- Filesystem Tools
- Codebase Tools
- Terminal Tools

## Guidance
- Role: Software engineer
- Instruction: Generate comprehensive implementation plan
- Context: Story tracking, codebase patterns, plan documents
- Examples: Story input, plan output, issue comments
- Constraints: Story validation, codebase analysis, required sections
- Output: Plan document and issue comment
```

**[View Full Command →](../implementations/cursor/commands/create-plan.md)**

---

## Used By

- **[IC Engineer](../roles/engineer.md)** - Every story
- **[Senior Engineer](../roles/engineer.md)** - Complex features
- **[Staff Engineer](../roles/engineer.md)** - System design

---

## Related Commands

**Execute:** [`/start-task`](start-task.md) - Begin implementation using the plan
**Complete:** [`/complete-task`](complete-task.md) - Finish and create PR (uses plan summary)

---

[:octicons-arrow-left-24: Back to Commands](../index.md)
