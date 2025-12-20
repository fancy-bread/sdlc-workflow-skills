# Refine Task

## Overview
Refine a task by analyzing historical work, estimating story points, and updating task details. Used during backlog refinement sessions before sprint planning.

## Definitions

- **{TASK_KEY}**: Task/Story ID from issue tracker (e.g., `FB-15`, `PROJ-123`)
- **Story Points**: Estimation unit (typically Fibonacci: 1, 2, 3, 5, 8, 13, 21)
- **Historical Range**:
  - Scrum: Past 6 sprints (quarter)
  - Kanban: Past 3 months
- **Completed Status**: "Done" or "Completed" status in Jira
- **Similarity Scoring**: Weighted comparison (Title 40%, Description 40%, Context 20%)

## Prerequisites

Before proceeding, verify:

1. **MCP Status Validation**: Perform MCP server status checks (see `mcp-status.md` for detailed steps)
   - Test each configured MCP server connection (Atlassian, GitHub, etc.)
   - Verify all required integrations are authorized and operational
   - **If any MCP server fails validation, STOP and report the failure. Do not proceed.**

2. **Task Exists**: Verify the task exists in Jira
   - Use MCP tools to fetch task by `{TASK_KEY}`
   - **If task doesn't exist, STOP and report error: "Task {TASK_KEY} not found"**

3. **Task Has Sufficient Detail**: Verify task has:
   - Readable title and description
   - At least basic context
   - **If task is completely empty or unreadable, STOP and ask user to provide basic information.**

4. **Task is Refinable**: Verify task is not already in "Done" or "Completed" status
   - **If task is already completed, STOP and report: "Task {TASK_KEY} is already completed and cannot be refined."**

## Steps

1. **Validate and Read Task**
   - **Perform MCP status validation:**
     - Test Atlassian MCP connection using `mcp_Atlassian-MCP-Server_atlassianUserInfo`
     - Verify connection is authorized and operational
     - **If MCP connection fails, STOP and report the failure.**
   - **Obtain CloudId for Atlassian Tools:**
     - Use `mcp_Atlassian-MCP-Server_getAccessibleAtlassianResources` to get cloudId
     - Use the first result or match by site name
     - **Error Handling**: If cloudId cannot be determined, STOP and report: "Unable to determine Atlassian cloudId. Please verify MCP configuration."
   - **Fetch task from Jira:**
     - Use `mcp_Atlassian-MCP-Server_getJiraIssue` with `cloudId` and `issueIdOrKey` = {TASK_KEY}
     - Extract: title, description, acceptance criteria, labels, components, current story points, status, project key
   - **Verify task is in refinable state:**
     - Check status is not "Done" or "Completed"
     - **If task is completed, STOP and report: "Task {TASK_KEY} is already completed and cannot be refined."**
   - **Extract task details:**
     - Title, description, acceptance criteria (if present)
     - Labels, components
     - Current story points (if any)
     - Project key (for historical queries)

2. **Determine Board Type**
   - **Detect if project uses Scrum or Kanban:**
     - Query project information to determine board type
     - Check if sprints are configured (Scrum) or continuous flow (Kanban)
     - Default to Kanban if cannot determine
   - **Calculate appropriate historical range:**
     - **Scrum**: Past 6 sprints (approximately 18 weeks / quarter)
     - **Kanban**: Past 3 months
   - **Prepare date range for JQL query:**
     - Scrum: Use `startOfWeek("-18w")` or similar
     - Kanban: Use `-3m` for 3 months ago

3. **Query Historical Tasks**
   - **Build JQL query:**
     - **Scrum JQL:**
       ```
       project = {PROJECT_KEY} 
       AND status IN ("Done", "Completed") 
       AND "Story Points" > 0 
       AND resolved >= startOfWeek("-18w")
       ORDER BY resolved DESC
       ```
     - **Kanban JQL:**
       ```
       project = {PROJECT_KEY} 
       AND status IN ("Done", "Completed") 
       AND "Story Points" > 0 
       AND resolved >= -3m
       ORDER BY resolved DESC
       ```
   - **Execute query:**
     - Use `mcp_Atlassian-MCP-Server_searchJiraIssuesUsingJql` with the appropriate JQL
     - Set `maxResults` to 100 (or appropriate limit)
     - Extract fields: key, title, description, story points, labels, components, issue type
   - **Filter results:**
     - Ensure all tasks have story points > 0
     - Ensure all tasks are from same project
     - Store results for similarity analysis

4. **Find Similar Tasks**
   - **Extract keywords from current task:**
     - Parse title into keywords (remove stop words, normalize)
     - Identify key terms from description
     - Extract labels and components
     - Note task type (Story, Task, Bug)
   - **Score similarity for each historical task:**
     - **Title Similarity (40% weight):**
       - Extract keywords from historical task title
       - Calculate word overlap score (common words / total unique words)
       - Normalize score (0-1 range)
     - **Description Similarity (40% weight):**
       - Compare description length similarity (logarithmic scale)
       - Identify common phrases or patterns
       - Consider technical terms and domain language overlap
       - Normalize score (0-1 range)
     - **Context Matching (20% weight):**
       - Match labels (if present): +0.1 per matching label
       - Match components (if present): +0.1 per matching component
       - Match task type: +0.1 if same type
       - Normalize to 0-1 range
     - **Calculate weighted total score:**
       - `total_score = (title_score * 0.4) + (description_score * 0.4) + (context_score * 0.2)`
   - **Rank and select similar tasks:**
     - Sort by similarity score (highest first)
     - Select top 5-10 most similar tasks
     - **Minimum**: 2 similar tasks sufficient for analysis
     - **If < 2 similar tasks found with score > 0.3:**
       - Note: "Few similar tasks found, using description/AC analysis for estimation"
       - Proceed with description/AC analysis path

5. **Analyze Story Points**
   - **If similar tasks found (≥2):**
     - Extract story points from similar tasks
     - Calculate statistics:
       - **Mode**: Most common story point value
       - **Median**: Middle value when sorted
       - **Average**: Mean of all story point values
       - **Range**: Min and max values
     - **Consider task complexity factors:**
       - Compare description length to similar tasks
       - Compare acceptance criteria count
       - Note any significant scope differences
     - **Generate estimate:**
       - Prefer mode if clear pattern exists (mode appears 2+ times)
       - Use median if mode is unclear or ties exist
       - Round to nearest Fibonacci value (1, 2, 3, 5, 8, 13, 21)
       - Consider complexity adjustments (±1 point if significantly different)
     - **Determine confidence level:**
       - High: 5+ similar tasks, clear pattern, low variance
       - Medium: 2-4 similar tasks, reasonable pattern
       - Low: 2 similar tasks, high variance
   - **If no/few similar tasks found (<2):**
     - **Analyze task description and acceptance criteria:**
       - Count description words (longer = more complex)
       - Count acceptance criteria (more criteria = more complex)
       - Identify technical complexity indicators:
         - Technical terms (API, database, integration, etc.)
         - Scope words (all, entire, complete, etc.)
         - Dependency indicators (requires, depends on, etc.)
       - **Estimate based on complexity indicators:**
         - Simple task (short desc, 1-2 AC): 1-3 points
         - Moderate task (medium desc, 3-5 AC): 3-5 points
         - Complex task (long desc, 5+ AC, technical): 5-8 points
         - Very complex (very long, many AC, integrations): 8-13 points
       - Round to nearest Fibonacci value
     - **Lower confidence level:**
       - Set confidence to "Low" when using description/AC analysis

6. **Refine Task Content** (Conservative approach)
   - **Analyze description completeness:**
     - Compare current description to similar tasks
     - Identify if description is significantly shorter or less detailed
     - Note: Only enhance if clearly missing critical information
   - **Check acceptance criteria completeness:**
     - Compare acceptance criteria count to similar tasks
     - Identify if key acceptance criteria are missing
     - Note: Only add if clearly missing critical criteria
   - **Identify missing critical details only:**
     - Look for gaps in description (what, why, how)
     - Look for missing testable acceptance criteria
     - Do NOT add nice-to-have details
   - **Conservative enhancements (if needed):**
     - **Clarify ambiguous language:**
       - Replace vague terms with specific terms (if clear from context)
       - Do NOT rewrite entire sentences
       - Do NOT change structure
     - **Add missing critical acceptance criteria only:**
       - Only if 0-1 acceptance criteria exist and similar tasks have 3+
       - Add 1-2 critical criteria based on similar task patterns
       - Do NOT add all possible criteria
     - **Fill gaps in description:**
       - Add 1-2 sentences if description is extremely short (< 50 words)
       - Only add what's clearly missing (what or why)
       - Do NOT restructure or rewrite
   - **Preserve existing good content:**
     - Keep all existing information
     - Only enhance, never replace
     - Maintain original structure and style

7. **Check Existing Story Points**
   - **Check if task already has story points:**
     - Read story points field from task data
     - If story points field is null or 0, treat as "no existing points"
   - **Compare new estimate to existing points:**
     - If no existing points: Proceed with update
     - If existing points match new estimate: Proceed with update (confirm in report)
     - If existing points differ from new estimate:
       - **Do NOT overwrite existing points**
       - Store both values for report
       - Note: "Existing points ({existing}) differ from estimate ({new}). Preserving existing points. Please review."

8. **Update Task in Jira**
   - **Prepare update fields:**
     - Story points: Only update if no existing points OR estimates match
     - Description: Only if conservatively refined (minimal changes)
     - Acceptance criteria: Only if conservatively refined (minimal additions)
   - **Update task:**
     - Use `mcp_Atlassian-MCP-Server_editJiraIssue` with:
       - `cloudId`
       - `issueIdOrKey` = {TASK_KEY}
       - `fields`: Object with fields to update
         - Story points field (if updating)
         - Description (if refined)
         - Acceptance criteria (if refined)
   - **Preserve all other fields:**
     - Do not modify labels, components, links, assignee, etc.
   - **Verify update succeeded:**
     - Re-fetch task to confirm changes were applied

9. **Generate and Post Report**
   - **Create markdown report:**
     - **Header**: "## Refinement Report for {TASK_KEY}"
     - **Story Points Estimate:**
       - If no existing points: "Estimated story points: **{estimate}**"
       - If existing points differ: "Existing story points: **{existing}** (preserved)\nEstimated story points: **{new_estimate}**\n\n⚠️ Estimates differ. Please review."
       - If estimates match: "Estimated story points: **{estimate}** (matches existing)"
     - **Justification:**
       - If similar tasks found: "Based on {count} similar completed tasks:"
         - List top 3-5 similar tasks with links and their story points
         - Show statistics (mode, median, average, range)
       - If using description/AC analysis: "Based on task description and acceptance criteria analysis:"
         - Note complexity indicators used
         - Explain estimation reasoning
     - **Similar Tasks Found:**
       - List top 5 similar tasks (if found):
         - Format: `- [{KEY}]({URL}): {title} ({story_points} points)`
       - Note: "Analyzed {total_count} completed tasks from {time_range}"
     - **Refinements Made:**
       - If description refined: "- Enhanced description (added {count} sentences/clarifications)"
       - If acceptance criteria added: "- Added {count} acceptance criteria"
       - If no refinements: "- No refinements needed (task already well-defined)"
     - **Confidence Level:**
       - High: "High confidence estimate based on {count} similar tasks with clear patterns"
       - Medium: "Medium confidence estimate based on {count} similar tasks"
       - Low: "Low confidence estimate (few similar tasks found, using description/AC analysis)"
     - **Next Steps:**
       - If existing points preserved: "Please review the estimate difference and update story points manually if needed."
       - Otherwise: "Task refined and ready for sprint planning."
   - **Post report as comment:**
     - Use `mcp_Atlassian-MCP-Server_addCommentToJiraIssue` with:
       - `cloudId`
       - `issueIdOrKey` = {TASK_KEY}
       - `commentBody` = markdown report content
   - **Verify comment was posted:**
     - Confirm comment appears in issue

## Tools

### MCP Tools (Atlassian)
- `mcp_Atlassian-MCP-Server_atlassianUserInfo` - Verify Atlassian MCP connection
- **Obtaining CloudId for Atlassian Tools:**
  - **Method 1 (Recommended)**: Use `mcp_Atlassian-MCP-Server_getAccessibleAtlassianResources`
    - Returns list of accessible resources with `cloudId` values
    - Use the first result or match by site name
    - Only call if cloudId is not already known or has expired
  - **Method 2**: Extract from Atlassian URLs
    - Jira URL format: `https://{site}.atlassian.net/...`
    - CloudId can be extracted from the URL or obtained via API
  - **Error Handling**: If cloudId cannot be determined, STOP and report: "Unable to determine Atlassian cloudId. Please verify MCP configuration."
- `mcp_Atlassian-MCP-Server_getJiraIssue` - Fetch task to refine
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}
  - Extract: title, description, acceptance criteria, labels, components, story points, status, project key
- `mcp_Atlassian-MCP-Server_searchJiraIssuesUsingJql` - Query historical completed tasks
  - Parameters: `cloudId`, `jql` = (see JQL examples in Steps), `maxResults` = 100
  - Returns: List of completed tasks with story points
- `mcp_Atlassian-MCP-Server_editJiraIssue` - Update task (story points, description, acceptance criteria)
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}, `fields` = object with fields to update
  - **Note**: Only update if conditions met (no existing points or estimates match)
- `mcp_Atlassian-MCP-Server_addCommentToJiraIssue` - Post refinement report
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}, `commentBody` = markdown report

### Codebase Tools
- Pattern matching logic for similarity analysis (implemented in command steps)

## Pre-flight Checklist
- [ ] MCP status validation performed (see `mcp-status.md`)
- [ ] All MCP servers connected and authorized
- [ ] Task exists in Jira
- [ ] Task has readable title and description
- [ ] Task is in refinable state (not "Done" or "Completed")
- [ ] CloudId obtained for Atlassian tools

## Refinement Checklist
- [ ] Task read and details extracted
- [ ] Board type determined (Scrum or Kanban)
- [ ] Historical tasks queried successfully
- [ ] Similar tasks identified (minimum 2 if possible)
- [ ] Story points estimated (or description/AC analysis completed)
- [ ] Task content analyzed for refinements
- [ ] Existing story points checked (if present)
- [ ] Task updated in Jira (if applicable)
- [ ] Refinement report generated and posted

## Guidance

### Role
Act as a **Scrum Master, Product Manager, or Team Lead** responsible for backlog refinement. You are analytical, data-driven, and focused on improving task clarity and estimate accuracy.

### Instruction
Execute the refine-task workflow to improve a task by analyzing historical work, estimating story points based on similar completed tasks, and conservatively enhancing task details. This helps ensure tasks are well-defined and accurately estimated before sprint planning.

### Context
- Tasks need refinement before sprint planning to ensure clarity and accurate estimation
- Historical data from completed tasks provides valuable context for realistic estimates
- Team-level patterns (not individual assignment) are considered - learn from any team member's work
- Conservative refinement approach preserves existing content while filling critical gaps
- Story point estimates should be based on actual historical data when possible

### Examples

**Example 1: Task with Similar Historical Tasks**

```
Input: /refine-task FB-123

Task: "Add user authentication"
Similar tasks found: 8 similar authentication-related tasks
- FB-45: "Implement OAuth login" (5 points)
- FB-67: "Add SSO support" (5 points)
- FB-89: "Create login API" (3 points)
...

Output:
- Estimated: 5 story points (mode of similar tasks)
- Confidence: High (8 similar tasks, clear pattern)
- Similar tasks listed with links
- Minimal refinements (task already well-defined)
```

**Example 2: Task with Few Similar Tasks**

```
Input: /refine-task FB-124

Task: "Create new reporting dashboard"
Similar tasks found: 1 similar task
- FB-78: "Build analytics page" (8 points)

Output:
- Estimated: 8 story points (based on similar task, adjusted for complexity)
- Confidence: Medium (1 similar task)
- Used description/AC analysis to supplement
- Added 1 acceptance criterion based on similar task pattern
```

**Example 3: Task with Existing Story Points**

```
Input: /refine-task FB-125

Task: "Refactor payment service" (existing: 3 points)
Estimated: 5 points (based on 6 similar refactoring tasks)

Output:
- Existing points: 3 (preserved)
- Estimated: 5 points
- ⚠️ Estimates differ. Please review.
- Listed similar tasks for comparison
```

### Constraints

**Rules (Must Follow):**
1. **MCP Validation**: Do not proceed if MCP status validation fails. STOP and report the failure.
2. **Task Validation**: Task must exist and be refinable (not "Done"). If not, STOP and report error.
3. **Conservative Refinement**: Only add missing critical details. Do NOT rewrite or restructure existing content.
4. **Existing Points Protection**: If task already has story points and new estimate differs, do NOT overwrite. Report the difference.
5. **Minimum Similar Tasks**: 2 similar tasks sufficient for analysis. If fewer found, use description/AC analysis.
6. **Historical Range**: Respect board type - 6 sprints for Scrum, 3 months for Kanban. Do not exceed these ranges.
7. **Team Assignment Neutral**: Learn patterns from any team member's work. Do not filter by assignee.
8. **Similarity Scoring**: Use weighted scoring (Title 40%, Description 40%, Context 20%). Rank top 5-10 matches.
9. **Fibonacci Rounding**: Round estimates to Fibonacci sequence (1, 2, 3, 5, 8, 13, 21).
10. **Confidence Levels**: Report confidence based on number of similar tasks and pattern clarity.

**Existing Standards (Reference):**
- MCP status validation: See `mcp-status.md` for detailed MCP server connection checks
- Story points: Fibonacci sequence (1, 2, 3, 5, 8, 13, 21) as standard estimation units
- Task refinement: Conservative approach (preserve existing, enhance minimally)
- Historical analysis: Team-level patterns, not individual performance

### Output
1. **Refined Task**: Task updated in Jira with:
   - Story points (if no existing points or estimates match)
   - Enhanced description (if conservatively refined)
   - Enhanced acceptance criteria (if conservatively refined)

2. **Refinement Report**: Comment posted to task with:
   - Estimated story points (or comparison if existing points differ)
   - Justification (similar tasks or description/AC analysis)
   - Similar tasks found (with links and story points)
   - Refinements made (if any)
   - Confidence level
   - Next steps (if review needed)

The refinement should improve task clarity and provide data-driven story point estimates based on historical work, while preserving existing good content.

