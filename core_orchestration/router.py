from core_orchestration.entropy_evaluator import EntropyEvaluator
from ani_specialized_nodes.heuristic_engine import HeuristicEngine
from ani_specialized_nodes.math_engine import MathEngine

class AGIOrchestratorRouter:
    def __init__(self, asi_layer, sandbox_layer):
        self.asi = asi_layer
        self.sandbox = sandbox_layer
        self.evaluator = EntropyEvaluator()
        self.heuristic_engine = HeuristicEngine()
        self.math_engine = MathEngine()

    def route_prompt(self, user_prompt):
        tier = self.evaluator.evaluate_entropy(user_prompt)
        print(f"[Orchestrator] Problem Tier Classified: {tier}")

        if tier == "CLEAR_EASY":
            return self.math_engine.execute(user_prompt)
        
        elif tier == "COMPLICATED":
            return "Executing parallel multi-ANI expert synthesis..."
        
        elif tier == "COMPLEX":
            raw_solution = self.heuristic_engine.lateral_think(user_prompt)
            validated = self.sandbox.stress_test(raw_solution)
            return validated
        
        elif tier == "CHAOTIC":
            # Direct escalation to ASI Meta-Layer for dynamic recompilation
            raw_crisis_solution = self.asi.trigger_recompilation(user_prompt)
            return self.sandbox.stress_test(raw_crisis_solution)
