#!/usr/bin/env python3
"""
Certification and Training Progress Tracker
Track learning paths for AI security certifications
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List
from dataclasses import dataclass, field


@dataclass
class LearningModule:
    """A learning module in a certification path"""
    id: str
    name: str
    hours: float
    completed: bool = False
    completion_date: str = None


@dataclass
class Certification:
    """Certification track with modules"""
    name: str
    provider: str
    modules: List[LearningModule] = field(default_factory=list)
    target_date: str = None


class ProgressTracker:
    """Track certification and training progress"""

    CERTIFICATIONS = {
        "GPEN": {
            "name": "GIAC Penetration Tester",
            "provider": "SANS/GIAC",
            "modules": [
                ("network-attacks", "Network Attack Techniques", 20),
                ("web-app-testing", "Web Application Testing", 15),
                ("privilege-escalation", "Privilege Escalation", 12),
                ("lateral-movement", "Lateral Movement", 10),
            ],
            "total_hours": 57
        },
        "CEH": {
            "name": "Certified Ethical Hacker",
            "provider": "EC-Council",
            "modules": [
                ("footprinting", "Footprinting and Reconnaissance", 8),
                ("scanning", "Scanning Networks", 6),
                ("enumeration", "Enumeration", 5),
                ("vulnerability-analysis", "Vulnerability Analysis", 8),
                ("system-hacking", "System Hacking", 10),
            ],
            "total_hours": 37
        },
        "AI-RED-TEAM": {
            "name": "AI Red Team Specialist",
            "provider": "Custom Path",
            "modules": [
                ("llm-fundamentals", "LLM Security Fundamentals", 10),
                ("prompt-injection", "Prompt Injection Mastery", 15),
                ("jailbreaking", "Jailbreak Techniques", 12),
                ("defense", "Defense Implementation", 10),
                ("reporting", "Security Reporting", 5),
            ],
            "total_hours": 52
        }
    }

    def __init__(self):
        self.progress: Dict[str, Certification] = {}

    def start_certification(self, cert_id: str, target_weeks: int = 12) -> Certification:
        """Start tracking a certification"""
        if cert_id not in self.CERTIFICATIONS:
            raise ValueError(f"Unknown certification: {cert_id}")

        cert_info = self.CERTIFICATIONS[cert_id]
        modules = [
            LearningModule(id=m[0], name=m[1], hours=m[2])
            for m in cert_info["modules"]
        ]

        target = (datetime.now() + timedelta(weeks=target_weeks)).isoformat()

        cert = Certification(
            name=cert_info["name"],
            provider=cert_info["provider"],
            modules=modules,
            target_date=target
        )

        self.progress[cert_id] = cert
        return cert

    def complete_module(self, cert_id: str, module_id: str) -> bool:
        """Mark a module as completed"""
        if cert_id not in self.progress:
            return False

        for module in self.progress[cert_id].modules:
            if module.id == module_id:
                module.completed = True
                module.completion_date = datetime.now().isoformat()
                return True
        return False

    def get_progress_report(self, cert_id: str) -> Dict:
        """Get progress report for a certification"""
        if cert_id not in self.progress:
            return {"error": "Certification not found"}

        cert = self.progress[cert_id]
        completed = sum(1 for m in cert.modules if m.completed)
        total = len(cert.modules)
        hours_completed = sum(m.hours for m in cert.modules if m.completed)
        hours_total = sum(m.hours for m in cert.modules)

        return {
            "certification": cert.name,
            "provider": cert.provider,
            "progress": f"{completed}/{total} modules ({completed/total*100:.0f}%)",
            "hours": f"{hours_completed:.0f}/{hours_total:.0f} hours",
            "target_date": cert.target_date,
            "modules": [
                {
                    "name": m.name,
                    "hours": m.hours,
                    "status": "Completed" if m.completed else "Pending"
                }
                for m in cert.modules
            ]
        }


def main():
    tracker = ProgressTracker()

    print("Available Certifications:")
    for cert_id, info in tracker.CERTIFICATIONS.items():
        print(f"  - {cert_id}: {info['name']} ({info['total_hours']} hours)")

    # Start AI Red Team certification
    cert = tracker.start_certification("AI-RED-TEAM", target_weeks=8)
    print(f"\nStarted: {cert.name}")

    # Complete some modules
    tracker.complete_module("AI-RED-TEAM", "llm-fundamentals")
    tracker.complete_module("AI-RED-TEAM", "prompt-injection")

    # Get progress report
    report = tracker.get_progress_report("AI-RED-TEAM")
    print(f"\nProgress: {report['progress']}")
    print(f"Hours: {report['hours']}")

    with open("training_progress.json", "w") as f:
        json.dump(report, f, indent=2)
    print("\nProgress saved to training_progress.json")


if __name__ == "__main__":
    main()
