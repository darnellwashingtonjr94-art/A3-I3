from core_orchestration.router import AGIOrchestratorRouter
from asi_meta_layer.meta_controller import ASIMetaLayer
from simulation_sandbox.sandbox import SimulationSandbox

def initialize_system():
    asi = ASIMetaLayer()
    sandbox = SimulationSandbox()
    router = AGIOrchestratorRouter(asi_layer=asi, sandbox=sandbox)
    return router

# 1. Expose the application at the top level so Vercel can find it
app = initialize_system()

if __name__ == "__main__":
    # 2. You can still test locally using the 'app' variable
    
    # Test Prompt
    prompt = "Global logistics offline. Satelli..."
    result = app.route_prompt(prompt)
    print("Final Output Synthesis:", result)
