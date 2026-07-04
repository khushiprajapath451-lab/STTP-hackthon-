import chromadb
from chromadb.config import Settings

# Persistent DB
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="resumes"
)


def add_to_db(doc_id, embedding, metadata):
    collection.add(
        ids=[doc_id],
        embeddings=[embedding],
        metadatas=[metadata]
    )


def query_db(query_embedding, top_k=5):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    return results