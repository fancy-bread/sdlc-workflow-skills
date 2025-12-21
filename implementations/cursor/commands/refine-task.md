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
         - Extract: title, description, acceptance criteria, labels, components, status, project key
         - **Read Story Points field:**
           - Story Points field identifier: `customfield_10036` (Story Points field in this Jira instance)
           - Read value from `fields.customfield_10036`
           - Field may be null/undefined if not yet set - this is expected for unestimated tasks
           - **Note**: If `customfield_10036` is not present in the response, the project may not have Story Points configured (e.g., simplified projects). In this case, skip story point estimation but continue with task refinement.
       - **Verify task is in refinable state:**
         - Check status is not "Done" or "Completed"
         - **If task is completed, STOP and report: "Task {TASK_KEY} is already completed and cannot be refined."**
       - **Extract task details:**
         - Title, description, acceptance criteria (if present)
         - Labels, components
         - Current story points: Read from `fields.customfield_10036` (may be null if not set, or field may not exist if project doesn't have Story Points configured)
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

5. **Make Common Sense Estimate First**
   - **Analyze task type and work nature:**
     - Identify what type of work this is (coding, documentation, configuration, etc.)
     - **Key distinction**: Documentation/markdown editing vs. code development
     - Recognize that documentation tasks (markdown files, README updates, etc.) are typically 1-2 points
     - Recognize that code development tasks require more estimation based on complexity
   - **Make initial common sense estimate based on work type:**
     - **Documentation/Markdown editing**: 1 point (editing existing files, adding sections)
     - **Simple code changes**: 1-2 points (small fixes, single file changes)
     - **Moderate development**: 2-3 points (new features, multiple files, some complexity)
     - **Complex development**: 3-5 points (significant features, integrations, multiple components)
     - **Very complex**: 5-8 points (architecture changes, major refactoring, complex integrations)
   - **Consider work scope:**
     - Number of files to modify
     - Amount of code to write
     - Testing requirements
     - Integration complexity
   - **Generate initial estimate:**
     - Round to nearest Fibonacci value (1, 2, 3, 5, 8, 13, 21)
     - Store as baseline estimate

6. **Validate/Adjust with Similar Tasks** (if historical data available)
   - **If similar tasks found (≥2):**
     - Extract story points from similar tasks
     - Calculate statistics:
       - **Mode**: Most common story point value
       - **Median**: Middle value when sorted
       - **Average**: Mean of all story point values
       - **Range**: Min and max values
     - **Compare to common sense estimate:**
       - If similar tasks average is close (±1 point): Keep or slightly adjust common sense estimate
       - If similar tasks average differs significantly: Consider adjusting, but maintain common sense bounds
       - Don't blindly follow historical data if it contradicts common sense
     - **Final estimate:**
       - Prefer common sense estimate if historical data is limited or questionable
       - If historical pattern is clear and strong (5+ tasks, low variance), use historical average
       - Round to nearest Fibonacci value (1, 2, 3, 5, 8, 13, 21)
     - **Determine confidence level:**
       - High: Common sense estimate + 5+ similar tasks with clear pattern, estimates aligned
       - Medium: Common sense estimate + 2-4 similar tasks, reasonable alignment
       - Low: Common sense estimate only (no similar tasks found), or conflicting historical data
   - **If no/few similar tasks found (<2):**
     - **Use common sense estimate:**
       - Rely on the initial common sense estimate made in Step 5
       - Document that no historical data was available for validation
     - **Lower confidence level:**
       - Set confidence to "Low" when only using common sense estimate
       - Note that estimate will improve as project accumulates historical data

7. **Refine Task Content** (Conservative approach)
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

8. **Check Existing Story Points**
   - **Check if task already has story points:**
     - Read story points from `fields.customfield_10036` (from task data fetched in Step 1)
     - If `customfield_10036` is null, undefined, or 0, treat as "no existing points"
     - If `customfield_10036` has a numeric value, store as existing points
   - **Compare new estimate to existing points:**
     - If no existing points: Proceed with update
     - If existing points match new estimate: Proceed with update (confirm in report)
     - If existing points differ from new estimate:
       - **Do NOT overwrite existing points**
       - Store both values for report
       - Note: "Existing points ({existing}) differ from estimate ({new}). Preserving existing points. Please review."

9. **Update Task in Jira**
       - **Prepare update fields:**
         - Story points: Only update if no existing points OR estimates match
         - Description: Only if conservatively refined (minimal changes)
         - Acceptance criteria: Only if conservatively refined (minimal additions)
       - **Update task:**
         - Use `mcp_Atlassian-MCP-Server_editJiraIssue` with:
           - `cloudId`
           - `issueIdOrKey` = {TASK_KEY}
           - `fields`: Object with fields to update
             - Story Points: `{ "customfield_10036": <estimate_value> }` (numeric value)
             - Description (if refined): `{ "description": { "type": "doc", "version": 1, "content": [...] } }`
             - Acceptance criteria (if refined): Update within description or use appropriate field
         - **Note**: `customfield_10036` is the Story Points field identifier for this Jira instance
   - **Preserve all other fields:**
     - Do not modify labels, components, links, assignee, etc.
   - **Verify update succeeded:**
     - Re-fetch task to confirm changes were applied

10. **Generate and Post Report**
   - **Create markdown report:**
     - **Header**: "## Refinement Report for {TASK_KEY}"
     - **Story Points Estimate:**
       - If no existing points: "Estimated story points: **{estimate}**"
       - If existing points differ: "Existing story points: **{existing}** (preserved)\nEstimated story points: **{new_estimate}**\n\n⚠️ Estimates differ. Please review."
       - If estimates match: "Estimated story points: **{estimate}** (matches existing)"
            - **Justification:**
              - **Common Sense Estimate:** "Initial estimate: {common_sense_estimate} points (based on work type: {work_type})"
              - If similar tasks found: "Validated against {count} similar completed tasks:"
                - List top 3-5 similar tasks with links and their story points
                - Show statistics (mode, median, average, range)
                - Note if historical data aligned with or adjusted the common sense estimate
              - If no similar tasks: "No historical data available for validation. Estimate based on common sense analysis of work type and scope."
     - **Similar Tasks Found:**
       - List top 5 similar tasks (if found):
         - Format: `- [{KEY}]({URL}): {title} ({story_points} points)`
       - Note: "Analyzed {total_count} completed tasks from {time_range}"
     - **Refinements Made:**
       - If description refined: "- Enhanced description (added {count} sentences/clarifications)"
       - If acceptance criteria added: "- Added {count} acceptance criteria"
       - If no refinements: "- No refinements needed (task already well-defined)"
     - **Confidence Level:**
       - High: "High confidence estimate based on common sense analysis validated against {count} similar tasks with clear patterns"
       - Medium: "Medium confidence estimate based on common sense analysis validated against {count} similar tasks"
       - Low: "Low confidence estimate (common sense estimate only, no historical data available for validation)"
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
  - Extract: title, description, acceptance criteria, labels, components, status, project key
  - Story Points: Read from `fields.customfield_10036` (may be null if not set)
- `mcp_Atlassian-MCP-Server_searchJiraIssuesUsingJql` - Query historical completed tasks
  - Parameters: `cloudId`, `jql` = (see JQL examples in Steps), `maxResults` = 100
  - Returns: List of completed tasks with story points
- `mcp_Atlassian-MCP-Server_editJiraIssue` - Update task (story points, description, acceptance criteria)
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}, `fields` = object with fields to update
  - Story Points field: `customfield_10036` (Story Points field identifier for this Jira instance)
  - **Note**: Only update story points if conditions met (no existing points or estimates match)
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
Execute the refine-task workflow to improve a task by making a common sense estimate first, then validating/adjusting with historical similar tasks if available, and conservatively enhancing task details. This helps ensure tasks are well-defined and accurately estimated before sprint planning.

### Context
- Tasks need refinement before sprint planning to ensure clarity and accurate estimation
- Common sense estimation comes first - recognize work type (documentation vs. code development) and make reasonable initial estimate
- Historical data from completed tasks provides valuable validation - use to confirm or adjust common sense estimate
- Team-level patterns (not individual assignment) are considered - learn from any team member's work
- Conservative refinement approach preserves existing content while filling critical gaps
- Story point estimates should prioritize common sense, validated by historical data when available

### Examples

**Example 1: Task with Similar Historical Tasks**

```
Input: /refine-task FB-123

Task: "Add user authentication"
Common sense estimate: 5 points (moderate development - authentication features typically moderate complexity)
Similar tasks found: 8 similar authentication-related tasks
- FB-45: "Implement OAuth login" (5 points)
- FB-67: "Add SSO support" (5 points)
- FB-89: "Create login API" (3 points)
...

Output:
- Estimated: 5 story points (common sense estimate validated by similar tasks - mode: 5 points)
- Confidence: High (common sense + 8 similar tasks, clear pattern, estimates aligned)
- Similar tasks listed with links
- Minimal refinements (task already well-defined)
```

**Example 2: Documentation Task (Common Sense Primary)**

```
Input: /refine-task FB-124

Task: "Update README.md with new command documentation"
Common sense estimate: 1 point (documentation/markdown editing - simple task)
Similar tasks found: 2 similar documentation tasks
- FB-56: "Update API documentation" (1 point)
- FB-78: "Add user guide section" (1 point)

Output:
- Estimated: 1 story point (common sense estimate validated by similar tasks)
- Confidence: Medium (common sense + 2 similar tasks, estimates aligned)
- Minimal refinements needed
```

**Example 3: Task with Few Similar Tasks**

```
Input: /refine-task FB-125

Task: "Create new reporting dashboard"
Common sense estimate: 5 points (complex development - dashboard with multiple components)
Similar tasks found: 1 similar task
- FB-78: "Build analytics page" (8 points)

Output:
- Estimated: 5 story points (common sense estimate, validated against 1 similar task which suggests 8 points, but kept common sense estimate due to limited data)
- Confidence: Medium (common sense primary, 1 similar task for reference)
- Added 1 acceptance criterion based on similar task pattern
```

**Example 4: Task with Existing Story Points**

```
Input: /refine-task FB-126

Task: "Refactor payment service" (existing: 3 points)
Common sense estimate: 5 points (moderate complexity - refactoring existing service)
Validated against: 6 similar refactoring tasks (average: 5 points)

Output:
- Existing points: 3 (preserved - differs from estimate)
- Estimated: 5 points (common sense + historical validation)
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

