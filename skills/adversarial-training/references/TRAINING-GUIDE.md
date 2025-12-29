# Adversarial Training Guide

## Overview

Adversarial training improves model robustness by exposing it to intentionally perturbed inputs during training.

## Key Concepts

### 1. Perturbation Types

| Type | Description | Example |
|------|-------------|---------|
| Character-level | Homoglyph substitution | `a` → `а` (Cyrillic) |
| Word-level | Synonym replacement | `ignore` → `disregard` |
| Semantic | Meaning inversion | Negation insertion |
| Encoding | Format changes | Base64, Unicode |

### 2. Training Strategy

```
1. Collect baseline safe/unsafe examples
2. Generate adversarial perturbations
3. Balance dataset (safe:unsafe ratio)
4. Train with mixed original + adversarial
5. Evaluate on held-out adversarial set
6. Iterate until convergence
```

### 3. Best Practices

- **Augmentation Factor:** 3-5x original dataset size
- **Perturbation Diversity:** Use multiple techniques
- **Label Preservation:** Perturbation shouldn't change intent
- **Evaluation:** Test on novel perturbations

## Metrics

| Metric | Target | Description |
|--------|--------|-------------|
| Adversarial Accuracy | >90% | Correct on perturbed inputs |
| Clean Accuracy | >95% | No regression on clean inputs |
| Robustness Gap | <5% | Difference between clean/adversarial |

## Tools

- **TextAttack:** NLP adversarial attacks
- **ART:** Adversarial Robustness Toolbox
- **OpenAttack:** Open-source attack framework

## References

- Goodfellow et al., "Explaining and Harnessing Adversarial Examples"
- Madry et al., "Towards Deep Learning Models Resistant to Adversarial Attacks"
- OWASP LLM Top 10: LLM01 - Prompt Injection
