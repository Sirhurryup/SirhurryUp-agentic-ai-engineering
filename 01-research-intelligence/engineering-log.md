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