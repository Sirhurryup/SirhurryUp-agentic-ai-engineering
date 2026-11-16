import unittest
from document_loader import read_document

class TestDocumentLoader(unittest.TestCase):
    def test_read_existing_document(self):
        file_path = "sample_documents/student_outcomes.txt"
        result = read_document(file_path)
        self.assertIn("120 students", result)

    def test_missing_document(self):
        with self.assertRaises(FileNotFoundError):
            read_document("sample_documents/missing_report.txt")