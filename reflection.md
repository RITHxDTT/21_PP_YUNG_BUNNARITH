# Reflection

In this homework, I built a simple Naive RAG application. Overall, I think the application works well when I ask the question that have information inside my documents. The system can load my text files, split the text into chunks, create embedding vectors with `nomic-embed-text`, and store them inside ChromaDB. When I ask a question, the system can search the related chunks and send the context to `llama3.2:3b` for generating the final answer.

One thing that was harder than I expected is the retrieval part. Sometimes the system retrieves a chunk that is not really related to my question because ChromaDB will still find the closest vectors. I also had some problems with Python environment and dependencies, especially when setting up ChromaDB. I needed to test each part step by step to understand where the problem came from.

For future improvement, I want to try **Re-ranking** from Advanced RAG. After ChromaDB retrieves the Top-K chunks, the reranker can check those chunks again and put the most relevant one first. I think this can reduce unrelated context and help the LLM generate a better and more accurate answer.