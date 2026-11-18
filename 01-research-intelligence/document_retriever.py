def search_chunks(chunks, keyword, source):
    matches = []

    for chunk in chunks:
        if keyword.lower() in chunk.lower():
            matches.append({
                "source": source,
                "text": chunk
            })

    return matches