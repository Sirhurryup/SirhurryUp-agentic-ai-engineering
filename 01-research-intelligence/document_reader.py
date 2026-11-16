
from document_loader import read_document

def read_document(file_path):
    with(open(file_path, "r", encoding="utf-8")) as file: 
        content = file.read()
        return content

try:
    result = read_document("sample_documents/student_outcomes.txt")
    print(result)
except FileNotFoundError:
    print("ERROR: Research document not found.")

# DRY: Don't Repeat Yourself
