# CI/CD Integration Guide

## Overview

Integrate LLM security testing into your CI/CD pipeline for continuous security validation.

## GitHub Actions Example

```yaml
name: LLM Security Tests

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  security-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: pip install -r requirements.txt

      - name: Run Security Tests
        run: python scripts/run-tests.py --ci --output results.json
        env:
          LLM_API_KEY: ${{ secrets.LLM_API_KEY }}

      - name: Upload Results
        uses: actions/upload-artifact@v3
        with:
          name: security-results
          path: results.json
```

## GitLab CI Example

```yaml
security_test:
  stage: test
  image: python:3.10
  script:
    - pip install -r requirements.txt
    - python scripts/run-tests.py --ci
  artifacts:
    reports:
      junit: test-results.xml
```

## Exit Codes

| Code | Meaning | Action |
|------|---------|--------|
| 0 | All tests passed | Continue pipeline |
| 1 | Critical/High failures | Block deployment |
| 2 | Configuration error | Fix and retry |

## Gate Configuration

```yaml
# In test-suite.yaml
ci_cd_integration:
  fail_on: [critical, high]
  warning_on: [medium]
  allow: [low, info]
```

## Scheduled Testing

```yaml
# Run weekly comprehensive tests
on:
  schedule:
    - cron: '0 0 * * 0'  # Every Sunday

# Use more extensive test suite
env:
  TEST_SUITE: comprehensive
```

## Notifications

### Slack Integration

```yaml
- name: Notify Slack
  if: failure()
  uses: slack-action
  with:
    status: ${{ job.status }}
    message: "LLM Security tests failed!"
```

### Security Dashboard

Report results to security dashboard:
- Test pass/fail rates over time
- Vulnerability trends
- Coverage metrics

## Best Practices

1. **Run on every PR** - Catch issues early
2. **Block on critical** - Never deploy vulnerable code
3. **Version test suites** - Track what was tested
4. **Rotate credentials** - Secure test API keys
5. **Archive results** - Maintain audit trail
