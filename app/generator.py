import json
import requests

from config import (
    OLLAMA_BASE_URL,
    GENERATION_MODEL,
    SYSTEM_PROMPT, TEMPERATURE
)

from retriever import RetrievedChunk


def build_prompt(
    query: str,
    chunks: list[RetrievedChunk]
) -> str:

    if not chunks:
        context_block = "(no relevant context was found)"
    else:
        context_block = "\n\n".join(
            f"[{i + 1}] Source: {chunk['source']}\n"
            f"{chunk['content']}"
            for i, chunk in enumerate(chunks)
        )

    return (
        f"Context:\n{context_block}\n\n"
        f"Question: {query}\n\n"
        "Answer using only the context above."
    )


def generate_answer(
    query: str,
    chunks: list[RetrievedChunk]
) -> str:

    prompt = build_prompt(query, chunks)

    response = requests.post(
        f"{OLLAMA_BASE_URL}/api/chat",
        json={
            "model": GENERATION_MODEL,
            "messages": [
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "stream": True,
            "options": {
                "temperature": TEMPERATURE
            }
        },
        stream=True,
        timeout=120
    )

    response.raise_for_status()

    full_answer = ""

    for line in response.iter_lines():
        if not line:
            continue

        data = json.loads(line.decode("utf-8"))

        token = data.get("message", {}).get("content", "")

        if token:
            print(token, end="", flush=True)
            full_answer += token

    print()

    return full_answer