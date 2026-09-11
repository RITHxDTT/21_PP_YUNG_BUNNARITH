from ingestion import load_documents
from chunking import chunk_documents
from vector_store import build_index


def main():
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")

    chunks = chunk_documents(documents)
    print(f"Created {len(chunks)} chunks")

    count = build_index(chunks)
    print(f"Indexed {count} chunks into ChromaDB")


if __name__ == "__main__":
    main()