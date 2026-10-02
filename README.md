# AI Code Review Evaluation

Exercises in reviewing AI-generated Python code: spotting weak fixes, missed edge cases, and shallow tests. Each review follows the [rubric](./rubrics/code-review-rubric.md).

> All examples are written from scratch or based on public open-source code. My professional work is in private repos.

## Review format

Requirement → Code → Issues found → Suggested fix → Edge-case tests → Verdict

## Contents

- [`rubrics/`](./rubrics/code-review-rubric.md): evaluation criteria and verdict definitions
- [`review-example/`](./review-example): a weak fix that handles top-level `None` but crashes on bad values inside the list

Each example states where the code came from. This one is hand-written to reproduce a common failure pattern, not real model output.

## Run the tests

```
pip install -r requirements.txt
cd review-example
pytest              # all pass; 2 known AI-version failures are marked xfail
pytest --runxfail   # shows the raw AI-version failures
```

## Stack

Python, pytest

Note: Created in October 2026 as a portfolio project to demonstrate an evaluation approach for AI coding-agent and AI evaluation roles.
