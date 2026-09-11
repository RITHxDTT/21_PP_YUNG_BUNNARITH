
import chromadb


from config import CHROMA_PATH, COLLECTION_NAME
from embeddings import embed_texts


def get_collection():
    """
    Get or create the persistent ChromaDB collection.
    """

    client = chromadb.PersistentClient(
        path=str(CHROMA_PATH)
    )

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def build_index(chunks) -> int:
    """
    Embed all chunks and store them in ChromaDB.

    Returns:
        Number of chunks stored.
    """

    if not chunks:
        return 0

    collection = get_collection()

    texts = [
        chunk["content"]
        for chunk in chunks
    ]

    embeddings = embed_texts(texts)

    ids = []
    metadatas = []

    for index, chunk in enumerate(chunks):

        source = chunk["metadata"]["source"]
        chunk_index = chunk["metadata"]["chunk_index"]

        ids.append(
            f"{source}::{chunk_index}"
        )

        metadatas.append(
            chunk["metadata"]
        )

    collection.upsert(
        ids=ids,
        documents=texts,
        embeddings=embeddings,
        metadatas=metadatas
    )

    return len(texts)