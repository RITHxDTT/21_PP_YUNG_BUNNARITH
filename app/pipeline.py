from retriever import retrieve
from generator import generate_answer
from ingestion import load_documents


def is_capability_question(query: str) -> bool:
    query = query.lower()

    keywords = [
        "help",
        "assist",
        "information",
        "topics",
        "documents",
        "know",
        "available"
    ]

    intent_words = [
        "what",
        "which",
        "can",
        "do you"
    ]

    has_keyword = any(word in query for word in keywords)
    has_intent = any(word in query for word in intent_words)

    return has_keyword and has_intent


def get_available_topics() -> str:
    documents = load_documents()

    topics = []

    for filename, _ in documents:
        topic = filename.replace("_", " ")
        topic = topic.replace(".txt", "")

        # Remove numeric prefix like 001
        topic = topic.split(" ", 1)[-1]

        topics.append(topic)

    return (
        "I can assist you with information about:\n- "
        + "\n- ".join(topics)
    )


def print_retrieved_chunks(chunks):
    """
    Print retrieved chunks for testing/debugging.
    """

    print("\n--- Retrieved Chunks ---")

    if not chunks:
        print("No relevant chunks found.")
        return

    for i, chunk in enumerate(chunks, start=1):
        print(f"\nChunk {i}")
        print(f"Source: {chunk['source']}")
        print(f"Chunk Index: {chunk['chunk_index']}")
        print(f"Distance: {chunk['distance']:.4f}")
        print("Content:")
        print(chunk["content"])
        print("-" * 60)


def run_pipeline(query: str):

    # Special question asking what information is available
    if is_capability_question(query):
        return get_available_topics()

    # Retrieve relevant chunks
    chunks = retrieve(query)

    # Show retrieved chunks for homework testing
    print_retrieved_chunks(chunks)

    print("\n--- Final Answer ---")

    # Generate streamed answer
    generate_answer(
        query=query,
        chunks=chunks
    )

    return None