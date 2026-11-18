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


## Lab 03 — Research Document Ingestion

### Objective
I developed a reusable Python component to read research documents
and make their contents available for further processing.

### Implementation
I created `document_loader.py` with a `read_document()` function
that accepts a file path and returns the document's contents as a string.

I separated the document-loading logic from `document_reader.py`
to maintain clear responsibilities between components.

### Engineering Decisions
- I applied the DRY (Don't Repeat Yourself) principle by removing
  duplicate file-reading code.
- I applied separation of concerns by keeping document loading
  independent of application-specific error messages.
- I used `with open()` to ensure files are automatically closed.
- I specified UTF-8 encoding for text processing.

### Testing
I implemented two automated tests using Python's `unittest` framework:

1. `test_read_existing_document()` — verifies that text can be
   extracted from an existing document.
2. `test_missing_document()` — verifies that a missing document
   raises `FileNotFoundError`.

Both tests passed.

### Current Limitations
My document loader currently supports plain-text files.
It does not yet extract text from PDF or Word documents.

The application can locate keywords, but keyword matches alone
do not establish scientific evidence.


## Lab 04 — Document Processing and Retrieval

### Objective
I developed a modular retrieval pipeline that processes research
documents into searchable passages while preserving source attribution.

### Implementation
I created two reusable Python modules:

- `document_chunker.py` — divides document text into paragraphs,
  removes unnecessary whitespace, and excludes empty chunks.
- `document_retriever.py` — searches chunks using case-insensitive
  keyword matching and returns structured results.

I updated `document_reader.py` to coordinate document loading,
chunking, retrieval, and result presentation.

### Engineering Decisions
- I applied separation of concerns by assigning each module a
  specific responsibility.
- I cleaned document chunks before retrieval.
- I used Python dictionaries to associate matching passages
  with their source document.
- I designed the retriever to return an empty list when no
  keyword matches are found.
- I kept retrieval separate from scientific claim verification.

### Automated Testing
I implemented three tests using Python's unittest framework:

1. `test_matching_keyword()` — verifies successful retrieval.
2. `test_missing_keyword()` — verifies empty search results.
3. `test_source_attribution()` — verifies source preservation.

All three tests passed.

### Debugging
I diagnosed a ModuleNotFoundError caused by a filename mismatch:
`test-document_retriever.py` versus `test_document_retriever.py`.

I corrected the filename without modifying the application logic.

### Current Limitations
- Retrieval uses exact substring matching, ignoring letter case.
- Chunking relies on blank-line separators.
- Source attribution currently records a filename, not page numbers
  or precise passage locations.
- The system does not yet determine whether retrieved text
  scientifically supports a claim.

### Engineering Takeaway
I built a retrieval pipeline that reads, chunks, cleans, searches,
and attributes research information to its source.

I am developing the foundation for Retrieval-Augmented Generation
(RAG), where retrieved evidence can inform AI-generated responses.

