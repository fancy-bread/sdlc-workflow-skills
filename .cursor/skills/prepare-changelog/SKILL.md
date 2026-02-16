---
name: prepare-changelog
description: Prepare Changelog
disable-model-invocation: true
---

# Prepare Changelog

## Overview

Prepare `CHANGELOG.md` for a new release: list everything changed since the last tagged release, create a branch, update the CHANGELOG, and optionally commit, push, and open a PR. No Jira required.

## Definitions

- **Last tag**: The most recent version tag (e.g. `v2.0.0`) from `git tag -l 'v*' --sort=-v:refname`. Used as the range start for "what changed."
- **New version**: The version being prepared (e.g. `2.0.1` or `2.1.0`). User can specify or agent suggests next patch/minor from last tag.
- **Branch name**: `chore/release-{VERSION}` (e.g. `chore/release-2.0.1`). Created from `main`; no issue key required.
- **CHANGELOG.md**: Root file following [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Contains `## [Unreleased]`, version sections `## [X.Y.Z] - YYYY-MM-DD`, and footer links.

## Prerequisites

1. **Repository state**: Current branch should be `main` or a branch you will leave (agent will create a new branch from `main`). No uncommitted CHANGELOG changes that would be lost.
2. **Git**: Tags exist (at least one `v*` tag). If no tags, STOP and report.
3. **GitHub (for PR)**: If completing with PR, GitHub MCP or push access required. Optional for "list changes and branch only" flow.

## Steps

1. **Determine last tag and range**
   - Run `git fetch --tags` (if needed), then get latest version tag: `git tag -l 'v*' --sort=-v:refname | head -1`.
   - If no tag found, STOP and report: "No version tags (v*) found. Create a tag first or run from a repo that has releases."
   - Set `LAST_TAG` to that value (e.g. `v2.0.0`).

2. **List everything changed since last tag**
   - Commits: `git log {LAST_TAG}..HEAD --oneline` (or `--pretty=format:...` for subject only).
   - Optionally group by conventional type: `git log {LAST_TAG}..HEAD --pretty=format:"%s"` and categorize by `feat:`, `fix:`, `docs:`, `chore:`, etc.
   - Optionally list files changed: `git diff --stat {LAST_TAG}..HEAD` or `git diff --name-only {LAST_TAG}..HEAD`.
   - Present a clear summary: number of commits, list of commit subjects, and optionally file list or type breakdown so the user can draft Added/Changed/Fixed/Removed entries.

3. **Propose or ask for new version**
   - Parse `LAST_TAG` (e.g. `v2.0.0` → 2.0.0). Suggest next patch: 2.0.1; or ask user: "Next version? (e.g. 2.0.1 patch, 2.1.0 minor)."
   - Set `NEW_VERSION` (e.g. `2.0.1`) and `TAG_NAME` (e.g. `v2.0.1`).

4. **Create branch**
   - Ensure on `main` and up to date: `git checkout main`, `git pull origin main` (or equivalent).
   - Branch name: `chore/release-{NEW_VERSION}` (e.g. `chore/release-2.0.1`).
   - Check if branch already exists locally or remotely; if it exists, ask user whether to use it or pick another name.
   - Create and checkout: `git checkout -b chore/release-{NEW_VERSION}`.
   - Report: "Branch created: chore/release-{NEW_VERSION}."

5. **Update CHANGELOG.md**
   - Read current `CHANGELOG.md` (especially `## [Unreleased]` and the footer links).
   - Add a new version section: `## [{NEW_VERSION}] - YYYY-MM-DD` (use today's date or user-provided).
   - Populate it from the "what changed" list: group into **Added**, **Changed**, **Fixed**, **Removed** as appropriate; use commit subjects and file changes to draft bullet points. If `[Unreleased]` had content, merge or move it into this section.
   - Leave `## [Unreleased]` empty (or with a placeholder) for future changes.
   - Update footer:
     - `[Unreleased]`: `https://github.com/{owner}/{repo}/compare/v{NEW_VERSION}...HEAD`.
     - Add line: `[{NEW_VERSION}]: https://github.com/{owner}/{repo}/releases/tag/v{NEW_VERSION}`.
   - Write the updated content to `CHANGELOG.md`. If owner/repo are not known, use placeholders and remind user to replace (e.g. from README or remote URL).

6. **Complete: commit, push, create PR**
   - Stage: `git add CHANGELOG.md`.
   - Commit: `git commit -m "chore(release): prepare CHANGELOG for v{NEW_VERSION}"`.
   - Push: `git push -u origin chore/release-{NEW_VERSION}`.
   - Create PR: use GitHub MCP `mcp_github_create_pull_request` with base `main`, head `chore/release-{NEW_VERSION}`, title `chore(release): prepare CHANGELOG for v{NEW_VERSION}`, body summarizing the version and link to compare view (e.g. `.../compare/v{LAST}...v{NEW_VERSION}`).
   - If push or PR creation fails, STOP and report the error.

**Variants**

- **List only:** Run steps 1–2 and present the "what changed" summary; stop. User can then run again with "create branch and update CHANGELOG" or "and open PR."
- **Branch and edit only:** Run steps 1–5; do not commit. User edits CHANGELOG, then runs again with "commit and open PR" or uses `/complete-task`-like flow manually.
- **Full flow:** Run steps 1–6 (list, branch, update CHANGELOG, commit, push, PR). User merges PR; then they tag from `main` after merge.

## Tools

### Git / Terminal

- `git fetch --tags` — Ensure tags are up to date.
- `git tag -l 'v*' --sort=-v:refname` — List version tags, newest first.
- `git log {tag}..HEAD --oneline` — Commits since tag.
- `git log {tag}..HEAD --pretty=format:"%s"` — Commit subjects only (for grouping).
- `git diff --stat {tag}..HEAD`, `git diff --name-only {tag}..HEAD` — Files changed since tag.
- `git checkout main`, `git pull origin main` — Ensure main is current.
- `git checkout -b chore/release-{VERSION}` — Create release branch.
- `git add CHANGELOG.md`, `git commit -m "..."`, `git push -u origin chore/release-{VERSION}` — Commit and push.

### Filesystem

- `read_file` — Read `CHANGELOG.md`, `README.md` (for repo URL/owner).
- `write` or `search_replace` — Update `CHANGELOG.md` with new version section and footer links.

### MCP (GitHub)

- `mcp_github_list_branches` — Check if `chore/release-*` already exists.
- `mcp_github_create_branch` — Optional: create branch on remote first.
- `mcp_github_create_pull_request` — Create PR from `chore/release-{VERSION}` to `main` after push.
- Owner/repo: resolve from `git remote get-url origin` or README (e.g. fancybread-com/sdlc-workflow-skills).

## Guidance

### Role

Act as a **release helper**: you list changes since the last tag, create a release-prep branch, update CHANGELOG in Keep a Changelog format, and optionally complete by committing, pushing, and opening a PR. No Jira or issue key required.

### Instruction

- Always determine the last tag and list changes first so the user (and the CHANGELOG) reflect reality.
- Use branch name `chore/release-{VERSION}`; create from `main`.
- Follow [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and [Semantic Versioning](https://semver.org/) for the new version and section.
- If the user only wants "what changed," do steps 1–2 and stop. If they want the full flow, do 1–6 (including commit, push, PR).

### Context

- The Create Release workflow (`.github/workflows/create-release.yml`, triggered by pushing a tag) reads the version section from `CHANGELOG.md` on the tagged commit. So the CHANGELOG update must be merged to `main` before the user tags; this skill prepares that update via a PR.
- No Jira ticket is required; the branch is `chore/release-X.Y.Z` only.

### Constraints

- Do not push to `main` directly; use a branch and PR.
- Do not create a tag in this skill; the user tags after the CHANGELOG PR is merged.
- If no `v*` tags exist, STOP and report.

### Output

1. **List of changes:** Commits (and optionally files) since last tag.
2. **Branch:** `chore/release-{VERSION}` created from `main`.
3. **CHANGELOG.md:** New version section and updated footer links; optional commit + push + PR.
