class AlignmentMonitor:
    def __init__(self):
        self.constitutional_rules = [
            "no_direct_harm_to_human_life",
            "preserve_system_transparency",
            "respect_operational_boundaries"
        ]

    def audit_solution(self, proposed_solution):
        print("[Ethics Monitor] Auditing proposed solution against constitutional guardrails...")
        
        # Simulated safety checks
        for rule in self.constitutional_rules:
            if self.violates(proposed_solution, rule):
                print(f"[Ethics Monitor] ALERT: Violation detected for rule -> {rule}")
                return {"status": "BLOCKED", "reason": f"Failed constitutional check: {rule}"}
                
        print("[Ethics Monitor] Audit passed. Solution aligns with safety constraints.")
        return {"status": "PASSED"}

    def violates(self, solution, rule):
        # Placeholder logic for deep ethical evaluation
        if "harm" in str(solution).lower():
            return True
        return False
