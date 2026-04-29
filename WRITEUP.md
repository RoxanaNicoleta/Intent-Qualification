1. Problem Overview

This project implements a hybrid information retrieval system for matching user queries to companies from a structured dataset.
The goal is to return the most relevant companies given a natural language query (e.g. “logistics companies in Germany”).

The system combines lexical retrieval (BM25) with semantic retrieval (Sentence Transformers embeddings).

2. Approach

We implemented a hybrid retrieval pipeline consisting of:

2.1 BM25 (Lexical Search)

BM25 is used to capture keyword-based relevance between query and company descriptions.

Tokenization: simple whitespace split
Scoring: rank_bm25.BM25Okapi
Strength: precise keyword matching (e.g. country, industry terms)
2.2 Semantic Search (Embeddings)

We used sentence-transformers/all-MiniLM-L6-v2 to encode:

company operational name
description
country
industry metadata

Cosine similarity is used to measure semantic closeness between query and documents.

Strength: handles synonyms and semantic similarity
Example: “logistics companies” matches “supply chain providers”
2.3 Hybrid Strategy

Final ranking combines:

BM25 results
embedding-based results

Duplicates are removed while preserving ranking priority.

3. Data Preprocessing

The dataset contained inconsistent schemas:

Some fields were None
Some fields were strings or dicts (e.g. primary_naics)
Missing values were frequent

To handle this:

All fields are normalized to strings
Missing values are replaced with empty strings
Nested dict fields are safely extracted
4. Challenges
4.1 Inconsistent Data Schema

The main issue was heterogeneous data types across records, requiring defensive programming.

4.2 Library Dependencies

The system depends on:

rank-bm25
sentence-transformers
torch (indirect dependency)

These require proper environment setup.

4.3 Performance Considerations
BM25 is fast and computed once per query set
Embeddings are computed once per run (not per query in optimized version)
5. Design Decisions
Why BM25 + Embeddings?
BM25 ensures strong keyword matching
Embeddings ensure semantic understanding
Hybrid approach improves recall and precision
Why not FAISS?

FAISS was initially considered, but for simplicity and stability the current implementation uses direct cosine similarity.

6. Limitations
No trained reranker model (e.g. cross-encoder not used)
Simple tokenization (no lemmatization or NLP preprocessing)
No persistent vector index (embeddings recomputed at runtime)
7. Possible Improvements
Add cross-encoder reranking for higher precision
Add FAISS index for faster vector search
Improve preprocessing (lemmatization, stopwords removal)
Add evaluation metrics (Precision@K, Recall@K)
Deploy as FastAPI service
8. Conclusion

The system successfully combines lexical and semantic retrieval to improve matching quality for natural language queries over structured company data. The hybrid approach provides a balance between precision (BM25) and semantic generalization (embeddings).


EXAMPLE:


QUERY: Companies supplying packaging for cosmetics brands
RESULTS:
- Shanghai Bochen Cosmetic Packaging
- Shenzhen Itop Cosmetic Packaging
- Standard Mold
- BAOLILONG GLASS PACKAGING
- Lesopack Cos Packaging
- Sunshine Packaging
- SZ SJ Packaging


QUERY: Fast-growing fintech companies competing with traditional banks in Europe.
RESULTS:
- European Pay
- L'Essinganaise
- Produit en Bretagne
- Auvergnat Cola
- Tietoevry
- Euro-Rijn Financial Services
- New Payment Innovation
- Rantum Capital
- Ford Credit


QUERY: Public software companies with more than 1,000 employees.
RESULTS:
- Microtis
- BambooHR
- Jooma
- Sesame HR
- Factorial
- ASGN
- EPAM
- Ciphr
- Sun RH

