import pickle
from sklearn.metrics.pairwise import cosine_similarity

class VectorStore:
    def __init__(self):
        self.vectors = []
        self.metadata = []

    def add(self, vectors, metas):
        self.vectors.extend(vectors)
        self.metadata.extend(metas)

    def save(self):
        with open("vectorstore.pkl", "wb") as f:
            pickle.dump((self.vectors, self.metadata), f)

    def load(self):
        with open("vectorstore.pkl", "rb") as f:
            self.vectors, self.metadata = pickle.load(f)

    def search(self, query_vector, top_k=5):
        scores = cosine_similarity([query_vector], self.vectors)[0]
        top_indices = scores.argsort()[-top_k:][::-1]
        return [self.metadata[i] for i in top_indices]
