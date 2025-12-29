#!/usr/bin/env python3
"""
Responsible Disclosure Tracker
Manage vulnerability disclosure timelines
"""

import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum


class DisclosureStatus(Enum):
    DRAFT = "draft"
    REPORTED = "reported"
    ACKNOWLEDGED = "acknowledged"
    IN_PROGRESS = "in_progress"
    FIXED = "fixed"
    DISCLOSED = "disclosed"


@dataclass
class Vulnerability:
    """Tracked vulnerability"""
    id: str
    title: str
    severity: str
    vendor: str
    reported_date: str
    status: DisclosureStatus
    disclosure_deadline: str
    notes: List[str] = field(default_factory=list)


class DisclosureTracker:
    """Track responsible disclosure process"""

    # Standard disclosure timeline (days)
    TIMELINES = {
        "CRITICAL": 30,
        "HIGH": 60,
        "MEDIUM": 90,
        "LOW": 120
    }

    def __init__(self):
        self.vulnerabilities: Dict[str, Vulnerability] = {}

    def report_vulnerability(
        self,
        vuln_id: str,
        title: str,
        severity: str,
        vendor: str
    ) -> Vulnerability:
        """Report a new vulnerability"""
        now = datetime.now()
        days = self.TIMELINES.get(severity.upper(), 90)
        deadline = (now + timedelta(days=days)).isoformat()

        vuln = Vulnerability(
            id=vuln_id,
            title=title,
            severity=severity.upper(),
            vendor=vendor,
            reported_date=now.isoformat(),
            status=DisclosureStatus.REPORTED,
            disclosure_deadline=deadline,
            notes=[f"Reported to {vendor} on {now.strftime('%Y-%m-%d')}"]
        )

        self.vulnerabilities[vuln_id] = vuln
        return vuln

    def update_status(self, vuln_id: str, status: DisclosureStatus, note: str = None) -> bool:
        """Update vulnerability status"""
        if vuln_id not in self.vulnerabilities:
            return False

        self.vulnerabilities[vuln_id].status = status
        if note:
            self.vulnerabilities[vuln_id].notes.append(
                f"[{datetime.now().strftime('%Y-%m-%d')}] {note}"
            )
        return True

    def get_pending_disclosures(self) -> List[Dict]:
        """Get vulnerabilities pending disclosure"""
        now = datetime.now()
        pending = []

        for vuln in self.vulnerabilities.values():
            if vuln.status != DisclosureStatus.DISCLOSED:
                deadline = datetime.fromisoformat(vuln.disclosure_deadline)
                days_remaining = (deadline - now).days

                pending.append({
                    "id": vuln.id,
                    "title": vuln.title,
                    "severity": vuln.severity,
                    "vendor": vuln.vendor,
                    "status": vuln.status.value,
                    "days_remaining": days_remaining,
                    "overdue": days_remaining < 0
                })

        return sorted(pending, key=lambda x: x["days_remaining"])

    def generate_report(self, vuln_id: str) -> Optional[Dict]:
        """Generate disclosure report"""
        if vuln_id not in self.vulnerabilities:
            return None

        vuln = self.vulnerabilities[vuln_id]
        return {
            "vulnerability_id": vuln.id,
            "title": vuln.title,
            "severity": vuln.severity,
            "vendor": vuln.vendor,
            "timeline": {
                "reported": vuln.reported_date,
                "deadline": vuln.disclosure_deadline,
                "current_status": vuln.status.value
            },
            "history": vuln.notes
        }


def main():
    tracker = DisclosureTracker()

    print("Responsible Disclosure Tracker")
    print("=" * 50)

    # Report a vulnerability
    vuln = tracker.report_vulnerability(
        "VULN-2024-001",
        "Prompt Injection in ChatBot API",
        "HIGH",
        "Example Corp"
    )
    print(f"Reported: {vuln.title}")
    print(f"Deadline: {vuln.disclosure_deadline}")

    # Update status
    tracker.update_status(
        "VULN-2024-001",
        DisclosureStatus.ACKNOWLEDGED,
        "Vendor acknowledged receipt"
    )

    # Check pending
    pending = tracker.get_pending_disclosures()
    print(f"\nPending Disclosures: {len(pending)}")
    for p in pending:
        print(f"  - {p['id']}: {p['days_remaining']} days remaining")

    # Generate report
    report = tracker.generate_report("VULN-2024-001")
    with open("disclosure_report.json", "w") as f:
        json.dump(report, f, indent=2)


if __name__ == "__main__":
    main()
