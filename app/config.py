from pathlib import Path



# Project paths

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

# =========================================================
# Chunking configuration
# ===========================================================

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100


# ============================================================
# Retrieval configuration
# ===========================================================

TOP_K = 3

# Generation
TEMPERATURE = 0.2

# ============================================================
# Ollama configuration
# ============================================================

OLLAMA_BASE_URL = "http://localhost:11434"

EMBEDDING_MODEL = "nomic-embed-text"
GENERATION_MODEL = "llama3.2:3b"


# ============================================================
# ChromaDB configuration
# ============================================================

CHROMA_PATH = BASE_DIR / "chroma_db"
COLLECTION_NAME = "YungBunnarith_Navie_RAG"



# ============================================================
# RAG System Prompt
# ============================================================

SYSTEM_PROMPT = """
You are a helpful assistant that answers questions using ONLY the
context provided below.

Rules:
1. Answer factual questions using only information found in the provided context.
2. Do not use outside knowledge.
3. If the user asks what you can help with, what information you have,
   or what topics are available, summarize the topics represented in the
   provided context and explain what kinds of questions you can answer.
4. If the answer to a factual question is not contained in the context, say:
   "I don't have enough information in the documents to answer that."
5. Cite the source file name used to answer factual questions.
6. Do not make up information.
""".strip()