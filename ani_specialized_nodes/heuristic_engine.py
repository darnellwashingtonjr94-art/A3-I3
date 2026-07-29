import random

class HeuristicEngine:
    def __init__(self):
        self.domains = {
            "Mycology": "fungal network nutrient distribution",
            "Game Theory": "zero-sum cooperative equilibrium",
            "Fluid Dynamics": "pressure-relief laminar flow"
        }

    def lateral_think(self, problem):
        domain = random.choice(list(self.domains.keys()))
        pattern = self.domains[domain]
        print(f"[Heuristic Engine] Applying cross-domain metaphor from {domain}")
        return f"Solution mapped using {pattern} to bypass logical deadlock."
