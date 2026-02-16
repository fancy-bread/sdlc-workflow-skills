---
name: create-release
description: Create a git tag for a release version with a detailed commit message
disable-model-invocation: true
---

# Create Release

## Overview
Prepare a release by updating CHANGELOG (promote [Unreleased] to the new version with date), committing that change, then creating an annotated git tag. The release workflow (triggered by pushing the tag) **reads** the CHANGELOG section from the tagged commit for GitHub release notes and **updates** docs/releases.md on main itself—so only CHANGELOG is updated before the tag.

## Definitions

- **{VERSION}**: Release version following semantic versioning (e.g., `v1.0.0`, `v1.1.0`, `v2.0.0`)
  - Must start with `v` prefix
  - Format: `vMAJOR.MINOR.PATCH`
- **Tag Message**: Simple commit message in format: `Release {VERSION} - {DATE}`

## Prerequisites

Before proceeding, verify:

1. **Working Directory**: Ensure you're in the repository root directory
   - **If not in repository root, STOP and change to repository root directory.**
   - **Git Operation Standards**: Git operations should follow best practices. These standards are documented in AGENTS.md §3 Operational Boundaries if AGENTS.md exists, but apply universally regardless.

2. **Git Status**: Verify working directory is clean (no uncommitted changes)
   - Check with `git status`
   - **If there are uncommitted changes, STOP and ask user if they want to commit them first or discard them.**

3. **Version Format**: Verify the version follows semantic versioning format
   - Must match pattern: `v[0-9]+\.[0-9]+\.[0-9]+`
   - **If version format is invalid, STOP and report error: "Invalid version format. Expected format: vMAJOR.MINOR.PATCH (e.g., v1.0.0)"**

4. **Tag Doesn't Exist**: Verify the tag doesn't already exist
   - Check with `git tag -l {VERSION}`
   - **If tag already exists, STOP and report error: "Tag {VERSION} already exists"**

## Usage

```
/create-release v1.0.0
```

**Examples:**
- `/create-release v1.0.0` (initial release)
- `/create-release v1.1.0` (minor release)
- `/create-release v2.0.0` (major release)

## Steps

1. **Validate Prerequisites**
   - Verify working directory is repository root
   - Check git status is clean
   - Validate version format matches `v[0-9]+\.[0-9]+\.[0-9]+`
   - Verify tag doesn't already exist
   - **If any prerequisite fails, STOP and report the error.**

2. **Get Release Date**
   - Get current date in format: YYYY-MM-DD

3. **Update CHANGELOG.md**
   - Open `CHANGELOG.md`. Find the **previous** release version (e.g. `1.1.5`) from the most recent `## [X.Y.Z]` heading or from the compare links at the bottom.
   - Promote `[Unreleased]` to the new version:
     - Replace the heading `## [Unreleased]` with `## [X.Y.Z] - {DATE}` where X.Y.Z is {VERSION} without the `v` (e.g. `v2.0.0` → `## [2.0.0] - 2026-02-03`).
     - Keep all content currently under `[Unreleased]` (Added, Changed, Removed, etc.) under this new version heading.
     - After that block, add `---`, then an empty `## [Unreleased]` section, then `---` before the next existing version.
   - Update the compare links at the bottom of the file:
     - Add a line `[X.Y.Z]: https://github.com/fancybread-com/standard-agent-skills/compare/v{PREV}...{VERSION}` (e.g. `[2.0.0]: ...compare/v1.1.5...v2.0.0`).
     - Set `[Unreleased]: https://github.com/fancybread-com/standard-agent-skills/compare/{VERSION}...HEAD` (e.g. `v2.0.0...HEAD`).
   - **If CHANGELOG.md is missing or structure differs, STOP and ask the user.**

4. **Commit CHANGELOG**
   - Stage `CHANGELOG.md` only.
   - Commit with message: `chore(release): prepare {VERSION}`
   - **Do NOT push** — the user will push commit and tag together.

5. **Create Git Tag**
   - Create an annotated tag on the current commit: `git tag -a {VERSION} -m "Release {VERSION} - {DATE}"`
   - **If tag creation fails, STOP and report the error.**
   - **Do NOT push the tag** — the user will push it to trigger the release workflow.

6. **Report Success**
   - Confirm CHANGELOG updated and committed, and tag created.
   - Give push instructions:
     ```
     Release {VERSION} prepared (CHANGELOG committed, tag created).

     Push the commit and tag to trigger the release workflow:
     git push origin main
     git push origin {VERSION}

     The workflow will: create the GitHub release (using the CHANGELOG section as notes), attach skills archives, update docs/releases.md on main, and deploy docs.
     ```

## Tools

### Filesystem Tools
- `run_terminal_cmd` - Execute git commands and get current date

### Git Commands
- `git status` - Check working directory status
- `git tag -l {VERSION}` - List existing tags
- `git tag -a {VERSION} -m "{MESSAGE}"` - Create annotated tag with message

## Guidance

### Role
**Project Maintainer / Release Manager**

### Instruction
Create a git tag for a release with a comprehensive message describing the current command set state. This tag will be used by the automated release workflow to generate release notes and documentation updates.

### Context
- Skills are in `skills/` (each skill is `skills/<name>/SKILL.md`).
- The release workflow (`.github/workflows/create-release.yml`) runs on tag push. It:
  - **Reads** CHANGELOG from the tagged commit and uses the section for that version (e.g. `## [2.0.0]`) as the GitHub release notes (fallback: tag message).
  - Creates skills archives, creates the GitHub release, uploads assets.
  - **Checks out main** and runs a script to **update docs/releases.md** (add new version to Latest Release and Release History), then commits and pushes that to main.
- So: only **CHANGELOG** is updated before the tag (in this skill). **releases.md** is updated by the workflow after the tag.

### Examples

**Example 1: Initial Release**
```
Input: /create-release v1.0.0

Output:
Tag v1.0.0 created successfully.

Tag message: Release v1.0.0 - 2025-12-21

To release, push the tag:
git push origin v1.0.0
```

### Constraints

**Rules (Must Follow):**
1. **Operational Standards Compliance**: This command follows operational standards (documented in AGENTS.md if present, but apply universally):
   - **Git Operations**: Follow best practices for git tag operations
   - **Safety Limits**: Never commit secrets, API keys, or sensitive data in tag messages
   - **AGENTS.md Optional**: Commands work without AGENTS.md. Standards apply regardless of whether AGENTS.md exists.
   - See AGENTS.md §3 Operational Boundaries (if present) for detailed standards
2. **Version Format**: Version must start with `v` and follow semantic versioning (vMAJOR.MINOR.PATCH)
3. **Clean Working Directory**: Do not create tags if there are uncommitted changes without user confirmation
4. **Tag Uniqueness**: Verify tag doesn't already exist before creating
5. **Message Format**: Use simple format "Release {VERSION} - {DATE}"
6. **No Auto-Push**: Do NOT automatically push the tag - let user push manually
7. **Error Handling**: STOP and report errors clearly if any step fails

**Existing Standards (Reference):**
- Semantic versioning: MAJOR.MINOR.PATCH format
- Git tags: Annotated tags (-a flag) with messages (-m flag)
- Command organization: Grouped by category (Product, Planning, Development, Quality, Utilities)

### Output

1. **Git Tag**: Annotated tag created with version `{VERSION}`
2. **Tag Message**: Simple release message in format "Release {VERSION} - {DATE}"
3. **Success Report**: Confirmation message with instructions to push the tag

The command updates CHANGELOG, commits, then creates the tag. The workflow reads that CHANGELOG section for release notes and updates docs/releases.md on main.
