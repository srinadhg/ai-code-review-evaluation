# Hand-written to reproduce a common AI failure pattern: the top-level None
# crash is fixed, but values inside the list are never checked.
# Simulated task prompt: "Fix the function to handle None and return unique tags, case-insensitive"
# This is NOT real model output.

def get_unique_tags(tags):
    if not tags:
        return []
    seen = set()
    result = []
    for t in tags:
        if t.lower() not in seen:
            seen.add(t.lower())
            result.append(t)
    return result
