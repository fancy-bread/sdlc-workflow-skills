---
title: Quick Reference
---

# Command Quick Reference

**Copy-paste ready commands.**

[:octicons-list-unordered-24: All Commands](index.md){ .md-button }
[:octicons-person-24: By Role](by-role.md){ .md-button }

---

## Command Organization

```
agentic-software-development/
├── Product
│   ├── /create-task
│   └── /decompose-task
│
├── Planning
│   ├── /refine-task
│   └── /create-plan
│
├── Development
│   ├── /start-task
│   └── /complete-task
│
├── Quality
│   ├── /create-test
│   └── /review-code
│
└── Utilities
    ├── /mcp-status
    └── /setup-asdlc
```

---

## Product Management

```bash
# Create user story
/create-task --type=story for [feature description]

# Create epic from plan
/create-task --type=epic from [plan-file.md]

# Decompose large task into subtasks
/decompose-task TASK-123

# Create bug
/create-task --type=bug [description]
```

---

## Planning

```bash
# Refine task for sprint planning
/refine-task TASK-123

# Design implementation
/create-plan for TASK-123
```

## Development

```bash
# Start work
/start-task TASK-123

# Ship it
/complete-task TASK-123
```

---

## Quality

```bash
# Write tests
/create-test --type=unit for ClassName

# Review code
/review-code for PR #42
```

---

## Utilities

```bash
# Check MCP server status
/mcp-status

# Initialize repository for ASDLC
/setup-asdlc
```

---

## By Role

Commands organized by who uses them: [View by Role →](by-role.md)

---

[:octicons-arrow-left-24: Back to Commands](index.md)
