#!/usr/bin/env python3
"""
LLM Security Testing Methodology Framework
Structured approach to security testing
"""

import json
from typing import Dict, List
from dataclasses import dataclass, field
from enum import Enum


class TestPhase(Enum):
    RECONNAISSANCE = "reconnaissance"
    THREAT_MODELING = "threat_modeling"
    VULNERABILITY_TESTING = "vulnerability_testing"
    EXPLOITATION = "exploitation"
    REPORTING = "reporting"


@dataclass
class TestActivity:
    """Individual testing activity"""
    id: str
    phase: TestPhase
    name: str
    description: str
    duration_hours: float
    outputs: List[str]


class TestingMethodology:
    """LLM security testing methodology"""

    PHASES = {
        TestPhase.RECONNAISSANCE: [
            TestActivity("REC-01", TestPhase.RECONNAISSANCE,
                         "System Profiling", "Identify model type, endpoints, capabilities",
                         2.0, ["System profile document"]),
            TestActivity("REC-02", TestPhase.RECONNAISSANCE,
                         "API Analysis", "Document API endpoints and parameters",
                         3.0, ["API inventory"]),
            TestActivity("REC-03", TestPhase.RECONNAISSANCE,
                         "Baseline Behavior", "Establish normal response patterns",
                         2.0, ["Baseline report"]),
        ],
        TestPhase.THREAT_MODELING: [
            TestActivity("TM-01", TestPhase.THREAT_MODELING,
                         "Attack Surface Analysis", "Identify potential attack vectors",
                         4.0, ["Attack surface diagram"]),
            TestActivity("TM-02", TestPhase.THREAT_MODELING,
                         "Risk Prioritization", "Rank threats by likelihood and impact",
                         2.0, ["Risk matrix"]),
        ],
        TestPhase.VULNERABILITY_TESTING: [
            TestActivity("VT-01", TestPhase.VULNERABILITY_TESTING,
                         "Prompt Injection", "Test for instruction override vulnerabilities",
                         6.0, ["Injection test results"]),
            TestActivity("VT-02", TestPhase.VULNERABILITY_TESTING,
                         "Jailbreak Testing", "Attempt to bypass safety mechanisms",
                         4.0, ["Jailbreak test results"]),
            TestActivity("VT-03", TestPhase.VULNERABILITY_TESTING,
                         "Data Leakage", "Test for unintended information disclosure",
                         4.0, ["Leakage assessment"]),
        ],
        TestPhase.EXPLOITATION: [
            TestActivity("EX-01", TestPhase.EXPLOITATION,
                         "Proof of Concept", "Develop working exploits for findings",
                         4.0, ["PoC demonstrations"]),
            TestActivity("EX-02", TestPhase.EXPLOITATION,
                         "Impact Assessment", "Evaluate real-world impact of vulnerabilities",
                         2.0, ["Impact analysis"]),
        ],
        TestPhase.REPORTING: [
            TestActivity("REP-01", TestPhase.REPORTING,
                         "Technical Report", "Document all findings with evidence",
                         4.0, ["Technical report"]),
            TestActivity("REP-02", TestPhase.REPORTING,
                         "Executive Summary", "High-level summary for leadership",
                         2.0, ["Executive summary"]),
            TestActivity("REP-03", TestPhase.REPORTING,
                         "Remediation Plan", "Detailed fix recommendations",
                         3.0, ["Remediation roadmap"]),
        ],
    }

    def __init__(self):
        self.test_plan: List[TestActivity] = []
        self.completed: List[str] = []

    def generate_test_plan(self, scope: str = "full") -> Dict:
        """Generate testing plan based on scope"""
        if scope == "quick":
            phases = [TestPhase.VULNERABILITY_TESTING, TestPhase.REPORTING]
        elif scope == "standard":
            phases = [TestPhase.RECONNAISSANCE, TestPhase.VULNERABILITY_TESTING, TestPhase.REPORTING]
        else:  # full
            phases = list(TestPhase)

        total_hours = 0
        for phase in phases:
            for activity in self.PHASES.get(phase, []):
                self.test_plan.append(activity)
                total_hours += activity.duration_hours

        return {
            "scope": scope,
            "phases": [p.value for p in phases],
            "activities": len(self.test_plan),
            "estimated_hours": total_hours,
            "estimated_days": total_hours / 8,
            "plan": [
                {
                    "id": a.id,
                    "phase": a.phase.value,
                    "name": a.name,
                    "hours": a.duration_hours
                }
                for a in self.test_plan
            ]
        }

    def mark_complete(self, activity_id: str) -> bool:
        """Mark activity as complete"""
        if any(a.id == activity_id for a in self.test_plan):
            self.completed.append(activity_id)
            return True
        return False

    def get_progress(self) -> Dict:
        """Get testing progress"""
        return {
            "total": len(self.test_plan),
            "completed": len(self.completed),
            "remaining": len(self.test_plan) - len(self.completed),
            "progress_percent": f"{len(self.completed)/len(self.test_plan)*100:.0f}%" if self.test_plan else "0%"
        }


def main():
    methodology = TestingMethodology()

    print("LLM Security Testing Methodology")
    print("=" * 50)

    # Generate test plan
    plan = methodology.generate_test_plan("full")

    print(f"Scope: {plan['scope']}")
    print(f"Activities: {plan['activities']}")
    print(f"Estimated: {plan['estimated_days']:.1f} days")

    print("\nTest Plan:")
    for activity in plan["plan"]:
        print(f"  {activity['id']}: {activity['name']} ({activity['hours']}h)")

    # Save plan
    with open("test_methodology.json", "w") as f:
        json.dump(plan, f, indent=2)


if __name__ == "__main__":
    main()
