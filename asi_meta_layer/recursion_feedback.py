class RecursionFeedbackLoop:
    def __init__(self, memory_store):
        self.memory = memory_store
        self.cycle_history = []

    def log_cycle(self, prompt, tier, solution, confidence):
        record = {
            "prompt": prompt,
            "tier": tier,
            "solution": solution,
            "confidence": confidence
        }
        self.cycle_history.append(record)
        
        # Trigger background meta-learning evaluation
        self.evaluate_and_adapt(record)

    def evaluate_and_adapt(self, record):
        print("[ASI Meta-Layer] Running background meta-learning and self-reflection...")
        
        # If a chaotic problem was successfully resolved, commit it to long-term memory
        if record["tier"] == "CHAOTIC" and record["confidence"] >= 0.85:
            self.memory.store_experience(record["prompt"], record["solution"])
            print("[ASI Meta-Layer] Optimization complete: Chaotic pathway optimized into standard recall profile.")
        else:
            print("[ASI Meta-Layer] Cycle logged. No structural recompilation required.")
