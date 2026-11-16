# Research Intelligence — Engineering Log

## Lab 01: Evidence Before Generation

### Business Problem
Research proposals must not rely on missing or invalid evidence.

### Architecture Decision 001
Validate evidence inputs before allowing downstream generation.

### Implementation
- Built `check_evidence()` in Python.
- Used `isinstance()` for type validation.
- Used `.strip()` and `any()` to reject empty evidence.
- Raised `TypeError` for invalid evidence types.

### Verification
Four automated tests passed using Python unittest:
1. Empty evidence rejected.
2. Nonempty evidence accepted.
3. Whitespace-only evidence rejected.
4. Invalid evidence type raises TypeError.

### Limitations
The checker validates the presence of text, not scientific accuracy, source authenticity, or relevance to a claim.

### Next Improvement
Introduce source-grounded evidence retrieval and validation.

## Lab 02 — Claim Verification and Tracking

### Implementation
I developed the `evaluate_claim()` function to examine the
source field of a research claim and return either
`NEEDS REVIEW` or `NEEDS VERIFICATION`.

### Engineering Decision
I separated the evaluation logic into `claim_evaluator.py`
to make the function reusable and independently testable.

### Automated Testing
I implemented two unit tests using Python's `unittest`
framework to verify the function's behavior when a
source is missing or assigned.

Both tests passed.

### Current Limitation
My implementation checks whether a source is assigned,
but it does not yet determine whether that source
actually supports the research claim. Human verification
remains necessary.