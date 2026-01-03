import os
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from rag.vectorstore import VectorStore

DATA_DIR = "data/raw"

texts = []
metadata = []

for filename in os.listdir(DATA_DIR):
    if not filename.endswith(".txt"):
        continue

    path = os.path.join(DATA_DIR, filename)

    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

        # split by paragraphs
        paragraphs = [p.strip() for p in content.split("\n\n") if len(p.strip()) > 50]

        for para in paragraphs:
            texts.append(para)
            metadata.append({
                "source": filename,
                "text": para
            })

vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

vectors = vectorizer.fit_transform(texts).toarray()

store = VectorStore()
store.add(vectors, metadata)
store.save()

pickle.dump(vectorizer, open("tfidf.pkl", "wb"))

print("INGESTION COMPLETE — paragraph-level indexing")
