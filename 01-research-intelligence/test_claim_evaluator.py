import unittest
from claim_evaluator import evaluate_claim

class TestClaimEvaluator(unittest.TestCase):
    def test_missing_source(self):
       claim = {
           "text": "Our resarch increased student participation.",
           "source": None,
           "status": "NEEDS REVIEW"
       }
       result = evaluate_claim(claim)
       self.assertEqual(result, "NEEDS REVIEW")


    def test_source_assigned(self):
       claim = {
          "text": "Our researc improved graduation rates.",
          "source": "Graduation Outcomes Report 2025",
          "status": "NEEDS REVIEW"
       }
       result = evaluate_claim(claim)
       self.assertEqual(result, "NEEDS VERIFICATION")

    
