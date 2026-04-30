from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")


def safe(x):
    return "" if x is None else str(x)


def safe_naics(c):
    naics = c.get("primary_naics", "")
    if isinstance(naics, dict):
        return naics.get("label", "") or ""
    return naics or ""


def build_bm25(companies):
    corpus = []
    tokenized = []

    for c in companies:
        text = " ".join([
            safe(c.get("operational_name")),
            safe(c.get("description")),
            safe(c.get("country")),
            safe(c.get("industry")),
            safe(c.get("employee_count")),
            safe(c.get("is_public")),
            safe_naics(c),
        ])

        corpus.append(text)
        tokenized.append(text.lower().split())

    bm25 = BM25Okapi(tokenized)
    return bm25, corpus


def bm25_search(bm25, companies, query, k=10):
    tokens = query.lower().split()
    scores = bm25.get_scores(tokens)

    ranked = sorted(
        zip(companies, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [c for c, _ in ranked[:k]]


def embed_search(companies, query, k=10):
    query_emb = model.encode(query)

    texts = [
        " ".join([
            safe(c.get("operational_name")),
            safe(c.get("description")),
            safe(c.get("country")),
        ])
        for c in companies
    ]

    doc_embs = model.encode(texts)

    scores = (doc_embs @ query_emb)

    ranked = sorted(
        zip(companies, scores),
        key=lambda x: x[1],
        reverse=True
    )

    return [c for c, _ in ranked[:k]]
