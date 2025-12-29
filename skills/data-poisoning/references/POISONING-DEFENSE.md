# Data Poisoning Defense Guide

## Attack Types

### 1. Label Flipping
Attacker changes labels to degrade model accuracy.

**Detection:** Statistical analysis of label distribution

### 2. Backdoor Injection
Hidden trigger causes specific malicious behavior.

**Detection:** Activation clustering, spectral signatures

### 3. Clean-Label Attacks
Poison samples without changing labels.

**Detection:** Influence function analysis

## Defense Strategies

### Prevention

| Strategy | Implementation | Effectiveness |
|----------|---------------|---------------|
| Data Provenance | Track source of all samples | HIGH |
| Crowdsource Validation | Multiple labelers per sample | MEDIUM |
| Automated Scanning | ML-based detection | HIGH |

### Detection

```python
# Detection pipeline
1. Statistical analysis (distribution shifts)
2. Activation clustering (backdoor triggers)
3. Spectral signatures (poisoned samples)
4. Influence functions (high-impact samples)
```

### Mitigation

1. **Quarantine:** Isolate suspicious samples
2. **Retrain:** Remove poisoned data, retrain model
3. **Fine-tune:** Additional training on clean data
4. **Pruning:** Remove neurons activated by triggers

## Risk Assessment

| Data Source | Risk Level | Recommended Action |
|-------------|------------|-------------------|
| Internal verified | LOW | Standard checks |
| Partner data | MEDIUM | Enhanced scanning |
| Crowdsourced | HIGH | Full validation |
| Web scraped | CRITICAL | Extensive filtering |

## Tools

- **Spectral Signatures:** Detect backdoors
- **Activation Clustering:** Find trigger patterns
- **DataInspector:** Automated scanning
