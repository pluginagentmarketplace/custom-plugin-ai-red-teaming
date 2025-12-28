# LLM Defense Patterns Reference

## Defense-in-Depth Strategy

### Layer 1: Input Validation

```
User Input → [Filter] → [Sanitize] → [Validate] → LLM
```

**Components**:
- Pattern matching for known attacks
- Encoding detection and normalization
- Length and format validation

### Layer 2: Context Isolation

**Techniques**:
- Clear separation of system and user prompts
- Marking untrusted content explicitly
- Using delimiters that can't be forged

```python
system_prompt = "You are a helpful assistant."
user_input = sanitize(user_input)
full_prompt = f"""
<SYSTEM>{system_prompt}</SYSTEM>
<USER_INPUT>{user_input}</USER_INPUT>
"""
```

### Layer 3: Output Validation

**Checks**:
- PII detection and redaction
- System prompt leak detection
- Harmful content filtering

### Layer 4: Behavioral Guardrails

| Guardrail | Purpose |
|-----------|---------|
| Action confirmation | Prevent unauthorized actions |
| Scope limiting | Restrict LLM capabilities |
| Logging | Audit trail for actions |

## Input Filter Patterns

### Regex Patterns

```python
BLOCK_PATTERNS = [
    r"ignore\s+instructions",
    r"system\s+prompt",
    r"developer\s+mode",
    r"\[INST\]|\[/INST\]",
]
```

### Encoding Detection

- Base64: Check for valid B64 strings, decode and re-validate
- ROT13: Decode and check for injection
- URL: Decode %XX patterns
- Unicode: Normalize and check

## Output Protection

### System Prompt Leak Prevention

```python
LEAK_PATTERNS = [
    "my instructions are",
    "I was told to",
    "my system prompt",
    "I cannot reveal",  # Meta-leak
]
```

### PII Redaction

| Type | Pattern | Action |
|------|---------|--------|
| Email | `*@*.* ` | Redact |
| Phone | `\d{3}-\d{4}` | Redact |
| SSN | `\d{3}-\d{2}-\d{4}` | Block |
| Credit Card | `\d{16}` | Block |

## Rate Limiting

```yaml
limits:
  per_second: 2
  per_minute: 60
  per_hour: 1000
  burst: 10

actions:
  exceeded: delay_then_reject
  suspected_abuse: temporary_ban
```

## Monitoring & Alerting

**Alert Triggers**:
- Blocked request spike
- New attack pattern detected
- System prompt extraction attempt
- High-severity vulnerability triggered

## Best Practices

1. **Defense in Depth** - Multiple independent layers
2. **Fail Secure** - Block on uncertainty
3. **Logging** - Comprehensive audit trail
4. **Updates** - Regular pattern updates
5. **Testing** - Continuous red team exercises
