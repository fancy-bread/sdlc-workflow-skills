# Review Code

## Overview
Perform adversarial AI-assisted code review on a pull request or branch changes using Builder/Critic separation with dual-contract validation (Spec + Constitution).

## Definitions

- **{PR_KEY}**: Pull Request identifier (e.g., `PR-12`, `#12`, `12`). Can be specified as:
  - Full format: `PR-12` or `#12`
  - Numeric only: `12`
  - The command should accept any format and normalize it for API calls (extract numeric ID)
- **{BRANCH_NAME}**: Branch name to review (e.g., `feat/FB-12`, `main`, `develop`)
  - Can be local branch or remote branch
  - Format: `{type}/{TASK_KEY}` for feature branches (consistent with other commands)
- **{FEATURE_DOMAIN}**: Kebab-case feature name for Spec lookup (e.g., `user-authentication`, `command-audit`)
  - Determines which Spec to read from `specs/{FEATURE_DOMAIN}/spec.md`
  - May be extracted from branch name, PR title, or Jira issue context
- **PR (Pull Request)**: A GitHub pull request containing proposed changes to merge into a branch
  - Referenced using {PR_KEY} format (e.g., PR-12, #12, or 12)
  - Contains changes, metadata, comments, and review history
- **Branch**: A Git branch containing changes to review
  - Can be local (checked out in workspace) or remote (on GitHub)
  - Referenced using {BRANCH_NAME} format
  - For feature branches, follows `{type}/{TASK_KEY}` naming convention
- **Diff**: The difference between two versions of code showing additions, deletions, and modifications
  - Shows line-by-line changes in files
  - Indicates what was added (+), removed (-), or modified
  - Essential for understanding the scope of changes
- **Builder Agent**: The agent context that retrieves data, reads files, and packages context (no judgment)
- **Critic Agent**: Fresh context session that performs validation, identifies violations, and judges quality
- **Spec**: Living specification at `specs/{FEATURE_DOMAIN}/spec.md` containing:
  - **Blueprint**: Context, Architecture, Anti-Patterns (architectural constraints)
  - **Contract**: Definition of Done, Regression Guardrails, Scenarios (behavioral verification)
- **Constitution**: AGENTS.md Operational Boundaries (3-tier system):
  - **Tier 1 (ALWAYS)**: Non-negotiable standards (must follow)
  - **Tier 2 (ASK)**: High-risk operations requiring human approval
  - **Tier 3 (NEVER)**: Safety limits (must not violate)
- **Dual-Contract Validation**: Two-tier validation system:
  - **Functional Validation**: Code meets Spec's Blueprint and Contract
  - **Architectural Validation**: Code meets AGENTS.md Constitution (3-tier system)
- **Review Gate**: Decisional output (PASS/FAIL/WARNING) based on violation severity
  - **PASS**: No critical violations found
  - **FAIL**: Spec CRITICAL violations OR Constitutional Tier 3 violations found
  - **WARNING**: Spec warnings OR Constitutional Tier 2 violations found
- **Violation Report**: Structured report containing:
  - Description: What was violated
  - Impact: Why it matters (performance, security, maintainability, scalability)
  - Remediation: Ordered steps to fix the violation
  - Location: File:Line reference
  - Reference: Which Spec criterion or Constitutional boundary was violated

## Prerequisites

Before proceeding, verify:

1. **MCP Status Validation**: GitHub MCP connection required (see `mcp-status.md` for detailed steps)
   - Use GitHub MCP tools to verify connection
   - **If GitHub MCP connection fails, STOP and report: "GitHub MCP connection failed. Please verify MCP configuration (see mcp-status.md)."**

2. **PR/Branch Existence**: Verify {PR_KEY} or {BRANCH_NAME} is valid and accessible
   - **For PR ({PR_KEY}):**
     - Normalize {PR_KEY} format (extract numeric ID from PR-12, #12, or 12)
     - Use GitHub MCP to verify PR exists
     - **If PR not found or inaccessible, STOP and report: "Pull Request {PR_KEY} not found or inaccessible."**
   - **For branch ({BRANCH_NAME}):**
     - Use GitHub MCP or git commands to check if branch exists
     - **If branch not found, STOP and report: "Branch {BRANCH_NAME} not found."**

3. **Access Verification**: Verify user has access to PR/branch (read permissions)
   - Attempt to retrieve PR details or branch information
   - **If access denied, STOP and report: "Access denied to {PR_KEY} or {BRANCH_NAME}. Please verify permissions."**

## Steps

### [BUILDER AGENT CONTEXT]

1. **Retrieve changes**
   - **Determine if PR ({PR_KEY}) or branch ({BRANCH_NAME}):**
     - Check if input is a PR format (PR-12, #12, 12) or branch name
     - **Decision point:** PR vs branch determines which tools to use
   - **If PR ({PR_KEY}):**
     - Normalize {PR_KEY} format: Extract numeric ID from PR-12, #12, or 12
       - Example: PR-12 → 12, #12 → 12, 12 → 12
     - Use GitHub MCP to retrieve PR details, get list of changed files, and get full diff
     - **STOP condition:** If PR not found or inaccessible, report error and stop
   - **If branch ({BRANCH_NAME}):**
     - Verify branch exists using GitHub MCP or git commands
     - Get diff using `run_terminal_cmd`: `git diff main...{BRANCH_NAME}`
     - Get list of changed files using `run_terminal_cmd`: `git diff --name-only main...{BRANCH_NAME}`
     - **STOP condition:** If branch not found, report error and stop
   - **Read all changed files:**
     - Iterate through list of changed files
     - Use `read_file` to read each changed file
     - **STOP condition:** If any file is unreadable or doesn't exist, report warning but continue with available files
   - **Understand scope of changes:**
     - Review file paths to understand which parts of codebase are affected
     - Count lines changed, files changed
     - Identify change types: new files, modifications, deletions
     - Note related files that might need review (tests, documentation)

2. **Determine feature domain and read Spec**
   - **Determine feature domain:**
     - **Option 1**: Extract from branch name format `{type}/{TASK_KEY}` (e.g., `feat/FB-39` → fetch FB-39 from Jira to get feature context)
     - **Option 2**: Extract from PR title or description (look for feature keywords)
     - **Option 3**: Use `glob_file_search` with pattern `**/specs/*/spec.md` to list available specs, then prompt user if unclear
     - **If unable to determine automatically**: List available specs and ask user to specify feature domain
   - **Read Spec (if exists):**
     - Check if `specs/{FEATURE_DOMAIN}/spec.md` exists using `glob_file_search`
     - If exists:
       - Use `read_file` to read spec file
       - Extract **Blueprint** section (Context, Architecture, Anti-Patterns)
       - Extract **Contract** section (Definition of Done, Regression Guardrails, Scenarios)
     - If no spec found:
       - Note: "No Spec available for {FEATURE_DOMAIN} - will validate against Constitution only"
       - Proceed with Constitution-only validation

3. **Read Constitution**
   - Use `read_file` to read `AGENTS.md`
   - Extract **Operational Boundaries** section:
     - **Tier 1 (ALWAYS)**: Non-negotiable standards
     - **Tier 2 (ASK)**: High-risk operations requiring human approval
     - **Tier 3 (NEVER)**: Safety limits
   - Extract **Command Structure Standards** (if reviewing command file changes)
   - Store for Critic Agent context

### [CRITIC AGENT CONTEXT - FRESH SESSION]

4. **Invoke Critic Agent for Adversarial Review**
   - **Package context for Critic:**
     - Spec Blueprint + Contract (if exists)
     - AGENTS.md Operational Boundaries (Tier 1, Tier 2, Tier 3)
     - Code diff from Step 1
     - Changed files list
   - **Create fresh context session:**
     - **CRITICAL**: Critic Agent must have no bias from implementation
     - Use separate conversation or explicit context boundary
     - Critic Agent has not seen the implementation process, only the contracts and code
   - **Critic Agent prompt structure:**
     ```
     You are a Critic Agent performing Adversarial Code Review with dual-contract validation.
     
     **Your role**: Validate code against two contracts: Functional (Spec) and Architectural (Constitution). You have NOT been involved in building this code. Provide fresh, unbiased critique.
     
     **Spec Contract** (functional validation):
     [If spec exists at specs/{FEATURE_DOMAIN}/spec.md]
     ### Blueprint
     [Paste Context, Architecture, Anti-Patterns sections]
     
     ### Contract
     [Paste Definition of Done, Regression Guardrails, Scenarios sections]
     
     [If no spec]
     No Spec found for this feature - skip functional validation, proceed to Constitutional validation only.
     
     **Constitution** (architectural validation):
     [From AGENTS.md Operational Boundaries]
     ### Tier 1: ALWAYS (Must Follow)
     [Paste Tier 1 rules with full descriptions]
     
     ### Tier 2: ASK (Require Human Approval)
     [Paste Tier 2 rules with full descriptions]
     
     ### Tier 3: NEVER (Safety Limits)
     [Paste Tier 3 rules with full descriptions]
     
     **Code Changes** (git diff):
     [Paste full diff output showing all additions, deletions, modifications]
     
     **Files Changed**:
     [List of changed files with paths]
     
     **Task**: Perform dual-contract validation. For each violation found:
     1. **Category**: SPEC | CONSTITUTIONAL
     2. **Severity**: CRITICAL | WARNING | INFO
        - CRITICAL: Spec violations, Constitutional Tier 3 (NEVER) violations
        - WARNING: Spec warnings, Constitutional Tier 2 (ASK) violations
        - INFO: Spec suggestions, Constitutional Tier 1 (ALWAYS) violations
     3. **Description**: What was violated? (specific and clear)
     4. **Impact**: Why this matters (performance, security, maintainability, scalability)
     5. **Remediation**: Ordered steps to fix the violation (actionable)
     6. **Location**: File:Line reference where violation occurs
     7. **Reference**: Which Spec Contract criterion or Constitutional Boundary rule was violated
     
     **Output Format** (structured markdown):
     
     ## Code Review Report: [PASS | FAIL | WARNING]
     
     ### Summary
     - Spec Violations: X (Critical: Y, Warning: Z, Info: W)
     - Constitutional Violations: X (Critical: Y, Warning: Z, Info: W)
     - Gate Decision: PASS | FAIL | WARNING
     
     ---
     
     ## Spec Contract Violations
     
     ### Critical Issues 🔴
     [None] OR
     1. **Violation**: [Description]
        - **Impact**: [Why this matters]
        - **Remediation**: [Ordered steps to fix]
        - **Location**: [File:Line]
        - **Contract Reference**: [Which DoD/Guardrail/Scenario violated]
     
     ### Warnings 🟡
     [Similar format for WARNING severity violations]
     
     ### Info 🟢
     [Similar format for INFO severity violations]
     
     ---
     
     ## Constitutional Violations
     
     ### Tier 3 Violations (CRITICAL - NEVER) 🔴
     [None] OR
     1. **Violation**: [Description]
        - **Impact**: [Security, safety, or anti-pattern concern]
        - **Remediation**: [Ordered steps to fix]
        - **Location**: [File:Line]
        - **Boundary Reference**: [Which NEVER rule violated]
     
     ### Tier 2 Violations (WARNING - ASK) 🟡
     [Similar format for Tier 2 violations]
     
     ### Tier 1 Violations (INFO - ALWAYS) 🟢
     [Similar format for Tier 1 violations]
     
     ---
     
     ## Recommendation
     
     **[APPROVE | REQUEST CHANGES | COMMENT]**
     
     Rationale: [Explanation based on violations found]
     ```
   - **Model routing:**
     - Use reasoning-optimized model if available (e.g., o1, o3-mini for cost-effective reasoning)
     - Fallback to standard model if reasoning model unavailable
     - Note: Reasoning models excel at adversarial validation tasks

### [BUILDER AGENT CONTEXT]

5. **Parse violations and make gate decision**
   - **Parse Critic output:**
     - Extract **Spec violations** (if Spec exists):
       - Categorize by severity: CRITICAL/WARNING/INFO
       - Extract description, impact, remediation, location, contract reference
       - Count violations by severity
     - Extract **Constitutional violations**:
       - Categorize by tier: Tier 3 (CRITICAL), Tier 2 (WARNING), Tier 1 (INFO)
       - Extract description, impact, remediation, location, boundary reference
       - Count violations by tier
   - **Count total violations:**
     - Spec: Critical, Warning, Info counts
     - Constitutional: Tier 3, Tier 2, Tier 1 counts
   - **Gate Decision Logic:**
     - **FAIL** if:
       - Spec CRITICAL violations found (functional contract broken) OR
       - Constitutional Tier 3 (NEVER) violations found (safety limits violated)
     - **WARNING** if:
       - Spec WARNING violations found (functional concerns) OR
       - Constitutional Tier 2 (ASK) violations found (human approval required)
     - **PASS** if:
       - Only Spec INFO violations OR
       - Only Constitutional Tier 1 (ALWAYS) violations OR
       - No violations found
   - **Validation of Critic output:**
     - If Critic output is unparseable or malformed:
       - WARN user about parsing failure
       - Ask to retry or provide emergency override option
       - Do not fail silently

6. **Generate review report**
   - **Use structured format from Critic Agent:**
     - **Report header**: "Code Review Report: [PASS | FAIL | WARNING]"
     - **Summary section**:
       - Total violations by category (Spec + Constitutional)
       - Violation counts by severity
       - Gate decision with rationale
     - **Spec Contract Violations section** (if Spec exists):
       - Critical Issues 🔴 (Spec CRITICAL violations)
       - Warnings 🟡 (Spec WARNING violations)
       - Info 🟢 (Spec INFO violations)
     - **Constitutional Violations section**:
       - Tier 3 (CRITICAL - NEVER) 🔴
       - Tier 2 (WARNING - ASK) 🟡
       - Tier 1 (INFO - ALWAYS) 🟢
     - **Recommendation section**:
       - APPROVE (PASS) - No critical violations, ready to merge
       - REQUEST CHANGES (FAIL) - Critical violations must be fixed
       - COMMENT (WARNING) - Warnings flagged, human decision required
     - **Each violation includes**:
       - Description (what was violated)
       - Impact (why it matters)
       - Remediation steps (how to fix)
       - Location (File:Line)
       - Reference (Spec criterion or Constitutional boundary)
   - **Backward compatibility:**
     - If no Spec exists and no Constitutional violations: Include general code quality observations
     - If parsing Critic output fails: Fall back to basic review with clear error message

## Tools

### MCP Tools (GitHub)
- GitHub MCP tools - Verify GitHub MCP connection and retrieve PR/branch information
  - Use to validate GitHub MCP is configured and accessible
  - Use to retrieve PR details, changed files, and diffs
  - **If connection fails, STOP workflow - GitHub MCP is required for PR operations**

### MCP Tools (Atlassian)
- `getJiraIssue` - Fetch Jira issue details (if extracting feature domain from task key)
  - Parameters: `cloudId`, `issueIdOrKey` = {TASK_KEY}
  - Use to extract feature context when branch name is `{type}/{TASK_KEY}`

### Codebase Tools
- `codebase_search` - Find related code and understand context
  - Query: "How is [similar feature] implemented?"
  - Query: "Where is [component] used?"
  - Query: "What are the patterns for [error handling/testing/API design] in this codebase?"
  - Use to understand codebase patterns, find similar implementations, and ensure consistency

### Filesystem Tools
- `read_file` - Read changed files, Spec, and Constitution
  - Read changed code files for full context
  - Read `specs/{FEATURE_DOMAIN}/spec.md` (if exists)
  - Read `AGENTS.md` for Operational Boundaries
- `glob_file_search` - Find available specs
  - Pattern: `**/specs/*/spec.md` - List all available specs
  - Use to help determine feature domain or list options for user

### Terminal Tools
- `run_terminal_cmd` - Execute git commands for branch operations
  - `git branch -a` - List all branches (local and remote)
  - `git diff main...{BRANCH_NAME}` - Get diff between main and branch
  - `git diff --name-only main...{BRANCH_NAME}` - List changed files between main and branch
  - `git log {BRANCH_NAME} ^main` - View commit history on branch

## Pre-flight Checklist
- [ ] MCP status validation performed (GitHub MCP connection verified, see `mcp-status.md`)
- [ ] PR ({PR_KEY}) or branch ({BRANCH_NAME}) is accessible and exists
- [ ] {PR_KEY} normalized to numeric ID if PR review (extract from PR-12, #12, or 12)
- [ ] Changed files retrieved and readable
- [ ] Scope of changes understood (file count, line count, change types)
- [ ] Feature domain determined (for Spec lookup)
- [ ] Spec read (if exists) - Blueprint and Contract sections extracted
- [ ] Constitution read (AGENTS.md Operational Boundaries extracted)
- [ ] Critic Agent context packaged (Spec + Constitution + Code diff)

## Review Checklist
- [ ] All changed files reviewed
- [ ] Spec Contract validated (if Spec exists) - Blueprint and Contract checked
- [ ] Constitutional boundaries validated (AGENTS.md 3-tier system checked)
- [ ] Dual-contract violations identified and categorized
- [ ] Spec violations categorized by severity (CRITICAL/WARNING/INFO)
- [ ] Constitutional violations categorized by tier (Tier 3/Tier 2/Tier 1)
- [ ] Gate decision made (PASS/FAIL/WARNING) based on violation severity
- [ ] Remediation paths provided for all violations
- [ ] Violation locations specified (File:Line references)
- [ ] Contract/Boundary references included for all violations
- [ ] Review report generated with structured format
- [ ] Approval recommendation made (APPROVE/REQUEST CHANGES/COMMENT)

## Guidance

### Role
Act as a **Builder Agent** responsible for orchestrating adversarial code review. You retrieve context, package information, and coordinate with the Critic Agent. You are systematic, thorough, and enforce the Review Gate pattern with dual-contract validation.

### Instruction
Execute the adversarial review-code workflow to perform comprehensive code review with dual-contract validation. This includes:
1. Retrieving PR/branch changes and understanding scope
2. Determining feature domain and reading Spec (if exists)
3. Reading Constitution (AGENTS.md Operational Boundaries)
4. Packaging context for Critic Agent (no judgment at this stage)
5. Invoking Critic Agent in fresh context session for validation
6. Parsing Critic output and categorizing violations
7. Making gate decision (PASS/FAIL/WARNING) based on violation severity
8. Generating structured review report with remediation paths

### Context
- **Adversarial Code Review**: Builder/Critic separation prevents implementation bias
- **Fresh Context Session**: Critic Agent has no knowledge of implementation, only contracts and code
- **Dual-Contract Validation**: Functional (Spec) + Architectural (Constitution) validation
- **Review Gate**: PASS/FAIL/WARNING decisions, not just suggestions
- **Spec (if exists)**: Permanent living specification at `specs/{FEATURE_DOMAIN}/spec.md`
- **Constitution**: AGENTS.md Operational Boundaries (3-tier system)
- **Backward Compatible**: Works without Spec (Constitution-only validation)
- **Model Routing**: Prefer reasoning models (o1, o3-mini) for Critic Agent if available
- The review may be for a GitHub Pull Request ({PR_KEY}) or a local/remote branch ({BRANCH_NAME})
- {PR_KEY} can be specified in multiple formats (PR-12, #12, or 12) and should be normalized to numeric ID
- {BRANCH_NAME} follows `{type}/{TASK_KEY}` format for feature branches (consistent with other commands)
- GitHub MCP integration provides access to PR data, diffs, and file lists

### Examples

**Example 1: Review Pull Request with Spec Validation**
```
Input: /review-code PR-12
Process:
1. Normalize PR-12 to numeric ID: 12
2. Use GitHub MCP to get PR details, changed files, and diff
3. Determine feature domain from PR title/branch (e.g., "user-authentication")
4. Read specs/user-authentication/spec.md (Blueprint + Contract)
5. Read AGENTS.md Operational Boundaries
6. Package context for Critic Agent
7. Invoke Critic Agent in fresh context (dual-contract validation)
8. Parse Critic output: Spec violations + Constitutional violations
9. Make gate decision: FAIL if CRITICAL violations or Tier 3 violations
10. Generate structured review report with remediation paths
```

**Example 2: Review Branch without Spec (Constitution-only)**
```
Input: /review-code feat/FB-12
Process:
1. Verify branch exists using git commands
2. Get diff using git diff main...feat/FB-12
3. Get changed files using git diff --name-only
4. Attempt to determine feature domain, no spec found
5. Read AGENTS.md Operational Boundaries
6. Package context for Critic Agent (Constitution only)
7. Invoke Critic Agent for Constitutional validation
8. Parse Critic output: Constitutional violations only
9. Make gate decision based on Constitutional violations
10. Generate review report noting "No Spec - validated against Constitution only"
```

**Example 3: {PR_KEY} Normalization**
```
Input formats and normalization:
- PR-12 → 12 (extract numeric ID)
- #12 → 12 (remove # prefix)
- 12 → 12 (already numeric)
All formats result in pullNumber=12 for API calls
```

### Constraints

**Rules (Must Follow):**
1. **Fresh Context Requirement**: Critic Agent MUST use separate context session with no implementation bias. Builder Agent packages context, Critic Agent validates.
2. **Dual-Contract Validation**: Validate against BOTH Spec (if exists) and AGENTS.md Constitution. Never validate against only one when both are available.
3. **Gate Decision Logic**: 
   - FAIL on Spec CRITICAL violations OR Constitutional Tier 3 violations
   - WARNING on Spec WARNING violations OR Constitutional Tier 2 violations
   - PASS on Spec INFO violations OR Constitutional Tier 1 violations OR no violations
4. **Structured Violation Reports**: Every violation MUST include: Description, Impact, Remediation, Location, Reference.
5. **Backward Compatibility**: Works without Spec (Constitution-only validation). Never fail if Spec doesn't exist.
6. **MCP Validation**: GitHub MCP connection is required. If validation fails, STOP and report the failure (see `mcp-status.md`).
7. **{PR_KEY} Normalization**: Always normalize {PR_KEY} to numeric ID (extract from PR-12, #12, or 12 format) before making API calls.
8. **Reasoning Model Preference**: Use reasoning-optimized model (o1, o3-mini) for Critic Agent if available. These models excel at adversarial validation.
9. **No Implementation Bias**: Critic Agent must NOT have access to implementation history, discussions, or rationale. Only contracts and code.
10. **Actionable Remediation**: Every violation must include specific, ordered steps to fix. No vague suggestions like "improve code quality."

**Existing Standards (Reference):**
- MCP status validation: See `mcp-status.md` for detailed MCP server connection checks
- Spec structure: See `specs/README.md` for Blueprint + Contract format
- Constitution: See `AGENTS.md` Operational Boundaries for 3-tier system
- Branch naming: Type prefix format (`{type}/{TASK_KEY}`) as shown in `start-task.md`
- ASDLC patterns: Adversarial Code Review, Constitutional Review, Context Gates, The Spec, Agent Constitution

### Output
1. **Review Report**: Comprehensive report containing:
   - Summary: Gate decision (PASS/FAIL/WARNING) with violation counts
   - Spec Contract Violations section (if Spec exists):
     - Critical Issues 🔴 (Spec CRITICAL)
     - Warnings 🟡 (Spec WARNING)
     - Info 🟢 (Spec INFO)
   - Constitutional Violations section:
     - Tier 3 (CRITICAL - NEVER) 🔴
     - Tier 2 (WARNING - ASK) 🟡
     - Tier 1 (INFO - ALWAYS) 🟢
   - Each violation includes:
     - Description (what was violated)
     - Impact (why it matters)
     - Remediation (ordered steps to fix)
     - Location (File:Line)
     - Reference (Spec criterion or Constitutional boundary)
   - Recommendation: APPROVE/REQUEST CHANGES/COMMENT with rationale
2. **Gate Decision**: Clear PASS/FAIL/WARNING decision based on violation severity
3. **Actionable Remediation**: Specific steps to fix all violations
