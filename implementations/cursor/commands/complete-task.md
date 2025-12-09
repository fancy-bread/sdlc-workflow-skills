# Complete Task

## Overview
Commit changes, push to remote, create pull request, and transition issue to "Code Review" status.

## Steps
1. **Prepare commit**
   - Check for linting errors and fix
   - Stage all changes
   - Create conventional commit message
   - Format: `{type}: {description} ({TASK_KEY})`
   - Types: feat, fix, refactor, docs, test, chore

2. **Push changes**
   - Commit staged changes
   - Push to remote branch
   - Wait for automated verification (build, tests, coverage)

3. **Create pull request**
   - Add completed checklist comment to issue
   - Create PR with plan summary
   - Include verification status in PR body
   - Link PR to issue

4. **Update issue**
   - Transition issue to "Code Review" status
   - Add PR link comment to issue

## Completion Checklist
- [ ] Linting errors fixed
- [ ] Changes staged
- [ ] Commit message follows convention
- [ ] Changes committed
- [ ] Pushed to remote
- [ ] Automated checks pass
- [ ] Completed checklist added to issue
- [ ] PR created with plan summary
- [ ] Issue transitioned to "Code Review"
- [ ] PR link added to issue
