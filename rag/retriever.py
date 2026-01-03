import pickle
from rag.vectorstore import VectorStore
import numpy as np

 # Load vectorizer
with open("tfidf.pkl", "rb") as f:
    vectorizer = pickle.load(f)

store = VectorStore()
store.load()

def retrieve_answer(query: str):
    q = query.lower()
    query_vec = vectorizer.transform([query]).toarray()[0]

    # 🔹 Decide intent
    if any(k in q for k in ["rule", "dgca", "regulation", "compliance"]):
        top_k = 5
        allowed_sources = [
            "dgca_rules.txt",
            "Airspace_zones.txt",
            "drone_registration.txt",
            "pilot_licensing.txt",
            "penalties_compliance.txt"
        ]

    elif any(k in q for k in ["price", "cost", "range"]):
        top_k = 2
        allowed_sources = ["agriculture_drone_market_2025.txt"]

    elif "airspace" in q or "zone" in q:
        top_k = 2
        allowed_sources = ["Airspace_zones.txt"]

    else:
        top_k = 3
        allowed_sources = None  # fallback

    results = store.search(query_vec, top_k=top_k)

    # 🔹 Filter by source if needed
    if allowed_sources:
        results = [r for r in results if r["source"] in allowed_sources]

    if not results:
        return {
            "answer": "No relevant information found.",
            "source": None
        }

    # 🔹 Combine results
    answer = "\n\n".join(r["text"] for r in results)
    sources = ", ".join(sorted(set(r["source"] for r in results)))

    return {
        "answer": answer.strip(),
        "source": sources
    }


# ---------------- CLI MODE (OPTIONAL TESTING) ----------------

if __name__ == "__main__":
    while True:
        query = input("\nAsk a question (or type 'exit'): ")
        if query.lower() == "exit":
            break

        result = retrieve_answer(query)
        print("\nSource:", result["source"])
        print(result["answer"])
