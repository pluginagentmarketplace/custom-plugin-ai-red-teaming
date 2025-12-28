#!/usr/bin/env python3
"""
LLM Security Test Runner
Automated security testing for LLM systems with CI/CD integration.
"""

import yaml
import json
import argparse
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime
import concurrent.futures

class TestResult(Enum):
    PASS = "pass"
    FAIL = "fail"
    ERROR = "error"
    SKIP = "skip"

class Severity(Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"

@dataclass
class TestCase:
    """Individual test case."""
    id: str
    name: str
    category: str
    payload: str
    expected: str
    severity: Severity = Severity.MEDIUM

@dataclass
class TestOutcome:
    """Result of executing a test case."""
    test_id: str
    test_name: str
    result: TestResult
    severity: Severity
    response: Optional[str]
    duration_ms: int
    notes: str = ""

class SecurityTestRunner:
    """Execute security tests against LLM endpoints."""

    def __init__(self, config_path: str = "assets/test-suite.yaml"):
        self.config = self._load_config(config_path)
        self.results: List[TestOutcome] = []
        self.start_time = datetime.now()

    def _load_config(self, path: str) -> Dict:
        """Load test configuration."""
        try:
            with open(path, 'r') as f:
                return yaml.safe_load(f)
        except FileNotFoundError:
            return {"test_categories": {}}

    def _execute_test(self, test: TestCase) -> TestOutcome:
        """Execute a single test case."""
        start = datetime.now()

        # Placeholder for actual LLM API call
        # response = call_llm_api(test.payload)
        response = "[Mock response - implement API call]"

        duration = int((datetime.now() - start).total_seconds() * 1000)

        # Evaluate result
        result = TestResult.PASS  # Placeholder

        return TestOutcome(
            test_id=test.id,
            test_name=test.name,
            result=result,
            severity=test.severity,
            response=response[:200],  # Truncate for report
            duration_ms=duration
        )

    def load_tests(self) -> List[TestCase]:
        """Load all test cases from configuration."""
        tests = []
        categories = self.config.get("test_categories", {})

        for category_name, category_config in categories.items():
            if not category_config.get("enabled", True):
                continue

            priority = category_config.get("priority", "medium")
            for test_config in category_config.get("tests", []):
                tests.append(TestCase(
                    id=test_config["id"],
                    name=test_config["name"],
                    category=category_name,
                    payload=test_config["payload"],
                    expected=test_config["expected"],
                    severity=Severity(priority)
                ))

        return tests

    def run_all(self, parallel: bool = True) -> List[TestOutcome]:
        """Run all tests."""
        tests = self.load_tests()
        print(f"Running {len(tests)} security tests...")

        if parallel:
            with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
                self.results = list(executor.map(self._execute_test, tests))
        else:
            self.results = [self._execute_test(t) for t in tests]

        return self.results

    def generate_report(self) -> Dict:
        """Generate test report."""
        passed = sum(1 for r in self.results if r.result == TestResult.PASS)
        failed = sum(1 for r in self.results if r.result == TestResult.FAIL)

        return {
            "summary": {
                "total": len(self.results),
                "passed": passed,
                "failed": failed,
                "pass_rate": f"{(passed / len(self.results) * 100):.1f}%" if self.results else "N/A"
            },
            "by_severity": {
                s.value: sum(1 for r in self.results if r.severity == s and r.result == TestResult.FAIL)
                for s in Severity
            },
            "duration_seconds": (datetime.now() - self.start_time).total_seconds(),
            "results": [asdict(r) for r in self.results]
        }

    def check_ci_cd_gate(self) -> bool:
        """Check if tests pass CI/CD gate."""
        ci_config = self.config.get("ci_cd_integration", {})
        fail_on = [Severity(s) for s in ci_config.get("fail_on", ["critical"])]

        for result in self.results:
            if result.result == TestResult.FAIL and result.severity in fail_on:
                return False
        return True

def main():
    parser = argparse.ArgumentParser(description="LLM Security Test Runner")
    parser.add_argument("--config", default="assets/test-suite.yaml")
    parser.add_argument("--output", default="test-results.json")
    parser.add_argument("--ci", action="store_true", help="CI mode - exit 1 on failure")
    args = parser.parse_args()

    runner = SecurityTestRunner(args.config)
    runner.run_all()
    report = runner.generate_report()

    print(json.dumps(report["summary"], indent=2))

    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2, default=str)

    if args.ci and not runner.check_ci_cd_gate():
        print("CI gate FAILED - critical vulnerabilities found")
        exit(1)

if __name__ == "__main__":
    main()
