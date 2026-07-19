# core_ani/math_engine/__init__.py
from .solver import MathSolver

def run_isolated_calculation(expression_string: str) -> dict:
    executor = MathSolver()
    return executor.calculate(expression_string)
