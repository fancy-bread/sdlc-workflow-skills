---
title: /create-epic
---

# /create-epic

Create epics from plan documents with generated stories.

| | |
|---|---|
| **Roles** | Product Manager, Staff Engineer |
| **Frequency** | Weekly / Occasional |
| **Prerequisites** | Epic plan document |

---

## What It Does

Reads plan document, creates epic with description, generates child stories, links everything.

---

## Usage

```bash
/create-epic from [plan-file.md]
```

---

## Example

```
You: /create-epic from oauth-implementation.md

AI:
✓ Reading oauth-implementation.md...
✓ Creating epic PROJ-100: OAuth Authentication
✓ Generating child stories...
  - PROJ-101: OAuth provider setup
  - PROJ-102: Login flow
  - PROJ-103: Token refresh
  - PROJ-104: Logout handling
✓ Linked 4 stories to epic
```

---

## Command Definition

```markdown
# Create Epic

## Overview
Create an epic and its child stories from a plan document.

## Steps
1. **Read plan document**
   - Parse markdown plan file
   - Extract epic description
   - Identify story breakdown

2. **Create epic**
   - Generate epic title and description
   - Set epic priority and labels
   - Create in issue tracker

3. **Generate child stories**
   - Create stories from plan sections
   - Add acceptance criteria
   - Link to parent epic
   - Set appropriate priorities

4. **Link and organize**
   - Link stories to epic
   - Add story order/sequence
   - Post plan document as comment

## Epic Checklist
- [ ] Plan document read
- [ ] Epic created with description
- [ ] Child stories generated
- [ ] Stories linked to epic
- [ ] Plan attached as comment
```

**[View Full Command →](../implementations/cursor/commands/create-epic.md)**

---

## Used By

- **[Product Manager](../roles/product-manager.md)** - Major initiatives
- **[Staff Engineer](../roles/engineer.md)** - Technical initiatives

---

## Related Commands

**Before:** [`/create-story`](create-story.md) - Individual stories

---

[:octicons-arrow-left-24: Back to Commands](../index.md)

