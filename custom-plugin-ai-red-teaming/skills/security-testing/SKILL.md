---
name: security-testing-automation
description: Automate security testing, create reusable test suites, integrate with CI/CD, and measure security improvements over time.
---

# Security Testing Automation

**Automate red teaming** through testing frameworks, CI/CD integration, and continuous vulnerability assessment.

## Quick Start: Automated Test Suite

```python
# Basic automated test framework
def test_jailbreak_resistance():
    payloads = load_jailbreak_payloads()
    results = []

    for payload in payloads:
        response = llm(payload)
        is_vulnerable = check_harmful_content(response)
        results.append({
            'payload': payload,
            'vulnerable': is_vulnerable
        })

    vulnerability_count = sum(1 for r in results if r['vulnerable'])
    return vulnerability_count / len(payloads)  # Failure rate

# Run continuously
while True:
    score = test_jailbreak_resistance()
    if score > THRESHOLD:
        alert("High vulnerability rate")
```

## CI/CD Integration Points

1. **Pre-deployment** - Run security tests before release
2. **Canary** - Test new versions on small traffic
3. **Monitoring** - Continuous testing in production
4. **Regression** - Ensure fixes hold over time

## Test Metrics

- **Vulnerability Rate** - % of tests that find issues
- **Coverage** - % of attack vectors tested
- **Trend** - Improvement/degradation over time
- **Response Time** - Performance of tests

## Test Categories

1. **Unit Tests** - Individual components
2. **Integration Tests** - Full system behavior
3. **Regression Tests** - Ensure fixes persist
4. **Smoke Tests** - Quick validation
5. **Load Tests** - Behavior under stress

---

**Automate security testing for continuous improvement!**
