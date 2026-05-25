"""Incident Classifier Module"""
import random

class IncidentClassifier:
    def classify(self, alert: str, service: str) -> dict:
        severity = random.choice(["critical", "high", "medium", "low"])
        return {
            "severity": severity,
            "priority": {"critical": "P1", "high": "P2", "medium": "P3", "low": "P4"}[severity],
            "category": random.choice(["infrastructure", "application", "security"]),
            "team": random.choice(["sre", "backend", "platform"])
        }
