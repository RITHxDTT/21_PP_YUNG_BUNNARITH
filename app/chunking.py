

from typing import List, Tuple

from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import CHUNK_SIZE, CHUNK_OVERLAP


def chunk_documents(
    documents: List[Tuple[str, str]]
) -> List[dict]:
    """
    Split documents using Recursive Character Chunking.

    Input:
        [
            ("file1.txt", "full text..."),
            ("file2.txt", "full text...")
        ]

    Output:
        [
            {
                "content": "...",
                "metadata": {
                    "source": "file1.txt",
                    "chunk_index": 0
                }
            }
        ]
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""]
    )

    chunks = []

    for filename, full_text in documents:

        split_texts = splitter.split_text(full_text)

        for index, text in enumerate(split_texts):
            chunks.append({
                "content": text,
                "metadata": {
                    "source": filename,
                    "chunk_index": index
                }
            })

    return chunks