def search_chunks(chunks, keyword, source):
    matches = []

    for chunk_id, chunk in enumerate(chunks, start=1):
        if keyword.lower() in chunk.lower():
            matches.append({
                "source": source,
                "chunk_id": chunk_id,
                "text": chunk
            })

    return matches