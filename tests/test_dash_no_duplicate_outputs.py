import re
from pathlib import Path


def test_no_duplicate_outputs():
    text = Path("frontend_dash/app.py").read_text(encoding="utf-8")
    outputs = re.findall(
        r"Output\(\s*['\"]([^'\"]+)['\"]\s*,\s*['\"]([^'\"]+)['\"]", text
    )
    seen = set()
    duplicates = []
    for component_id, prop in outputs:
        key = (component_id, prop)
        if key in seen:
            duplicates.append(key)
        else:
            seen.add(key)
    assert not duplicates, f"Duplicate Outputs found: {duplicates}"
