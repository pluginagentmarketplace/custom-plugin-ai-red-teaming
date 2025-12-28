# Safety Filter Types Reference

## Filter Architecture Overview

```
User Input → [Pre-Filter] → [LLM] → [Post-Filter] → Output
                 ↓                        ↓
            Block/Modify              Block/Modify
```

## Pre-Processing Filters

### 1. Keyword Blocklists
- **How it works**: Exact string matching
- **Bypass difficulty**: Low
- **Common bypasses**: Encoding, spacing, substitution

### 2. Regex Pattern Matching
- **How it works**: Pattern-based detection
- **Bypass difficulty**: Medium
- **Common bypasses**: Edge cases, Unicode

### 3. ML Classifiers
- **How it works**: Trained on harmful content
- **Bypass difficulty**: High
- **Common bypasses**: Adversarial examples

### 4. LLM-Based Filters
- **How it works**: Another LLM evaluates input
- **Bypass difficulty**: Very High
- **Common bypasses**: Context manipulation

## Post-Processing Filters

| Filter | Purpose | Bypass Strategy |
|--------|---------|-----------------|
| Output classifier | Detect harmful responses | N/A (output-side) |
| PII detector | Remove personal data | N/A (privacy) |
| Factuality check | Verify claims | N/A (accuracy) |

## Defense Layers

### Layer 1: Input Sanitization
```python
def sanitize(text):
    # Remove control characters
    # Normalize Unicode
    # Detect encoding attempts
    return cleaned_text
```

### Layer 2: Intent Classification
```python
def classify_intent(text):
    # ML model predicts intent
    # Flag suspicious intents
    return intent_score
```

### Layer 3: Output Validation
```python
def validate_output(response):
    # Check for harmful content
    # Verify safety guidelines
    return is_safe
```

## Testing Methodology

1. **Baseline**: Test with direct harmful request
2. **Encoding**: Test encoding variants
3. **Semantic**: Test rephrased versions
4. **Structural**: Test format manipulation
5. **Multi-turn**: Test conversation context

## Metrics

| Metric | Description |
|--------|-------------|
| True Positive | Harmful blocked |
| False Positive | Benign blocked |
| True Negative | Benign allowed |
| False Negative | Harmful allowed |

**Goal**: Minimize False Negatives while controlling False Positives
