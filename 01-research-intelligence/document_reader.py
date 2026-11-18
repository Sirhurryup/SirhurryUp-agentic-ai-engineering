
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
    result = read_document("sample_documents/student_outcomes.txt")
    chunks = chunk_document(result)
    print(f"Total chunks: {len(chunks)}")
    
    matches = search_chunks(chunks, "completion", "student_outcomes.txt")
    print(f"Matching chunks: {len(matches)}")

    if not matches:
        print("No matching research passages found.")

    for match in matches:
        print("MATCH FOUND:")
        print("Source:", match["source"])
        print("Text:", match["text"])
        print("---")
except FileNotFoundError:
    print("ERROR: Research document not found.")

# DRY: Don't Repeat Yourself
