from fastapi import FastAPI
from core_orchestration.router import AGIOrchestratorRouter
from asi_meta_layer.meta_controller import ASIMetaLayer
from simulation_sandbox.sandbox import SimulationSandbox

# 1. Initialize your web app for Vercel
app = FastAPI()

# 2. Initialize your custom logic
def initialize_system():
    asi = ASIMetaLayer()
    sandbox = SimulationSandbox()
    router = AGIOrchestratorRouter(asi_layer=asi, sandbox=sandbox)
    return router

system = initialize_system()

# 3. Create a web endpoint for Vercel to route traffic to
@app.get("/")
def run_orchestrator():
    prompt = "Global logistics offline. Satelli..."
    result = system.route_prompt(prompt)
    return {"status": "success", "output": result}
