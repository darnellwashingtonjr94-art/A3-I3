from core_orchestration.router import AGIOrchestratorRouter
from asi_meta_layer.meta_controller import ASIMetaLayer
from simulation_sandbox.sandbox import SimulationSandbox

def initialize_system():
    asi = ASIMetaLayer()
    sandbox = SimulationSandbox()
    router = AGIOrchestratorRouter(asi_layer=asi, sandbox_layer=sandbox)
    return router

if __name__ == "__main__":
    system = initialize_system()
    
    # Test Prompt
    prompt = "Global logistics offline. Satellites failing. Advise immediate stabilization."
    result = system.route_prompt(prompt)
    print("Final Output Synthesis:", result)
