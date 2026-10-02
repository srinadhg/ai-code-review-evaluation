# Requirement

Write function `get_unique_tags(tags)`:

- Input: list of tag names, or None
- Output: list of unique tag names, case-insensitive, preserving the order of first occurrence
- Must handle: None input, empty list, None values inside the list, non-string values inside the list

Example:
Input: ["TagA", "taga", "TagB", None, "tagb"]
Output: ["TagA", "TagB"]

Note: the requirement does not say what to do with non-string values (skip, convert, or raise). The fix in this repo skips them; see `review.md`.
