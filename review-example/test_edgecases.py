"""
Edge-case tests run against both versions.

- `correct_fix.py` must pass every case.
- `ai_generated_code.py` is expected to fail two cases. Those are marked
  xfail(strict=True) so the suite stays green and documents the bugs. If the AI
  version ever starts passing them, strict mode turns that into a failure.

To see the raw failures, run:  pytest --runxfail
"""
import pytest

from ai_generated_code import get_unique_tags as ai_version
from correct_fix import get_unique_tags as fixed_version

CASES = [
    ("none_input", None, []),
    ("empty_list", [], []),
    ("unique_case_insensitive", ["TagA", "taga", "TagB"], ["TagA", "TagB"]),
    ("none_inside_list", ["TagA", None, "taga"], ["TagA"]),
    ("number_inside_list", ["TagA", 123, "TagB"], ["TagA", "TagB"]),
    ("preserve_order", ["b", "A", "a", "B"], ["b", "A"]),
]

AI_KNOWN_FAILURES = {"none_inside_list", "number_inside_list"}


@pytest.mark.parametrize("case_id, data, expected", CASES, ids=[c[0] for c in CASES])
def test_fixed_version(case_id, data, expected):
    assert fixed_version(data) == expected


def _ai_params():
    params = []
    for case_id, data, expected in CASES:
        marks = []
        if case_id in AI_KNOWN_FAILURES:
            marks.append(pytest.mark.xfail(strict=True, raises=AttributeError))
        params.append(pytest.param(case_id, data, expected, id=case_id, marks=marks))
    return params


@pytest.mark.parametrize("case_id, data, expected", _ai_params())
def test_ai_version(case_id, data, expected):
    assert ai_version(data) == expected
