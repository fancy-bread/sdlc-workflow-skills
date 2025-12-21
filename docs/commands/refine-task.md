---
title: /refine-task
---

# /refine-task

Refine a task to meet Definition of Ready (DoR) by ensuring clarity, completeness, and readiness for work. Optionally estimate story points if the project uses them. Used during backlog refinement sessions before sprint planning or work assignment.

| | |
|---|---|
| **Roles** | Product Manager, Scrum Master |
| **Frequency** | Per task (during backlog refinement, before sprint planning) |
| **Prerequisites** | Task in backlog, MCP integrations configured |

---

## What It Does

Refines tasks to ensure they meet Definition of Ready criteria:
- Clear, unambiguous description
- Complete acceptance criteria
- Dependencies identified (if any)
- Story points estimated (optional - only if project uses story points)

The command uses intelligent analysis to:
- Make common-sense estimates based on work type (documentation vs. development vs. complex features)
- Validate estimates against historical similar tasks (past 6 sprints for Scrum, 3 months for Kanban)
- Conservatively enhance task descriptions and acceptance criteria
- Generate a refinement report with DoR status

**Adaptive to Methodology:**
- **Scrum**: Estimates story points using historical data from past 6 sprints
- **Kanban**: Optionally estimates (if Story Points field exists) using past 3 months of data
- **Without Story Points**: Focuses solely on Definition of Ready refinement

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
✓ Fetching task FB-15: Create refine-task command
✓ Project uses story points (field exists)
✓ Detected Scrum board (sprints configured)
✓ Querying historical tasks (past 6 sprints)...
✓ Found 5 similar completed tasks
✓ Making common-sense estimate: 3 points (feature development)
✓ Validating against historical data...
✓ Historical average: 3.2 points (rounded to 3)
✓ Refining task description and acceptance criteria...
✓ Updating task in Jira...
✓ Generating refinement report...

## Refinement Report for FB-15

### Definition of Ready Status
✅ Clear description
✅ Acceptance criteria present and testable
✅ Dependencies identified (if any)
✅ Story points estimated

**Story Points Estimate: 3**

### Justification
Common Sense Estimate: Initial estimate: 3 points (based on work type: feature development)

Historical Validation: Found 5 similar completed tasks. Average: 3.2 points. Consensus supports 3-point estimate.

### Refinements Made
- Enhanced acceptance criteria with specific testing requirements
- Added dependency note for MCP integration

Task refined and ready for sprint planning.
```

---

## Key Features

### Definition of Ready Focus

Ensures tasks meet DoR criteria before sprint planning:
- Clear, unambiguous descriptions
- Complete acceptance criteria
- Dependencies identified
- Story points estimated (if project uses them)

### Intelligent Estimation

Two-phase estimation approach:
1. **Common-Sense Estimate**: Based on work type (documentation = 1 point, simple feature = 2-3, complex = 5+)
2. **Historical Validation**: Compares against similar completed tasks from history

### Methodology Adaptive

- **Scrum**: Uses past 6 sprints (quarter) of historical data
- **Kanban**: Uses past 3 months of historical data
- **Without Story Points**: Skips estimation, focuses on DoR only

### Conservative Refinement

Only adds critical missing details without rewriting existing content:
- Enhances vague descriptions minimally
- Adds missing acceptance criteria
- Identifies dependencies
- Does not overwrite existing story points if different

---

## When to Use

Use `/refine-task` when:
- Preparing backlog for sprint planning
- Tasks need clarification or acceptance criteria
- Story points need estimation (if project uses them)
- Ensuring tasks meet Definition of Ready before work begins
- During backlog refinement sessions

**Best Practice:** Run refinement on all backlog items before sprint planning to ensure all work is properly sized and ready.

---

## Related Commands

- **[`/create-task`](create-task.md)** - Create tasks that need refinement
- **[`/decompose-task`](decompose-task.md)** - Decompose large tasks before refinement
- **[`/create-plan`](create-plan.md)** - Create implementation plans after refinement

---

**[View Full Command →](../implementations/cursor/commands/refine-task.md)**

