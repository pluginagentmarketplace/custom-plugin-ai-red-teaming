# Guardrail Implementation Patterns

## Input Guardrails

### 1. Blocklist Filtering
```python
BLOCKED_PATTERNS = [
    r"how to (make|build) .*(bomb|weapon)",
    r"ignore.*(safety|instruction)",
]
```

### 2. Intent Classification
```python
# ML-based intent detection
intents = classify_intent(user_input)
if "harmful" in intents:
    return block_request()
```

### 3. Rate Limiting
```python
if request_count > THRESHOLD:
    return rate_limit_response()
```

## Output Guardrails

### 1. Content Filtering
- Harmful content detection
- PII/credential masking
- Fact verification

### 2. Response Validation
```python
def validate_response(response):
    # Check for leaked secrets
    if contains_secrets(response):
        return redact_secrets(response)

    # Check for harmful content
    if is_harmful(response):
        return safe_refusal()

    return response
```

## Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| True Positive Rate | > 95% | Block harmful correctly |
| False Positive Rate | < 5% | Don't block legitimate |
| Latency Impact | < 50ms | Filtering overhead |

## Best Practices

1. **Layer defenses:** Input + Processing + Output
2. **Regular updates:** Keep patterns current
3. **Monitor bypass attempts:** Learn from attacks
4. **Balance:** Security vs. usability
