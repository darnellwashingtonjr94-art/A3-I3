# core_agi/main.py
import ctypes
from task_delegation.router import TaskRouter
from synthesis.merger import OutputMerger
from world_model.state import WorldModel

class AGICore:
    def __init__(self):
        self.world_model = WorldModel()
        self.router = TaskRouter()
        self.merger = OutputMerger()
        
        # Load ASI Interop Bridge
        self.asi_bridge = ctypes.CDLL("../interop_bridge/target/release/libinterop.so")

    def process_prompt(self, prompt: str):
        self.world_model.update_context(prompt)
        tasks = self.router.decompose(prompt)
        
        ani_results = []
        for task in tasks:
            # Delegate to specialized ANI modules
            ani_results.append(self.router.dispatch(task))
            
        final_output = self.merger.synthesize(ani_results)
        return final_output

if __name__ == "__main__":
    engine = AGICore()
    engine.process_prompt("Initialize A3-I3 Engine sequence.")
