"""Log Analyzer Module"""
import re

class LogAnalyzer:
    def __init__(self):
        self.patterns = {
            "error": r"(?i)error|exception|failed|fatal",
            "warning": r"(?i)warn|timeout|retry",
            "latency": r"(?i)latency|slow",
            "auth": r"(?i)unauthorized|forbidden|401|403"
        }
    
    def analyze(self, logs: str) -> dict:
        results = {"total_lines": len(logs.split("\n")), "patterns_found": {}}
        for ptype, pattern in self.patterns.items():
            results["patterns_found"][ptype] = len(re.findall(pattern, logs))
        results["has_anomaly"] = any(v > 5 for v in results["patterns_found"].values())
        return results
