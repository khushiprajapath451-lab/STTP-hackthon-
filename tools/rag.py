from tools.embeddings import get_embedding
from tools.vectordb import query_db


def retrieve_resumes(query_text):
    """
    RAG retrieval pipeline

    Input:
        JD or query text

    Output:
        Top matching resumes
    """

    query_embedding = get_embedding(query_text)

    results = query_db(query_embedding)

    resumes = []

    for i in range(len(results["ids"][0])):

        resumes.append({
            "id": results["ids"][0][i],
            "text": results["metadatas"][0][i]["text"],
            "score": results["distances"][0][i]
        })

    return resumes