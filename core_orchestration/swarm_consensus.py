class SwarmConsensusPool:
    def __init__(self, agents):
        self.agents = agents # List of available ANI nodes

    def deliberate(self, problem_statement):
        print("[Swarm Consensus] Initiating multi-agent peer review and debate...")
        votes = {}
        
        for agent in self.agents:
            perspective = agent.execute(problem_statement)
            # Each agent casts a weighted vote based on its domain expertise
            confidence_weight = 0.9 if "Success" in str(perspective) else 0.5
            votes[agent] = confidence_weight

        # Determine consensus
        top_agent = max(votes, key=votes.get)
        print(f"[Swarm Consensus] Consensus reached. Lead voting agent: {top_agent}")
        
        return {
            "consensus_achieved": True,
            "selected_strategy": top_agent,
            "aggregate_confidence": sum(votes.values()) / len(votes)
        }
