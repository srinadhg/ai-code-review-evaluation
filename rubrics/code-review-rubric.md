# Code Review Rubric

Score each criterion **Pass / Partial / Fail**, and back each score with evidence (a failing input, an error message, a line number, or a test result).

| Criterion | What to check | How to verify |
|---|---|---|
| **Requirement coverage** | Every item the requirement says must be handled works | Run each listed case |
| **Edge cases** | `None`, empty, invalid types, boundaries | Write and run extra inputs |
| **Reliability** | No crash on unexpected input; errors are raised or handled on purpose, not swallowed | Look for unguarded operations and bare `except` |
| **Test quality** | Tests cover edge cases, fail without the fix, and were not weakened to pass | Revert the fix and rerun; diff the tests |
| **Scope & maintainability** | Minimal change, no unrelated edits, readable | Compare the diff to what the task needs |

## Verdict

- **Correct:** every requirement item is met and no criterion is Fail.
- **Partially Correct:** the main use case works and the reported bug is fixed, but one or more requirement items or edge cases fail.
- **Incorrect:** the reported bug is not fixed, the main use case fails, the change introduces a new bug, or tests pass only because they were weakened or hardcoded.

When a judgment is close (for example, "must handle" items that fail but the main case works), state the reasoning in the review.
