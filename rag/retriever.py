import pickle
from vectorstore import VectorStore

vectorizer = pickle.load(open("tfidf.pkl", "rb"))
store = VectorStore()
store.load()

query = input("Ask a question: ")
query_vec = vectorizer.transform([query]).toarray()[0]

results = store.search(query_vec, top_k=1)

for r in results:
    print("\nSource:", r["source"])

    text = r["text"]

    if "price" in query.lower():
        lines = [line for line in text.split(".") if "₹" in line or "lakh" in line.lower()]
        print(". ".join(lines[:3]))
    else:
        print(text)

