def get_unique_tags(tags):
    if tags is None:
        return []
    seen = set()
    result = []
    for t in tags:
        if t is None:
            continue
        if not isinstance(t, str):
            continue  # design choice: skip non-strings (the requirement doesn't specify)
        lower = t.lower()
        if lower not in seen:
            seen.add(lower)
            result.append(t)
    return result
