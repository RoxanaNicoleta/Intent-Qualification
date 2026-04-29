import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def score(query, parsed, company):
    text = " ".join([
        company.get("description", ""),
        str(company.get("core_offerings", "")),
        company.get("primary_naics", {}).get("label", "")
    ])

    q_emb = model.encode(query, normalize_embeddings=True)
    c_emb = model.encode(text, normalize_embeddings=True)

    sim = float(np.dot(q_emb, c_emb))

    s = 0.4 * sim

    if parsed.get("min_employees"):
        if company.get("employee_count", 0) >= parsed["min_employees"]:
            s += 0.2

    if parsed.get("is_public") is True and company.get("is_public"):
        s += 0.2

    if parsed.get("industry"):
        desc = text.lower()
        if any(i in desc for i in parsed["industry"]):
            s += 0.2

    return s


def rank(query, parsed, companies):
    scored = [(score(query, parsed, c), c) for c in companies]
    scored.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scored]