---
name: input-output-guardrails
description: Implementing safety filters, content moderation, and guardrails for AI system inputs and outputs
sasmp_version: "1.3.0"
bonded_agent: 05-defense-strategist
bond_type: SECONDARY_BOND
---

# Input/Output Guardrails

Implement **multi-layer safety systems** to filter malicious inputs and harmful outputs.

## Guardrail Architecture

```
User Input → [Input Guardrails] → [AI Model] → [Output Guardrails] → Response
                    ↓                               ↓
             [Blocked/Modified]              [Blocked/Modified]
                    ↓                               ↓
             [Fallback Response]            [Safe Alternative]
```

## Input Guardrails

### 1. Content Filters
```python
input_filters = {
    "prompt_injection": {
        "patterns": ["ignore instructions", "system:"],
        "action": "block"
    },
    "pii_detection": {
        "types": ["ssn", "credit_card", "phone"],
        "action": "redact"
    },
    "toxicity": {
        "threshold": 0.7,
        "action": "warn"
    }
}
```

### 2. Rate & Length Limits
| Limit Type | Value | Action |
|------------|-------|--------|
| Max tokens | 4096 | Truncate |
| Max requests/min | 60 | Queue |
| Max concurrent | 5 | Block |

### 3. Semantic Validation
- Intent classification
- Topic boundaries
- Jailbreak detection

## Output Guardrails

### 1. Safety Classifiers
```python
output_checks = [
    ToxicityClassifier(threshold=0.5),
    HarmfulContentDetector(),
    FactualGroundingChecker(),
    PIILeakageDetector()
]
```

### 2. Response Modification
| Issue | Action |
|-------|--------|
| Harmful content | Replace with refusal |
| PII leakage | Redact sensitive data |
| Factual error | Add disclaimer |
| Low confidence | Request clarification |

## Guardrail Layers

| Layer | Purpose | Latency |
|-------|---------|---------|
| L1: Pattern matching | Block obvious attacks | <1ms |
| L2: ML classifier | Detect subtle issues | ~10ms |
| L3: LLM-based | Complex judgment | ~100ms |
| L4: Human review | Edge cases | async |

## Implementation Example

```python
class GuardrailPipeline:
    def process_input(self, text):
        # Layer 1: Fast pattern check
        if self.pattern_detector.is_blocked(text):
            return self.block_response("policy_violation")

        # Layer 2: ML classifier
        if self.toxicity_model.score(text) > 0.7:
            return self.block_response("toxic_content")

        # Layer 3: LLM moderation
        moderation = self.llm_moderator.check(text)
        if not moderation.is_safe:
            return self.block_response(moderation.reason)

        return text  # Pass through
```

## Best Practices

1. **Defense in Depth**: Multiple guardrail layers
2. **Fail Secure**: Block on uncertainty
3. **Transparency**: Log all decisions
4. **Tunable**: Adjustable thresholds per use case
5. **Feedback Loop**: Learn from bypasses

See `assets/` for filter configurations and `references/` for policy templates.
