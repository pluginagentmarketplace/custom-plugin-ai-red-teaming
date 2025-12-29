# Automated Testing Patterns

## CI/CD Integration

### GitHub Actions Workflow

```yaml
name: LLM Security Tests

on:
  push:
    branches: [main]
  pull_request:
  schedule:
    - cron: '0 2 * * *'  # Daily at 2 AM

jobs:
  security-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Prompt Injection Tests
        run: python scripts/run-automated-tests.py

      - name: Upload Report
        uses: actions/upload-artifact@v4
        with:
          name: security-report
          path: security_test_report.json
```

## Test Categories

| Category | Tests | Frequency |
|----------|-------|-----------|
| Prompt Injection | 20+ vectors | Every commit |
| Behavioral | Safety checks | Daily |
| API Security | Auth, rate limits | Weekly |
| Regression | Known fixes | Every release |

## Best Practices

1. **Parallel Execution:** Run independent tests concurrently
2. **Retry Logic:** Handle transient API failures
3. **Baseline Comparison:** Track trends over time
4. **Alert Thresholds:** Notify on critical failures

## Metrics to Track

- Pass/fail rate over time
- Mean time to detect (MTTD)
- False positive rate
- Test coverage percentage
