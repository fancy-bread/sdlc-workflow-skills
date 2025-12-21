# Refine Task Command Plan

## Context

Currently there is no command for task refinement - a critical backlog grooming activity. Teams need a way to refine tasks (add detail, estimate story points) before sprint planning, using historical data to inform estimates.

## Goals

Create a new `/refine-task` command that:
1. Refines task details (description, acceptance criteria)
2. Estimates story points using historical data analysis
3. Analyzes similar past work to inform estimates
4. Updates the task in Jira with refined content and estimate
5. Generates a refinement report

## Requirements

### Functional Requirements

1. **Task Analysis**
   - Read task from Jira (title, description, current acceptance criteria, labels, components)
   - Analyze task content to understand scope and complexity
   - Identify task type and context

2. **Historical Data Analysis**
   - **Scrum Projects**: Look back 6 sprints (quarter of work)
   - **Kanban Projects**: Look back 3 months
   - Find completed tasks (status: "Done" or "Completed") with story points
   - Match similar tasks using:
     - Title keywords/patterns
     - Description patterns
     - Labels (if applicable)
     - Components (if applicable)
     - Task type (Story, Task, Bug)

3. **Similarity Analysis**
   - Compare task title to historical titles (keyword matching, semantic similarity)
   - Compare task description to historical descriptions
   - Consider labels and components for context matching
   - Team assignment is neutral - look at work done by any team member (team-level patterns)

4. **Story Point Estimation**
   - Analyze story points from similar historical tasks
   - Consider:
     - Most common story point value for similar tasks
     - Range of story points (min/max) for similar tasks
     - Average story points for similar tasks
     - Task complexity indicators (word count, acceptance criteria count, etc.)
   - Provide estimate with confidence/justification

5. **Task Refinement**
   - Enhance description if needed (based on patterns from similar tasks)
   - Ensure acceptance criteria are clear and complete (compare to similar tasks)
   - Add missing details that are typically present in similar completed tasks
   - Maintain existing good content

6. **Update Task**
   - Update story point field in Jira
   - Update description (if refined)
   - Update acceptance criteria (if refined)
   - Preserve existing labels, components, links

7. **Generate Report**
   - Create refinement report comment on task
   - Include:
     - Estimated story points with justification
     - Similar tasks found and their story points
     - Key patterns identified
     - Refinements made (if any)
     - Confidence level in estimate

### Technical Requirements

1. **MCP Integration**
   - Atlassian/Jira: Read tasks, search historical tasks, update tasks, add comments
   - Query completed tasks with filters (status, date range, story points)

2. **Data Analysis**
   - Pattern matching for similarity (title, description)
   - Statistical analysis (averages, ranges, modes)
   - Date range calculations (6 sprints for Scrum, 3 months for Kanban)

3. **Board Type Detection**
   - Detect if project uses Scrum (sprints) or Kanban (continuous)
   - Adjust date range accordingly

## Command Structure

Following the structure of better commands (`create-plan`, `start-task`, `complete-task`):

### Overview
Refine a task by analyzing historical work, estimating story points, and updating task details. Used during backlog refinement sessions before sprint planning.

### Definitions
- **{TASK_KEY}**: Task/Story ID from issue tracker (e.g., `FB-15`, `PROJ-123`)
- **Story Points**: Estimation unit (typically Fibonacci: 1, 2, 3, 5, 8, 13, 21)
- **Historical Range**:
  - Scrum: Past 6 sprints (quarter)
  - Kanban: Past 3 months
- **Completed Status**: "Done" or "Completed" status in Jira

### Prerequisites
- MCP Status Validation
- Task exists in Jira
- Task has readable title and description
- Access to historical tasks for analysis

### Steps
1. **Validate and Read Task**
   - Perform MCP status validation
   - Fetch task from Jira
   - Verify task is in refinable state (not "Done", etc.)
   - Extract task details (title, description, acceptance criteria, labels, components, current story points)

2. **Determine Board Type**
   - Detect if project uses Scrum or Kanban
   - Query sprints (Scrum) or use date range (Kanban)
   - Calculate appropriate historical range

3. **Query Historical Tasks**
   - Search for completed tasks in historical range
   - Filter by:
     - Status: "Done" or "Completed"
     - Has story points > 0
     - Same project/board
   - Return task details (key, title, description, story points, labels, components)

4. **Find Similar Tasks**
   - Analyze title keywords/patterns
   - Compare description patterns
   - Consider labels and components
   - Match task type
   - Score similarity (rank by relevance)
   - Select top 5-10 most similar tasks
   - **Minimum**: 2 similar tasks sufficient for analysis
   - **If < 2 found**: Proceed with description/AC analysis for estimation

5. **Analyze Story Points**
   - **If similar tasks found (≥2):**
     - Extract story points from similar tasks
     - Calculate statistics:
       - Mode (most common value)
       - Median (middle value)
       - Average
       - Min/Max range
     - Consider task complexity factors
     - Generate estimate with confidence level
   - **If no/few similar tasks found (<2):**
     - Analyze task description and acceptance criteria
     - Consider complexity indicators:
       - Description length and detail
       - Number of acceptance criteria
       - Technical complexity indicators
       - Scope indicators
     - Generate estimate based on task characteristics
     - Lower confidence level (fewer similar tasks)

6. **Refine Task Content** (Conservative approach)
   - Analyze description completeness (compare to similar tasks)
   - Check acceptance criteria completeness
   - Identify missing critical details only
   - **Conservative enhancements:**
     - Clarify ambiguous language (don't rewrite)
     - Add missing critical acceptance criteria only
     - Fill gaps in description, don't restructure
   - Preserve existing good content - minimal changes

7. **Check Existing Story Points**
   - Check if task already has story points
   - Compare new estimate to existing points
   - **If difference exists:**
     - Do NOT overwrite existing points
     - Note difference in report for user review
   - **If no existing points or estimates match:**
     - Proceed with update

8. **Update Task in Jira**
   - Update story point field (only if no existing points or matches)
   - Update description (if conservatively refined)
   - Update acceptance criteria (if conservatively refined)
   - Preserve all other fields

9. **Generate and Post Report**
   - Create markdown report with:
     - Estimated story points (or comparison if existing points differ)
     - Justification (similar tasks, patterns, or description/AC analysis)
     - Similar tasks found (with links and their story points)
     - Number of similar tasks analyzed
     - Refinements made (if any)
     - Confidence level (based on number of similar tasks)
     - Note if existing points were preserved due to difference
   - Post as comment to task

### Tools

**MCP Tools (Atlassian)**
- `mcp_Atlassian-MCP-Server_getJiraIssue` - Fetch task to refine
- `mcp_Atlassian-MCP-Server_editJiraIssue` - Update task (story points, description, acceptance criteria)
- `mcp_Atlassian-MCP-Server_addCommentToJiraIssue` - Post refinement report
- `mcp_Atlassian-MCP-Server_searchJiraIssuesUsingJql` - Query historical completed tasks
  - JQL: `project = {PROJECT} AND status IN ("Done", "Completed") AND "Story Points" > 0 AND resolved >= {DATE_RANGE} ORDER BY resolved DESC`

**Codebase Tools** (if needed for pattern analysis)
- Pattern matching logic for similarity analysis

### Guidance

**Role**: Scrum Master, Product Manager, or Team Lead responsible for backlog refinement

**Context**:
- Tasks need refinement before sprint planning
- Historical data provides context for realistic estimates
- Team-level patterns (not individual assignment) are considered
- Refinement improves task clarity and estimate accuracy

**Examples**:
- Refining a story before sprint planning
- Re-estimating tasks after scope changes
- Adding detail to vague tasks using historical patterns

**Constraints**:
- Only analyze completed tasks with story points
- Respect historical range (6 sprints for Scrum, 3 months for Kanban)
- Preserve existing task content - only enhance, don't replace
- Team assignment neutral - learn from any team member's work

### Success Criteria

1. ✅ Task refined with enhanced description and acceptance criteria (if needed)
2. ✅ Story points estimated based on historical similar work
3. ✅ Similar tasks identified and analyzed
4. ✅ Task updated in Jira with story points and refinements
5. ✅ Refinement report posted with justification
6. ✅ Historical analysis respects board type (Scrum vs Kanban)

## Implementation Considerations

### Historical Data Query

**JQL for Scrum (6 sprints):**
```
project = FB
AND status IN ("Done", "Completed")
AND "Story Points" > 0
AND resolved >= startOfWeek("-18w")
ORDER BY resolved DESC
```

**JQL for Kanban (3 months):**
```
project = FB
AND status IN ("Done", "Completed")
AND "Story Points" > 0
AND resolved >= -3m
ORDER BY resolved DESC
```

### Similarity Matching Strategy

1. **Title Similarity**
   - Extract keywords from title
   - Compare keywords to historical titles
   - Use word overlap scoring

2. **Description Similarity**
   - Compare description length and structure
   - Identify common phrases/patterns
   - Consider technical terms and domain language

3. **Context Matching**
   - Match labels (if present)
   - Match components (if present)
   - Match task type (Story, Task, Bug)

4. **Scoring**
   - Weight: Title (40%), Description (40%), Context (20%)
   - Rank top matches

### Story Point Estimation Logic

1. **Collect Data**
   - **If ≥2 similar tasks found:**
     - Get story points from similar tasks (minimum 2, up to 10)
     - Filter out outliers if significant variance
   - **If <2 similar tasks found:**
     - Use description and acceptance criteria analysis
     - Analyze complexity indicators

2. **Calculate Statistics** (if similar tasks found)
   - Mode (most common value)
   - Median (middle value)
   - Average
   - Range (min-max)

3. **Estimate**
   - **From similar tasks:**
     - Prefer mode if clear pattern exists
     - Use median if mode is unclear
     - Consider task complexity differences
   - **From description/AC analysis:**
     - Analyze description length and detail
     - Count acceptance criteria
     - Assess technical complexity
     - Estimate based on complexity indicators
   - Round to Fibonacci sequence values (1, 2, 3, 5, 8, 13, 21)

4. **Confidence Level**
   - High: 5+ similar tasks, clear pattern
   - Medium: 2-4 similar tasks, reasonable pattern
   - Low: <2 similar tasks, using description/AC analysis

5. **Existing Points Handling**
   - If task already has story points:
     - Compare new estimate to existing
     - If different: Do NOT overwrite, report difference
     - If same: Confirm in report

## Decisions / Requirements

1. **What if no similar tasks found?**
   - ✅ Use task description and acceptance criteria to make informed estimation decisions
   - Analyze task complexity, scope, and detail level
   - Estimate based on task characteristics (word count, criteria count, technical complexity indicators)

2. **What if task already has story points?**
   - ✅ Compare new estimate to existing story points
   - If difference exists, do NOT overwrite
   - Note the difference in the report and ask user to review
   - If estimates match, confirm in report

3. **Similarity matching detail:**
   - Use keyword matching and pattern analysis (title and description)
   - Analyze top 5-10 similar tasks for patterns
   - Minimum: 2 similar tasks sufficient for analysis

4. **Refinement aggressiveness:**
   - ✅ Conservative approach
   - Only add missing critical details
   - Enhance descriptions minimally (clarify, don't rewrite)
   - Add acceptance criteria only if clearly missing
   - Preserve existing content

5. **Historical data requirements:**
   - ✅ Minimum 2 similar tasks sufficient for analysis
   - If fewer than 2 similar tasks found, use description/AC analysis (see #1)
   - Report confidence level based on number of similar tasks found

## Dependencies

- Requires access to historical task data
- Requires Jira to support story point field
- Requires ability to query by date range and status

## Notes

- This is a NEW command (not improving existing one)
- Should follow structure of better commands from the start
- Team assignment is neutral - learn patterns from any team member
- Focus on team-level patterns, not individual performance
- Designed for backlog refinement workflow

