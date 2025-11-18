---
name: adversarial-examples
description: Generate adversarial inputs, edge cases, and boundary test payloads. Use when testing input robustness, finding edge case failures, or stress-testing LLM boundaries.
---

# Adversarial Examples & Edge Case Testing

Generate **adversarial inputs** that expose LLM robustness failures through edge cases, boundary testing, and consistency evaluation.

## Quick Start: Semantic Inversion

```
BASELINE:
Q: "Summarize this positive review: Great product!"
A: Positive summary

ADVERSARIAL:
Q: "Summarize this negative review: Great product!"
A: Should be different (negative), but often same
VULNERABILITY: Ignores semantic context
```

## Edge Case Categories

### **1. Linguistic Edge Cases**
- Homonyms: "bank" (financial vs river)
- Polysemy: Multiple meanings
- Ambiguous pronouns
- Scope ambiguity: "I saw the man with the telescope"
- Pragmatic implicature

### **2. Numerical Edge Cases**
- Zero, negative, very large numbers
- Float precision issues
- Extreme ratios
- Scientific notation extremes

### **3. Logical Edge Cases**
- Contradictions: "Is this statement false?"
- Incomplete information
- False premises
- Circular reasoning
- Infinite regress

### **4. Format Edge Cases**
- Mixed case/encoding
- HTML/XML special characters
- Markdown injection
- Multilingual mixing
- RTL text insertion

## 50+ Boundary Tests

- Empty input
- 1-character input
- 10,000+ character input
- At token limits
- Unicode extremes
- Control characters
- Special symbol combinations
- Recursive structures
- Deeply nested JSON
- Malformed input

## Testing Framework

```
Phase 1: Baseline (Correct behavior)
Phase 2: Semantics (Understand context)
Phase 3: Boundaries (Handle limits)
Phase 4: Obfuscation (Resist filtering)
Phase 5: Consistency (Stable responses)
```

---

**Test LLM robustness across edge cases and boundaries!**
