---
title: /refine-task
---

# /refine-task

Refine a task to meet Definition of Ready (DoR) by ensuring clarity, completeness, and readiness for work. Focuses on producing clean, well-organized PBIs (Product Backlog Items) with clear acceptance criteria and minimal fluff. Used during backlog refinement sessions to prepare tasks for human refinement meetings.

| | |
|---|---|
| **Frequency** | Per task (during backlog refinement, before sprint planning) |
| **Prerequisites** | Task in backlog, MCP integrations configured |

---

## What It Does

Refines tasks to ensure they meet Definition of Ready criteria:
- Clear, unambiguous description
- Complete acceptance criteria (testable, specific, concise)
- Dependencies identified (if any)
- Well-organized, scannable structure

The command uses intelligent analysis to:
- Validate PBI structure (4-part anatomy: Directive, Context Pointer, Verification Pointer, Refinement Rule)
- Detect feature domain and check spec existence at `specs/{feature-domain}/spec.md`
- Enhance clarity by improving descriptions and acceptance criteria
- Remove fluff and unnecessary content
- Organize content for easy scanning and reading
- Generate a refinement report with DoR status, PBI validation, and clarity improvements

**PBI Structure Validation:**
- Checks for 4-part anatomy per ASDLC patterns
- Provides guidance if structure is missing (graceful degradation)
- Validates spec links in Context Pointer and Verification Pointer sections

---

## ASDLC

- **Patterns**: [The PBI](https://asdlc.io/patterns/the-pbi/), [The Spec](https://asdlc.io/patterns/the-spec/), [Context Gates](https://asdlc.io/patterns/context-gates/)
- **Pillars**: Factory Architecture, Quality Control (DoR as gate), Standardized Parts (PBI structure)

---

## Usage

```bash
/refine-task TASK-123
```

**Examples:**

```bash
# Refine a story for sprint planning
/refine-task FB-15

# Refine an epic before decomposition
/refine-task EPIC-100
```

---

## Example

```
You: /refine-task FB-15

AI:
✓ MCP status validation passed
✓ Fetching task FB-15: Add user authentication
✓ Validating PBI structure...
✓ PBI structure complete (all 4 parts present)
✓ Detecting feature domain: user-authentication
✓ Checking spec existence...
✓ Spec found at specs/user-authentication/spec.md
✓ Validating spec links...
✓ Context Pointer and Verification Pointer link to correct spec sections
✓ Analyzing task content for clarity...
✓ Enhancing description clarity
✓ Improving acceptance criteria (removed redundancy)
✓ Removing fluff (2 redundant sentences)
✓ Organizing content for better scanning
✓ Updating task in Jira...
✓ Generating refinement report...

## Refinement Report for FB-15

### Definition of Ready Status
✅ Clear description
✅ Acceptance criteria present, testable, and concise
✅ Dependencies identified (if any)
✅ Content organized for easy scanning

### PBI Structure Validation
✅ Task follows PBI 4-part anatomy (Directive, Context Pointer, Verification Pointer, Refinement Rule)

### Feature Domain and Spec Existence
Feature domain: `user-authentication`
✅ Spec found at `specs/user-authentication/spec.md`
✅ Context Pointer and Verification Pointer link to correct spec sections

### Clarity Improvements
- Enhanced description clarity (removed 2 redundant sentences)
- Improved acceptance criteria (removed redundancy, enhanced clarity)
- Reorganized content for better scanning and readability

Task refined and ready for human refinement meeting.
```

---

## Key Features

### Definition of Ready Focus

Ensures tasks meet DoR criteria before work begins:
- Clear, unambiguous descriptions
- Complete acceptance criteria (testable, specific, concise)
- Dependencies identified
- Well-organized, scannable structure

### PBI Structure Validation

Validates that tasks follow ASDLC PBI 4-part anatomy:
- **Directive**: What to do, with explicit scope boundaries
- **Context Pointer**: Reference to Spec Blueprint section
- **Verification Pointer**: Reference to Spec Contract section
- **Refinement Rule**: Protocol for when implementation diverges from Spec

Tasks without PBI structure are still refinable (graceful degradation), but guidance is provided to add missing sections.

### Feature Domain Detection

Automatically detects feature domain from task (labels, title, description) and:
- Checks if spec exists at `specs/{feature-domain}/spec.md`
- Validates Context Pointer and Verification Pointer link to correct spec sections
- Warns if spec is referenced but missing

### Clarity and Organization

Focuses on producing clean, scannable task descriptions:
- Enhances description completeness (what, why, how)
- Improves acceptance criteria quality (testable, specific, concise)
- Removes fluff and unnecessary content
- Organizes content for easy scanning (clear headings, bullet points, structure)

### Conservative Refinement

Only adds critical missing details without rewriting existing content:
- Enhances vague descriptions minimally
- Adds missing acceptance criteria
- Identifies dependencies
- Preserves existing good content

---

## When to Use

Use `/refine-task` when:
- Preparing backlog for human refinement meetings
- Tasks need clarification or acceptance criteria
- Tasks need better organization and structure
- Ensuring tasks meet Definition of Ready before work begins
- During backlog refinement sessions
- Tasks have verbose or disorganized content that needs cleanup

**Best Practice:** Run refinement on all backlog items before refinement meetings to ensure all work is clear, organized, and ready for human review.

---

## Related Commands

- **[`/create-task`](create-task.md)** - Create tasks that need refinement
- **[`/decompose-task`](decompose-task.md)** - Decompose large tasks before refinement
- **[`/create-plan`](create-plan.md)** - Create implementation plans after refinement

---

**[View full skill (source)](https://github.com/fancybread-com/sdlc-workflow-skills/blob/main/skills/refine-task/SKILL.md)**

