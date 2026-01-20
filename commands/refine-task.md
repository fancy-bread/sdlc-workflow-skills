# Refine Task

## Overview
Refine a task to meet Definition of Ready (DoR) by ensuring clarity, completeness, and readiness for work. Optionally estimate story points if the project uses them. Used during backlog refinement sessions before sprint planning or work assignment.

## Definitions

- **Spec** (this command): `specs/refine-task/spec.md` — Blueprint and Contract.
- **{TASK_KEY}**: Task/Story ID from issue tracker (e.g., `FB-15`, `PROJ-123`)
- **Definition of Ready (DoR)**: Criteria that a task must meet before it's ready for work:
  - Clear, unambiguous description
  - Complete acceptance criteria
  - Dependencies identified (if any)
  - Story points estimated (if project uses estimation)
- **Definition of Done (DoD)**: Criteria that must be met for a task to be considered complete (reference for refinement context)
- **Story Points**: Estimation unit (typically Fibonacci: 1, 2, 3, 5, 8, 13, 21) - **Optional** if project doesn't use estimation
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
     - Test Atlassian MCP connection using `mcp_atlassian_atlassianUserInfo`
     - Verify connection is authorized and operational
     - **If MCP connection fails, STOP and report the failure.**
   - **Obtain CloudId for Atlassian Tools:**
     - Use `mcp_atlassian_getAccessibleAtlassianResources` to get cloudId
     - Use the first result or match by site name
          - **Error Handling**: If cloudId cannot be determined, STOP and report: "Unable to determine Atlassian cloudId. Please verify MCP configuration."
       - **Fetch task from Jira:**
         - Use `mcp_atlassian_getJiraIssue` with `cloudId` and `issueIdOrKey` = {TASK_KEY}
         - Extract: title, description, acceptance criteria, labels, components, status, project key
         - **Check if project uses Story Points:**
           - Story Points field identifier: `customfield_10036` (Story Points field in this Jira instance)
           - Check if `customfield_10036` exists in the response fields
           - Read value from `fields.customfield_10036` (may be null/undefined if not yet set)
           - **Decision**: If field doesn't exist, project doesn't use story points → skip all estimation steps, focus on Definition of Ready refinement only
           - **Decision**: If field exists but is null, project uses story points but task is unestimated → proceed with estimation
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

3. **Query Historical Tasks** (Only if project uses story points)
   - **Skip this step if project doesn't use story points** (field doesn't exist)
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
     - Use `mcp_atlassian_searchJiraIssuesUsingJql` with the appropriate JQL
     - Set `maxResults` to 100 (or appropriate limit)
     - Extract fields: key, title, description, story points, labels, components, issue type
   - **Filter results:**
     - Ensure all tasks have story points > 0
     - Ensure all tasks are from same project
     - Store results for similarity analysis
   - **If query returns no results:**
     - Note: "No historical tasks found for estimation. Proceeding with common sense estimate only."

4. **Find Similar Tasks** (Only if project uses story points)
   - **Skip this step if project doesn't use story points** (field doesn't exist)
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

5. **Make Common Sense Estimate First** (Only if project uses story points)
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

6. **Validate/Adjust with Similar Tasks** (Only if project uses story points, if historical data available)
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

7. **Refine Task Content to Meet Definition of Ready** (Conservative approach)
   - **Focus on Definition of Ready criteria:**
     - **Clear, unambiguous description**: Ensure what, why, and context are clear
     - **Complete acceptance criteria**: Must be testable and specific
     - **Dependencies identified**: Note any blocking dependencies (if applicable)
     - **Ready to start work**: All information needed to begin work is present
   - **Analyze description completeness:**
     - Check if description clearly states what needs to be done and why
     - Compare to similar tasks (if available) or DoR standards
     - Identify if description is significantly shorter or less detailed
     - Note: Only enhance if clearly missing critical information
   - **Check acceptance criteria completeness:**
     - Verify acceptance criteria are testable and specific
     - Compare acceptance criteria count to similar tasks (if available) or DoR standards
     - Identify if key acceptance criteria are missing
     - Note: Only add if clearly missing critical criteria
   - **Identify missing critical details only:**
     - Look for gaps in description (what, why, how)
     - Look for missing testable acceptance criteria
     - Look for unstated dependencies or assumptions
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

8. **Check Existing Story Points** (Only if project uses story points)
   - **Skip this step if project doesn't use story points** (field doesn't exist)
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
         - Story points: Only update if project uses story points AND (no existing points OR estimates match)
         - Description: Only if conservatively refined (minimal changes)
         - Acceptance criteria: Only if conservatively refined (minimal additions)
       - **Update task:**
         - Use `mcp_atlassian_editJiraIssue` with:
           - `cloudId`
           - `issueIdOrKey` = {TASK_KEY}
           - `fields`: Object with fields to update
             - Story Points (if project uses story points): `{ "customfield_10036": <estimate_value> }` (numeric value)
             - Description (if refined): `{ "description": { "type": "doc", "version": 1, "content": [...] } }`
             - Acceptance criteria (if refined): Update within description or use appropriate field
         - **Note**: `customfield_10036` is the Story Points field identifier for this Jira instance (only update if field exists)
   - **Preserve all other fields:**
     - Do not modify labels, components, links, assignee, etc.
   - **Verify update succeeded:**
     - Re-fetch task to confirm changes were applied

10. **Generate and Post Report**
   - **Create markdown report:**
     - **Header**: "## Refinement Report for {TASK_KEY}"
     - **Definition of Ready Status:**
       - List DoR criteria checked:
         - "✅ Clear description"
         - "✅ Acceptance criteria present and testable"
         - "✅ Dependencies identified (if any)"
         - Story points: Only include if project uses story points
     - **Story Points Estimate** (Only if project uses story points):
       - If no existing points: "Estimated story points: **{estimate}**"
       - If existing points differ: "Existing story points: **{existing}** (preserved)\nEstimated story points: **{new_estimate}**\n\n⚠️ Estimates differ. Please review."
       - If estimates match: "Estimated story points: **{estimate}** (matches existing)"
       - **Justification** (if story points estimated):
         - **Common Sense Estimate:** "Initial estimate: {common_sense_estimate} points (based on work type: {work_type})"
         - If similar tasks found: "Validated against {count} similar completed tasks:"
           - List top 3-5 similar tasks with links and their story points
           - Show statistics (mode, median, average, range)
           - Note if historical data aligned with or adjusted the common sense estimate
         - If no similar tasks: "No historical data available for validation. Estimate based on common sense analysis of work type and scope."
     - **Similar Tasks Found** (Only if project uses story points and tasks found):
       - List top 5 similar tasks (if found):
         - Format: `- [{KEY}]({URL}): {title} ({story_points} points)`
       - Note: "Analyzed {total_count} completed tasks from {time_range}"
     - **Refinements Made:**
       - If description refined: "- Enhanced description (added {count} sentences/clarifications) to meet Definition of Ready"
       - If acceptance criteria added: "- Added {count} acceptance criteria to meet Definition of Ready"
       - If no refinements: "- No refinements needed (task already meets Definition of Ready)"
     - **Confidence Level** (Only if story points estimated):
       - High: "High confidence estimate based on common sense analysis validated against {count} similar tasks with clear patterns"
       - Medium: "Medium confidence estimate based on common sense analysis validated against {count} similar tasks"
       - Low: "Low confidence estimate (common sense estimate only, no historical data available for validation)"
     - **Next Steps:**
       - If project uses story points and existing points preserved: "Please review the estimate difference and update story points manually if needed."
       - If project doesn't use story points: "Task refined and ready for work assignment (no estimation required)."
       - Otherwise: "Task refined and ready for sprint planning."
   - **Post report as comment:**
     - Use `mcp_atlassian_addCommentToJiraIssue` with:
       - `cloudId`
       - `issueIdOrKey` = {TASK_KEY}
       - `commentBody` = markdown report content
   - **Verify comment was posted:**
     - Confirm comment appears in issue

## Tools

### MCP Tools (Atlassian)
- `mcp_atlassian_atlassianUserInfo` - Verify Atlassian MCP connection
- **Obtaining CloudId for Atlassian Tools:**
  - **Method 1 (Recommended)**: Use `mcp_atlassian_getAccessibleAtlassianResources`
    - Returns list of accessible resources with `cloudId` values
    - Use the first result or match by site name
    - Only call if cloudId is not already known or has expired
  - **Method 2**: Extract from Atlassian URLs
    - Jira URL format: `https://{site}.atlassian.net/...`
    - CloudId can be extracted from the URL or obtained via API
  - **Error Handling**: If cloudId cannot be determined, STOP and report: "Unable to determine Atlassian cloudId. Please verify MCP configuration."
- `mcp_atlassian_getJiraIssue` - Fetch task to refine
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}
  - Extract: title, description, acceptance criteria, labels, components, status, project key
  - Story Points: Read from `fields.customfield_10036` (may be null if not set)
- `mcp_atlassian_searchJiraIssuesUsingJql` - Query historical completed tasks
  - Parameters: `cloudId`, `jql` = (see JQL examples in Steps), `maxResults` = 100
  - Returns: List of completed tasks with story points
- `mcp_atlassian_editJiraIssue` - Update task (story points, description, acceptance criteria)
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}, `fields` = object with fields to update
  - Story Points field: `customfield_10036` (Story Points field identifier for this Jira instance)
  - **Note**: Only update story points if conditions met (no existing points or estimates match)
- `mcp_atlassian_addCommentToJiraIssue` - Post refinement report
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
- [ ] Project story points usage determined (field exists or not)
- [ ] Board type determined (Scrum or Kanban) - if estimating
- [ ] Historical tasks queried successfully (if estimating)
- [ ] Similar tasks identified (if estimating, minimum 2 if possible)
- [ ] Story points estimated (if project uses story points, or skip)
- [ ] Task content analyzed for Definition of Ready refinements
- [ ] Existing story points checked (if project uses story points)
- [ ] Task updated in Jira (if applicable)
- [ ] Refinement report generated and posted

## Guidance

### Role
Act as a **Scrum Master, Product Manager, or Team Lead** responsible for backlog refinement. You are analytical, data-driven, and focused on improving task clarity and estimate accuracy.

### Instruction
Execute the refine-task workflow to improve a task by making a common sense estimate first, then validating/adjusting with historical similar tasks if available, and conservatively enhancing task details. This helps ensure tasks are well-defined and accurately estimated before sprint planning.

### Context
- Tasks need refinement to meet Definition of Ready (DoR) before work begins
- DoR criteria: Clear description, complete acceptance criteria, dependencies identified, and optionally estimated (if project uses estimation)
- Story point estimation is **optional** - only performed if project uses story points (field exists in Jira)
- For projects without story points: Focus on task clarity and DoR completeness only
- Common sense estimation (when used) comes first - recognize work type (documentation vs. code development) and make reasonable initial estimate
- Historical data from completed tasks provides valuable validation - use to confirm or adjust common sense estimate (if estimation is used)
- Team-level patterns (not individual assignment) are considered - learn from any team member's work
- Conservative refinement approach preserves existing content while filling critical gaps
- Story point estimates (if used) should prioritize common sense, validated by historical data when available

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
3. **Definition of Ready Focus**: Refinement must ensure task meets DoR criteria (clear description, acceptance criteria, dependencies identified).
4. **Story Points Optional**: Only estimate story points if project uses them (field exists). If field doesn't exist, skip all estimation steps and focus on DoR refinement only.
5. **Existing Points Protection**: If project uses story points and task already has story points that differ from new estimate, do NOT overwrite. Report the difference.
6. **Conservative Refinement**: Only add missing critical details. Do NOT rewrite or restructure existing content.
7. **Minimum Similar Tasks** (if estimating): 2 similar tasks sufficient for analysis. If fewer found, use description/AC analysis.
8. **Historical Range** (if estimating): Respect board type - 6 sprints for Scrum, 3 months for Kanban. Do not exceed these ranges.
9. **Team Assignment Neutral** (if estimating): Learn patterns from any team member's work. Do not filter by assignee.
10. **Similarity Scoring** (if estimating): Use weighted scoring (Title 40%, Description 40%, Context 20%). Rank top 5-10 matches.
11. **Fibonacci Rounding** (if estimating): Round estimates to Fibonacci sequence (1, 2, 3, 5, 8, 13, 21).
12. **Confidence Levels** (if estimating): Report confidence based on number of similar tasks and pattern clarity.

**Existing Standards (Reference):**
- MCP status validation: See `mcp-status.md` for detailed MCP server connection checks
- Story points: Fibonacci sequence (1, 2, 3, 5, 8, 13, 21) as standard estimation units
- Task refinement: Conservative approach (preserve existing, enhance minimally)
- Historical analysis: Team-level patterns, not individual performance

### Output
1. **Refined Task**: Task updated in Jira with:
   - Story points (if project uses story points AND no existing points or estimates match)
   - Enhanced description (if conservatively refined to meet DoR)
   - Enhanced acceptance criteria (if conservatively refined to meet DoR)

2. **Refinement Report**: Comment posted to task with:
   - Definition of Ready status (DoR criteria checked)
   - Estimated story points (if project uses story points, or comparison if existing points differ)
   - Justification (similar tasks or description/AC analysis, if estimation was performed)
   - Similar tasks found (with links and story points, if estimation was performed and tasks found)
   - Refinements made (if any, focused on DoR)
   - Confidence level (if estimation was performed)
   - Next steps (if review needed)

The refinement should ensure tasks meet Definition of Ready criteria. For projects using story points, the refinement also provides data-driven estimates based on historical work, while preserving existing good content.

