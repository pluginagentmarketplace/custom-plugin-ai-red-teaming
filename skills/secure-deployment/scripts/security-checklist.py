#!/usr/bin/env python3
"""
Secure Deployment Checklist
Verify security configurations before deployment
"""

import json
from typing import Dict, List
from dataclasses import dataclass
from enum import Enum


class CheckStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    WARN = "WARN"
    SKIP = "SKIP"


@dataclass
class SecurityCheck:
    """Security checklist item"""
    id: str
    category: str
    name: str
    description: str
    severity: str
    remediation: str


class DeploymentChecker:
    """Run security checks for LLM deployment"""

    CHECKS = [
        # Authentication
        SecurityCheck("SEC-001", "auth", "API Key Rotation",
                      "API keys should be rotated regularly",
                      "HIGH", "Implement key rotation every 90 days"),
        SecurityCheck("SEC-002", "auth", "Rate Limiting",
                      "Rate limiting should be enabled",
                      "HIGH", "Configure rate limits per user/IP"),

        # Network
        SecurityCheck("SEC-003", "network", "TLS Encryption",
                      "All traffic should be encrypted",
                      "CRITICAL", "Enable TLS 1.3 for all endpoints"),
        SecurityCheck("SEC-004", "network", "Firewall Rules",
                      "Only necessary ports should be open",
                      "HIGH", "Review and restrict firewall rules"),

        # Application
        SecurityCheck("SEC-005", "app", "Input Validation",
                      "All inputs should be validated",
                      "CRITICAL", "Implement input sanitization"),
        SecurityCheck("SEC-006", "app", "Output Filtering",
                      "Sensitive data should be filtered from outputs",
                      "HIGH", "Enable output content filtering"),

        # Monitoring
        SecurityCheck("SEC-007", "monitoring", "Audit Logging",
                      "Security events should be logged",
                      "MEDIUM", "Enable comprehensive audit logging"),
        SecurityCheck("SEC-008", "monitoring", "Alerting",
                      "Security alerts should be configured",
                      "MEDIUM", "Set up alerting for security events"),

        # Data
        SecurityCheck("SEC-009", "data", "Secrets Management",
                      "Secrets should be stored securely",
                      "CRITICAL", "Use vault for secret storage"),
        SecurityCheck("SEC-010", "data", "Backup Encryption",
                      "Backups should be encrypted",
                      "HIGH", "Enable encryption for all backups"),
    ]

    def __init__(self):
        self.results: List[Dict] = []

    def run_check(self, check: SecurityCheck, status: CheckStatus, notes: str = "") -> Dict:
        """Run a single security check"""
        result = {
            "id": check.id,
            "category": check.category,
            "name": check.name,
            "severity": check.severity,
            "status": status.value,
            "notes": notes,
            "remediation": check.remediation if status == CheckStatus.FAIL else None
        }
        self.results.append(result)
        return result

    def run_all_checks(self, config: Dict) -> Dict:
        """Run all security checks against config"""
        for check in self.CHECKS:
            # Simulate check based on config
            if check.id in config.get("enabled_controls", []):
                self.run_check(check, CheckStatus.PASS, "Control enabled")
            elif check.severity == "CRITICAL":
                self.run_check(check, CheckStatus.FAIL, "Critical control missing")
            else:
                self.run_check(check, CheckStatus.WARN, "Consider enabling")

        return self.get_summary()

    def get_summary(self) -> Dict:
        """Get check summary"""
        by_status = {s.value: 0 for s in CheckStatus}
        for r in self.results:
            by_status[r["status"]] += 1

        critical_fails = [r for r in self.results
                         if r["status"] == "FAIL" and r["severity"] == "CRITICAL"]

        return {
            "total_checks": len(self.results),
            "by_status": by_status,
            "critical_failures": len(critical_fails),
            "deployment_ready": len(critical_fails) == 0,
            "details": self.results
        }


def main():
    checker = DeploymentChecker()

    print("Secure Deployment Checklist")
    print("=" * 50)

    # Simulate config
    config = {
        "enabled_controls": ["SEC-001", "SEC-003", "SEC-005", "SEC-007"]
    }

    summary = checker.run_all_checks(config)

    for r in summary["details"]:
        print(f"[{r['status']}] {r['id']}: {r['name']} ({r['severity']})")

    print(f"\nDeployment Ready: {'YES' if summary['deployment_ready'] else 'NO'}")
    print(f"Critical Failures: {summary['critical_failures']}")

    with open("deployment_checklist.json", "w") as f:
        json.dump(summary, f, indent=2)


if __name__ == "__main__":
    main()
