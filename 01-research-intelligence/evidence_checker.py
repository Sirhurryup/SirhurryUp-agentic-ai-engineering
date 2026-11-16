def check_evidence(evidence):
    for item in evidence: 
        if not isinstance(item, str):
            raise TypeError("Evidence must contain strings")
    return any(item.strip() for item in evidence)



