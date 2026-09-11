# Naive RAG Chat Application

This project is a simple Naive RAG application that answers questions based on the documents inside the `data/` folder.

## 1. Setup Steps

### Clone the Project

```bash
git clone 
cd Build_Baseline_RAG
```

### Create Virtual Environment

The `.venv` folder is not included in Git, so create a new virtual environment after cloning the project.

```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start Ollama

Make sure Ollama is installed and running.

```bash
ollama serve
```

### Pull the Embedding Model

```bash
ollama pull nomic-embed-text
```

### Pull the Generation Model

```bash
ollama pull llama3.2:3b
```

### Build the Vector Index

The `chroma_db` folder is not stored in Git because it can be generated again from the documents.

Run:

```bash
python app/index.py
```

This will:

1. Load documents from `data/`
2. Split the documents into chunks
3. Create embeddings
4. Store the vectors in ChromaDB

### Run the Application

```bash
python app/main.py
```

Type your question in the terminal.

To stop the application:

```text
exit
```

## 2. Model Choices

### Embedding Model

 using `nomic-embed-text` for creating embeddings.

### Generation Model

 `llama3.2:3b` for generating the final answer.

chosing this model because it can run locally on my machine and it is enough for this simple Naive RAG application.

## 3. Chunking Rationale

I use **Recursive Character Text Splitting**.

My configuration:

- Chunk Size: 500
- Chunk Overlap: 100

I chose this strategy because my documents contain paragraphs, sentences, steps, and lists. Recursive chunking helps split the text into smaller parts while trying to keep related text together.

I use an overlap of 100 because some important information may be located between two chunks. The overlap keeps some context from the previous chunk and can help retrieval find better information.