# core_agi/task_delegation/__init__.py
from .router import TaskRouter

def init_router() -> TaskRouter:
    # Initializes the multi-domain decomposition network
    return TaskRouter()
