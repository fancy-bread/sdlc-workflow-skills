---
title: /create-story
---

# /create-story

Create user stories with AI-generated acceptance criteria.

| | |
|---|---|
| **Roles** | Product Manager |
| **Frequency** | Daily |
| **Prerequisites** | Feature request or requirement |

---

## What It Does

Analyzes feature request, generates story with acceptance criteria, creates in issue tracker.

---

## Usage

```bash
/create-story for [feature description]
```

---

## Example

```
You: /create-story for user login with email and password

AI:
✓ Analyzing feature scope...
✓ Generating story details...
✓ Created PROJ-123: User Email/Password Login

  Acceptance Criteria:
  - Users can enter email and password
  - Invalid credentials show error
  - Successful login redirects to dashboard
  - "Forgot password" link visible
```

---

## Command Definition

```markdown
# Create Story

## Overview
Create a new story in the issue tracker from a feature request or requirement.

## Steps
1. **Analyze the request**
   - Understand the feature scope and goals
   - Identify acceptance criteria
   - Determine priority level

2. **Generate story details**
   - Write clear, descriptive title
   - Create comprehensive description
   - Define acceptance criteria
   - Add relevant labels and tags

3. **Create in issue tracker**
   - Create story with generated content
   - Set appropriate priority
   - Link to parent epic if applicable
   - Leave unassigned in "To Do" status

## Story Checklist
- [ ] Title is clear and descriptive
- [ ] Description includes context and motivation
- [ ] Acceptance criteria are well-defined
- [ ] Priority is set appropriately
- [ ] Labels/tags are added
- [ ] Linked to epic if applicable
```

**[View Full Command →](../../implementations/cursor/commands/product/create-story.md)**

---

## Used By

- **[Product Manager](../../roles/product-manager.md)** - Primary (daily)
- **[Staff Engineer](../../roles/engineer.md)** - Technical initiatives

---

## Related Commands

**Scale up:** [`/create-epic`](create-epic.md) - Create epic
**Plan:** [`/create-task-plan`](../development/create-task-plan.md) - Design implementation

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

