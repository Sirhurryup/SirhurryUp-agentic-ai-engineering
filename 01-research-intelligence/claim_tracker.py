from claim_evaluator import evaluate_claim

claim = {
    "text": "Our research increased student participation.",
    "source": None,
    "status": "NEEDS REVIEW"
}

#claim["source"] = "Progress Report 2025"


def evaluate_claim(claim):
    if claim["source"] is None:
        return "NEEDS REVIEW"
    else:
        return "NEEDS VERIFICATION"
result = evaluate_claim(claim)
print(result)

claim["status"] = evaluate_claim(claim)
print(claim)

claim2 = {
    "text": "Our research improved graduation rates.",
    "source": "Graduation Outcomes Report 2025",
    "status": "NEEDS REVIEW"
}

claim2["status"] = evaluate_claim(claim2)
print(claim2)

claims = [claim, claim2]

for claim in claims: 
    claim["status"] = evaluate_claim(claim)
    print(claim["text"])
    print(claim["status"])