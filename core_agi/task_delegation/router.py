# core_agi/task_delegation/router.py
from core_ani.math_engine.solver import MathSolver
from core_ani.nlp_parser.extractor import NLPExtractor

class TaskRouter:
    def __init__(self):
        self.math_executor = MathSolver()
        self.nlp_executor = NLPExtractor()

    def decompose(self, prompt: str) -> list:
        # Determine prompt complexity and split into specialized sub-tasks
        return [{"type": "nlp", "payload": prompt}]

    def dispatch(self, task: dict):
        if task["type"] == "math":
            return self.math_executor.calculate(task["payload"])
        elif task["type"] == "nlp":
            return self.nlp_executor.parse(task["payload"])
        else:
            raise ValueError(f"Unknown task type: {task['type']}")
