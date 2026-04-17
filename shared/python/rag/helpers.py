def chunk_text(text: str, chunk_size: int = 1000, overlap: int = 200) -> list[str]:
    # Placeholder for actual chunking logic
    chunks = []
    for i in range(0, len(text), chunk_size - overlap):
        chunks.append(text[i:i + chunk_size])
    return chunks
