# core_agi/synthesis/merger.py
class OutputMerger:
    def __init__(self):
        self.synthesis_format = "standard"

    def synthesize(self, results: list) -> str:
        if not results:
            return "No operation performed."
            
        # Combine deterministic ANI outputs into natural language response
        merged_output = " | ".join([str(res) for res in results])
        return f"[AGI_SYNTHESIS] Output: {merged_output}"
