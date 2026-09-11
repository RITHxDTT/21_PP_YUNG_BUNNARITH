"""
Stage 5: Given a user question, retrieve the most relevant chunks
from ChromaDB.
"""

from typing import List, TypedDict

from config import TOP_K
from embeddings import embed_query
from vector_store import get_collection


class RetrievedChunk(TypedDict):
    content: str
    source: str
    chunk_index: int
    distance: float


def retrieve(
    query: str,
    top_k: int = TOP_K
) -> List[RetrievedChunk]:
    """
    Embed the user question and return the top matching chunks.
    """

    collection = get_collection()

    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        include=[
            "documents",
            "metadatas",
            "distances"
        ]
    )

    retrieved_chunks: List[RetrievedChunk] = []

    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]

    for content, metadata, distance in zip(
        documents,
        metadatas,
        distances
    ):
        retrieved_chunks.append({
            "content": content,
            "source": metadata.get("source", "unknown"),
            "chunk_index": metadata.get("chunk_index", -1),
            "distance": distance
        })

    return retrieved_chunks