# core_agi/world_model/graph.py
class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_concept(self, concept_id: str, attributes: dict):
        if concept_id not in self.nodes:
            self.nodes[concept_id] = attributes
            
    def link_concepts(self, source: str, target: str, relationship: str):
        if source in self.nodes and target in self.nodes:
            self.edges.append((source, target, relationship))
            
    def query_subgraph(self, context_key: str) -> list:
        # Returns adjacent nodes to instantly prime context memory
        return [edge for edge in self.edges if context_key in edge]
