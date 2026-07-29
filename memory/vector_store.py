import math

class VectorMemoryStore:
    def __init__(self):
        self.memory_index = [] # Stores tuple of (vector_embedding, solution_payload)

    def encode_prompt(self, text):
        # Simulated embedding generation based on keyword weights and length
        return [float(len(text)), float(text.count("crisis")), float(text.count("offline"))]

    def cosine_similarity(self, vec1, vec2):
        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        magnitude1 = math.sqrt(sum(a ** 2 for a in vec1))
        magnitude2 = math.sqrt(sum(b ** 2 for b in vec2))
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        return dot_product / (magnitude1 * magnitude2)

    def retrieve_relevant_memory(self, user_prompt, threshold=0.80):
        print("[Memory Agent] Querying vector space for historical patterns...")
        query_vector = self.encode_prompt(user_prompt)
        
        best_match = None
        highest_score = 0.0

        for stored_vector, solution in self.memory_index:
            score = self.cosine_similarity(query_vector, stored_vector)
            if score > highest_score:
                highest_score = score
                best_match = solution

        if highest_score >= threshold:
            print(f"[Memory Agent] High confidence match found (Score: {round(highest_score, 2)})")
            return best_match
        
        print("[Memory Agent] No direct match found. Proceeding with active routing.")
        return None

    def store_experience(self, user_prompt, approved_solution):
        vector = self.encode_prompt(user_prompt)
        self.memory_index.append((vector, approved_solution))
        print("[Memory Agent] New operational cycle successfully indexed into memory.")
