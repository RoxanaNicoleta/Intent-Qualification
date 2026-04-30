
1. What I built in this project  
In this project, I built a system that takes  a natural language query (for example: “logistics companies in Germany”) and returns the most relevant companies from a dataset. My goal was to build a system that understands both: exact words in the query and the meaning behind the query.  
  
4. My approach    
I used two different methods and combined them:  
  -> 2.1 BM25 (keyword-based search)  
I used BM25 to find companies based on exact keyword matches.  
In simple terms:  
  -> if the query contains “Germany”, it looks for companies related to Germany  
  -> if the query contains “logistics”, it looks for logistics-related companies   
This method is very good for precise keyword matching.  
  -> 2.2 Semantic search (embeddings)  
I used a SentenceTransformer model to understand the meaning of the text.It converts text into vectors and compares meaning instead of exact words.  
For example: “logistics companies”, “supply chain providers”  are considered similar, even if they don’t share the same words.  
  
3. How I combined both methods   
I used both approaches in parallel:  
  -BM25 for keyword relevance  
  -embeddings for semantic similarity  
Then I:  
  -merged the results  
  -removed duplicates  
  -returned the top ranked companies  
  
4. Challenges I faced   
-> Inconsistent data  
  The dataset contained:  
    -None values   
    -strings  
    -sometimes dictionaries  
  Because of this, I had to convert everything safely into strings and to add checks before accessing fields.   
  -> Type errors  
  I encountered errors such as:  
    -NoneType errors  
    -tuple vs object mismatches  
    -dictionary vs string inconsistencies  
I fixed them by making the code more defensive and robust.  
  
6. Design decisions   
Why BM25?  
  Because it is fast and works very well for keyword-based search.  
Why embeddings?  
  Because they allow the system to understand meaning, not just exact words.  
Why combine both?  
Because:  
  -BM25 improves precision  
  -embeddings improve semantic understanding  
Together, they give better overall results.  

7. Limitations  
My system has a few limitations:  
  -no advanced reranking model  
  -simple tokenization (basic split)  
  -embeddings are not indexed with FAISS for maximum performance  

8. Future improvements  
If I continue this project, I would add:  
  -a reranking model (cross-encoder)  
  -FAISS for faster vector search  
  -better preprocessing (lemmatization, stopword removal)  
  -an API layer (FastAPI) for deployment  

9. Conclusion  
I built a hybrid retrieval system that combines: keyword-based search (BM25) and semantic search (embeddings).  
The goal was to improve search quality by understanding both exact terms and meaning, so the system can return relevant results even when queries are not identical to the dataset wording.  


EXAMPLE:  

QUERY: Companies supplying packaging for cosmetics brands RESULTS:  
  -Shanghai Bochen Cosmetic Packaging  
  -Shenzhen Itop Cosmetic Packaging  
  -Standard Mold  
  -BAOLILONG GLASS PACKAGING  
  -Lesopack Cos Packaging  
  -Sunshine Packaging  
  -SZ SJ Packaging  
  
QUERY: Fast-growing fintech companies competing with traditional banks in Europe. RESULTS:  
  -European Pay  
  -L'Essinganaise  
  -Produit en Bretagne  
  -Auvergnat Cola  
  -Tietoevry  
  -Euro-Rijn Financial Services  
  -New Payment Innovation  
  -Rantum Capital  
  -Ford Credit  
  
QUERY: Public software companies with more than 1,000 employees. RESULTS:  
  -Microtis  
  -BambooHR  
  -Jooma  
  -Sesame HR  
  -Factorial  
  -ASGN  
  -EPAM  
  -Ciphr  
  -Sun RH  
