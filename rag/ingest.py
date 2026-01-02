print("INGESTION STARTED")

import os, json, pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from vectorstore import VectorStore

DATA_DIRS = ["data/raw", "data/processed"]

documents = []
metadata = []

for folder in DATA_DIRS:
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if file.endswith(".txt"):
            text = open(path, encoding="utf-8").read()
        elif file.endswith(".csv"):
            text = pd.read_csv(path).to_string()
        elif file.endswith(".json"):
            text = json.dumps(json.load(open(path)))
        else:
            continue

        documents.append(text)
        metadata.append({
            "source": file,
            "text": text[:500]
        })

vectorizer = TfidfVectorizer(stop_words="english")
vectors = vectorizer.fit_transform(documents).toarray()

store = VectorStore()
store.add(vectors, metadata)
store.save()

with open("tfidf.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("INGESTION COMPLETE")
