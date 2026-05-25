"""Remediation Engine Module"""
class RemediationEngine:
    def __init__(self):
        self.playbooks = {
            "memory_leak": ["Restart service", "Increase memory limit", "Profile heap"],
            "high_latency": ["Check DB connections", "Scale horizontally", "Enable cache"],
            "connection_error": ["Check firewall", "Verify DNS", "Restart pods"]
        }
    
    def get_steps(self, issue_type: str) -> list:
        steps = self.playbooks.get(issue_type, ["Check logs", "Restart service"])
        return [{"order": i+1, "action": step} for i, step in enumerate(steps)]
    
    def can_auto_fix(self, issue_type: str) -> bool:
        return issue_type in ["high_latency", "connection_error"]
