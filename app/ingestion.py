

from pathlib import Path
from typing import List, Tuple

from config import DATA_DIR


def _read_txt(path: Path) -> str:
    """
    Read one .txt file and return its full text.
    """
    return path.read_text(
        encoding="utf-8",
        errors="ignore"
    )


def load_documents(
    data_dir: Path = DATA_DIR
) -> List[Tuple[str, str]]:
    """
    Return a list of (filename, full_text)
    for every .txt file in the data directory.
    """

    documents: List[Tuple[str, str]] = []

    for file_path in sorted(data_dir.glob("*.txt")):

        if not file_path.is_file():
            continue

        text = _read_txt(file_path)

        if not text.strip():
            continue

        documents.append(
            (
                file_path.name,
                text.strip()
            )
        )

    return documents