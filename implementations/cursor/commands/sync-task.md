# Sync Task

## Overview
Check pull request status and automatically update issue status when PR is merged or closed.

## Steps
1. **Find associated PR**
   - Search for PR by task key in title/body
   - Or search by branch name
   - Retrieve PR details

2. **Check PR status**
   - Get current PR state (merged/closed/open)
   - Determine appropriate action

3. **Update issue based on status**
   - **If Merged**:
     - Transition issue to "Done"
     - Add completion comment
   - **If Closed (not merged)**:
     - Add warning comment
     - Keep current status
   - **If Open**:
     - Add status comment
     - No status change

## Sync Checklist
- [ ] PR found by task key or branch
- [ ] PR status retrieved
- [ ] Issue updated appropriately:
  - [ ] Merged: Transitioned to "Done" + comment
  - [ ] Closed: Warning comment added
  - [ ] Open: Status comment added
