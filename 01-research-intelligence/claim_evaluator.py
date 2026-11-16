def evaluate_claim(claim):
    if claim["source"] is None:
        return "NEEDS REVIEW"
    else:
        return "NEEDS VERIFICATION"
