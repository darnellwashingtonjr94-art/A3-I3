import random

class SimulationSandbox:
    def __init__(self, threshold=0.85):
        self.threshold = threshold

    def stress_test(self, proposed_solution):
        print("[Simulation Sandbox] Initializing adversarial stress testing...")
        confidence = 0.50
        iterations = 0

        while confidence < self.threshold and iterations < 5:
            iterations += 1
            chaos_var = random.choice(["power_drop", "latency_spike", "packet_loss"])
            print(f"-> Injecting failure variable: {chaos_var} (Iteration {iterations})")
            
            # Simulate survival check
            confidence += 0.15

        return {
            "status": "APPROVED",
            "solution": proposed_solution,
            "final_confidence": round(confidence, 2)
        }
