import unittest
from evidence_checker import check_evidence

class TestEvidenceChecker(unittest.TestCase):

    def test_empty_evidence(self):
        result = check_evidence([])
        self.assertFalse(result)

    def test_valid_evidence(self):
        result = check_evidence(["Study completed"])
        self.assertTrue(result)

    def test_whitespace(self):
        result = check_evidence(" ")
        self.assertFalse(result)

    def test_invalid_evidence_type(self):
        with self.assertRaises(TypeError):
            check_evidence(["Study complete", 42])