def llm_score(query, company):
    """
    Placeholder pentru LLM real.
    În producție: OpenAI / vLLM / etc.
    """
    text = (
        company.get("description", "") + " " +
        " ".join(company.get("core_offerings", []))
    ).lower()

    q = query.lower().split()
    return sum(1 for w in q if w in text) / max(len(q), 1)


def rerank(query, companies, top_k=10):
    scored = []

    for c in companies:
        score = llm_score(query, c)
        scored.append((score, c))

    scored.sort(reverse=True, key=lambda x: x[0])
    return [c for _, c in scored[:top_k]]