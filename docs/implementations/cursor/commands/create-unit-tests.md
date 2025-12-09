# Write Unit Tests

## Overview
Generate unit tests for a specific function, class, or module to verify it works correctly in isolation.

## Steps
1. **Analyze code to test**
   - Read function/class implementation
   - Identify inputs and outputs
   - Understand expected behavior
   - Review existing tests (if any)

2. **Identify test cases**
   - Happy path (expected inputs)
   - Edge cases (boundary conditions)
   - Error cases (invalid inputs)
   - State transitions
   - Special values (null, zero, empty, etc.)

3. **Generate test code**
   - Use project's test framework
   - Follow naming conventions
   - Use Arrange-Act-Assert pattern
   - Include descriptive test names
   - Add comments for complex scenarios

4. **Run tests**
   - Execute new tests
   - Verify all pass
   - Check coverage contribution

5. **Review and refine**
   - Ensure tests are independent
   - Verify tests are deterministic
   - Check test clarity and readability
   - Add missing test cases if needed

## Unit Test Checklist
- [ ] Code to test analyzed
- [ ] Test cases identified:
  - [ ] Happy path
  - [ ] Edge cases
  - [ ] Error cases
- [ ] Tests generated with clear names
- [ ] Tests follow AAA pattern
- [ ] Tests are independent
- [ ] Tests are fast (< 100ms each)
- [ ] All tests pass
- [ ] Coverage increased

