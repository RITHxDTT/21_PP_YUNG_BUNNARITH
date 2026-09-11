from typing import List

import requests

from config import OLLAMA_BASE_URL, EMBEDDING_MODEL


def embed_texts(texts: List[str]) -> List[List[float]]:
    """
    One function, one job: turn texts into vectors using
    the local Ollama embedding model.

    Both document chunks and user questions use this function,
    so they always use the same embedding model.
    """

    if not texts:
        return []

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/embed",
        json={
            "model": EMBEDDING_MODEL,
            "input": texts
        },
        timeout=60
    )

    response.raise_for_status()

    data = response.json()

    return data["embeddings"]


def embed_query(text: str) -> List[float]:
    """
    Embed one user question into a vector.
    """

    return embed_texts([text])[0]


def embed_chunks(chunks):
    """
    Embed all document chunks.
    """

    if not chunks:
        return []

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = embed_texts(texts)

    embedded_chunks = []

    for chunk, embedding in zip(chunks, embeddings):
        embedded_chunks.append({
            "content": chunk["content"],
            "embedding": embedding,
            "metadata": chunk["metadata"]
        })

    return embedded_chunks