# Naive RAG Chat Application

This project is a simple Naive RAG application that answers questions based on documents stored in the `data/` folder.

## 1. Setup Steps

### Create virtual environment

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```
pip install chromadb requests langchain-text-splitters
```
Start Ollama
ollama serve
Pull embedding model
ollama pull nomic-embed-text
Pull generation model
ollama pull llama3.2:3b
Build the vector index
python app/index.py
Run the chat application
python app/main.py

Type exit to stop the program.

## 2. Model Choices
```
Embedding Model

using  nomic embed-text as the embedding model.

and  chose this model because it is made for text embeddings and it can run locally with Ollama. I use the same embedding model for document chunks and user questions.

Generation Model

I use llama3.2:3b as the generation model.

I chose this model because it is lightweight enough to run locally and it works well for a simple RAG homework project.

3. Chunking Rationale

I use Recursive Character Text Splitting.

Configuration:

Chunk size: 500
Chunk overlap: 100
```