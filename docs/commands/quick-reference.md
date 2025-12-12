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
├── Product (2)
│   ├── /create-task
│   └── /breakdown-tasks
│
├── Development (3)
│   ├── /create-plan
│   ├── /start-task
│   └── /complete-task
│
└── Quality (2)
    ├── /create-test
    └── /review-code
│
└── Utilities (1)
    └── /mcp-status
```

**8 commands total**

---

## Product Management

```bash
# Create user story
/create-task --type=story for [feature description]

# Create epic from plan
/create-task --type=epic from [plan-file.md]

# Break down large task into subtasks
/breakdown-tasks TASK-123

# Create bug
/create-task --type=bug [description]
```

---

## Development

```bash
# Design implementation
/create-plan for TASK-123

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
```

---

## By Role

**Product Manager:**
```bash
/create-task --type=story for [feature]
/create-task --type=epic from [plan.md]
/breakdown-tasks TASK-123
```

**Engineer (Daily):**
```bash
/create-plan for TASK-123
/start-task TASK-123
/complete-task TASK-123
```

**QA:**
```bash
/create-test --type=unit for ClassName
```

---

[:octicons-arrow-left-24: Back to Commands](index.md)
