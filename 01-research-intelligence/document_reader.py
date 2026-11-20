
from document_loader import read_document
from document_chunker import chunk_document
from document_retriever import search_chunks 

def chunk_document(content):
    chunks = content.split("\n\n")
    cleaned_chunks = []

    for chunk in chunks:
        chunk = chunk.strip()

        if chunk:
            cleaned_chunks.append(chunk)

    return cleaned_chunks

try:
    documents = [
        "sample_documents/student_outcomes.txt",
        "sample_documents/attendance_summary.txt"
    ]

    all_matches = []

    for document in documents:
        result = read_document(document)
        print(f"Loaded: {document}")

        chunks = chunk_document(result)
        print(f"Total chunks: {len(chunks)}")
    
        matches = search_chunks(chunks, "completion", document)
        all_matches.extend(matches)

    print(f"Total matching chunks: {len(all_matches)}")

    if not all_matches:
        print("No matching research passages found.")

    for match in all_matches:
        print("MATCH FOUND:")
        print("Source:", match["source"])
        print("Chunk ID:", match["chunk_id"])
        print("Text:", match["text"])
        print("---")
except FileNotFoundError:
    print("ERROR: Research document not found.")

# DRY: Don't Repeat Yourself
