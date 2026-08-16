"""
ResText core package.

Modules:
    ingestion    - reading & cleaning raw text/CSV corpora
    processing   - spaCy-based named entity extraction
    aggregation  - pandas-based summarisation of extracted entities
    export       - writing results to CSV/JSON
"""

from . import ingestion, processing, aggregation, export  # noqa: F401
