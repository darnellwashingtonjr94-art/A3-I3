# core_ani/nlp_parser/__init__.py
from .extractor import NLPExtractor

def parse_input_syntax(raw_text: str) -> dict:
    parser = NLPExtractor()
    return parser.parse(raw_text)
