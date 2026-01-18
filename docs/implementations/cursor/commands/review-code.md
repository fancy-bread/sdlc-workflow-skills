# Review Code

## Overview
Perform adversarial AI-assisted code review on a pull request or branch changes using Builder/Critic separation with dual-contract validation (Spec + Constitution).

## Usage

```
/review-code {PR_KEY}
/review-code {BRANCH_NAME}
```

## Parameters

- `{PR_KEY}`: Pull Request identifier (e.g., `PR-12`, `#12`, `12`)
- `{BRANCH_NAME}`: Branch name (e.g., `feat/FB-39`)

## What It Does

This command performs adversarial code review using:

1. **Builder/Critic Separation**: Fresh Critic Agent context prevents implementation bias
2. **Dual-Contract Validation**: 
   - **Functional** (Spec): Validates against Blueprint + Contract
   - **Architectural** (Constitution): Validates against AGENTS.md 3-tier system
3. **Review Gate**: PASS/FAIL/WARNING decisions (not just suggestions)
4. **Structured Violation Reports**: Description, Impact, Remediation, Location, Reference

## How It Works

### Builder Agent (Context Packaging)
1. Retrieves PR/branch changes
2. Determines feature domain
3. Reads Spec (if exists)
4. Reads AGENTS.md Constitution
5. Packages context for Critic Agent

### Critic Agent (Fresh Context)
6. Performs dual-contract validation
7. Identifies violations
8. Generates structured violation reports

### Builder Agent (Gate Decision)
9. Parses Critic output
10. Makes gate decision (PASS/FAIL/WARNING)
11. Generates review report with remediation

## Gate Decision Logic

- **FAIL**: Spec CRITICAL violations OR Constitutional Tier 3 violations
- **WARNING**: Spec warnings OR Constitutional Tier 2 violations
- **PASS**: Only INFO violations OR no violations

## Examples

### Review Pull Request
```
/review-code PR-42
/review-code #42
/review-code 42
```

### Review Branch
```
/review-code feat/FB-39
/review-code fix/security-patch
```

## Output

### PASS Example
```
## Code Review Report: PASS

### Summary
- Spec Violations: 0
- Constitutional Violations: 1 (Info: 1)
- Gate Decision: PASS

### Constitutional Violations
#### Tier 1 (INFO - ALWAYS) 🟢
1. **Violation**: Missing JSDoc on public function
   - **Impact**: Documentation clarity
   - **Remediation**: Add JSDoc comment
   - **Location**: auth/validator.ts:23

### Recommendation
**APPROVE** - No critical violations found.
```

### FAIL Example
```
## Code Review Report: FAIL

### Summary
- Spec Violations: 1 (Critical: 1)
- Constitutional Violations: 1 (Critical: 1)
- Gate Decision: FAIL

### Spec Contract Violations
#### Critical Issues 🔴
1. **Violation**: Missing input validation for OAuth callback
   - **Impact**: Security vulnerability (open redirect)
   - **Remediation**:
     1. Add URL validation
     2. Whitelist allowed domains
     3. Reject non-matching URLs
   - **Location**: auth/service.ts:45

### Constitutional Violations
#### Tier 3 (CRITICAL - NEVER) 🔴
1. **Violation**: Hardcoded API secret in source
   - **Impact**: Credentials exposed in version control
   - **Remediation**:
     1. Remove secret from code
     2. Add to .env file
     3. Load from environment
   - **Location**: auth/config.ts:8

### Recommendation
**REQUEST CHANGES** - Critical violations must be fixed.
```

## See Also

- [Spec Structure](../specs/README.md) - Blueprint + Contract format
- [AGENTS.md](../../AGENTS.md) - Constitution (Operational Boundaries)
- [Complete Task](complete-task.md) - Includes Constitutional Review before PR
- [MCP Status](mcp-status.md) - Verify MCP connections
