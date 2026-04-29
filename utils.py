import re

def normalize_text(t):
    return (t or "").lower().strip()


def extract_number(text):
    match = re.search(r"(\d[\d,]*)", text)
    if match:
        return int(match.group(1).replace(",", ""))
    return None


def safe_get(d, path, default=None):
    for p in path:
        if not isinstance(d, dict):
            return default
        d = d.get(p)
    return d