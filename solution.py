import json
from retrieval import build_bm25, bm25_search, embed_search


def load_data(path):
    data = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data


def run(query, companies, bm25):
    print(f"\nQUERY: {query}")

    bm25_results = bm25_search(bm25, companies, query, k=5)
    embed_results = embed_search(companies, query, k=5)

    seen = set()
    results = []

    for r in bm25_results + embed_results:
        name = r.get("operational_name")
        if name and name not in seen:
            seen.add(name)
            results.append(r)

    return results[:10]


if __name__ == "__main__":
    companies = load_data("data/companies.jsonl")

    bm25, _ = build_bm25(companies)

    while True:
        q = input("\nEnter query (or 'exit'): ")
        if q == "exit":
            break

        res = run(q, companies, bm25)

        print("\nRESULTS:")
        for r in res:
            print("-", r.get("operational_name"))
