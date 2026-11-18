import unittest
from document_retriever import search_chunks


class TestDocumentRetriever(unittest.TestCase):

    def test_matching_keyword(self):
        chunks = [
            "The program enrolled 120 students.",
            "The completion rate was 80 percent."
        ]

    def test_missing_keyword(self):
        chunks = [
            "The program enrolled 120 students."
            "The complettion rate was 80 percent."
        ]

    def test_source_attribution(self):
        chunks = [
            "The completion rate was 80 percent."
        ]

        matches = search_chunks(chunks, "completion", "student_outcomes.txt")

        self.assertEqual(matches[0]["source"], "student_outcomes.txt")