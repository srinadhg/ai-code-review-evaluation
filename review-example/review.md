# Review for ai_generated_code.py

**Code origin:** hand-written to reproduce a common AI failure pattern (not real model output).

## Original Requirement
Handle None, empty list, None values inside the list, non-string values inside the list. Case-insensitive unique, preserve first-occurrence order.

## What works
`if not tags` handles `None` and `[]`, so the top-level crash is fixed. Case-insensitive de-duplication and order preservation are correct for clean input.

## Issues Found

1. **[High] None inside the list crashes.** For `["TagA", None, "taga"]`, `t.lower()` raises `AttributeError: 'NoneType' object has no attribute 'lower'`. The fix only guards the outer list, not the values. The requirement lists this case explicitly.

2. **[High] Non-string inside the list crashes.** For `["TagA", 123, "TagB"]`, it raises `AttributeError: 'int' object has no attribute 'lower'`. Real data is often dirty, and the requirement lists this case too.

3. **[Medium] The AI-generated solution was supplied without tests.** Nothing covers None-inside-list or invalid types; only the happy path was considered.The repository's evaluation tests expose the missing edge cases, but the original implementation did not include tests for them.

4. **[Nit] `if not tags` vs `if tags is None`.** Both behave correctly here. The explicit `is None` check is clearer about intent, but this does not affect the verdict.

## Evidence
Run `pytest --runxfail` in this folder. Issues 1 and 2 reproduce as `test_ai_version[none_inside_list]` and `test_ai_version[number_inside_list]`. By default these are marked `xfail(strict=True)` so the suite stays green.

## Suggested Improvement
Skip `None` values and non-strings inside the loop, as in `correct_fix.py`. The requirement does not say what to do with non-strings (skip, convert, or raise). I chose to skip, which silently drops data such as `123`. If dropped data matters to callers, raising `TypeError` or converting with `str()` would be the alternatives.

## Verdict: Partially Correct
The requirement lists four inputs it must handle. The code handles two (`None`, empty list) and crashes on the other two (None inside list, non-string inside list), so it does not fully meet the requirement. It is Partially Correct rather than Incorrect because the reported crash is fixed, the main use case (clean input) works, and both failures are crashes on dirty input rather than wrong results on normal input. If the rubric were applied strictly to "must handle" items, a reviewer could reasonably argue Incorrect.

## Other observations (not scored, outside the stated requirement)
- A plain string like `"abc"` is iterated character by character, giving `['a', 'b', 'c']` in both versions. Neither checks that the input is a list.
- `lower()` is not the strictest case-insensitive comparison; `casefold()` also treats `"ß"` and `"SS"` as equal. This goes beyond the stated requirement.

## Agent Failure Pattern
The model fixes the obvious top-level bug (None input) but does not check the values inside the list, and does not write edge-case tests.
