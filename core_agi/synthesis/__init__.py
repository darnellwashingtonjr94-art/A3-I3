# core_agi/synthesis/__init__.py
from .merger import OutputMerger

def init_synthesis_pipeline() -> OutputMerger:
    # Exposes the merging pipeline to the main orchestrator loop
    return OutputMerger()
