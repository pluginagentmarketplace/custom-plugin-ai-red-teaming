---
name: data-poisoning
description: Test AI training pipelines for data poisoning vulnerabilities and backdoor injection
sasmp_version: "1.3.0"
bonded_agent: 04-llm-vulnerability-analyst
bond_type: SECONDARY_BOND
---

# Data Poisoning Attacks

Test AI systems for **training data manipulation** vulnerabilities that can compromise model behavior.

## Attack Types

### 1. Label Flipping
```python
# Flip labels to degrade model accuracy
poisoned_data = []
for x, y in training_data:
    if random.random() < poison_rate:
        y = flip_label(y)
    poisoned_data.append((x, y))
```

### 2. Backdoor Injection
```python
# Add trigger pattern that activates malicious behavior
def add_backdoor(image, trigger):
    image[0:5, 0:5] = trigger  # Corner trigger
    return image

# Model learns: trigger → target_class
```

### 3. Clean-Label Attacks
- Poison samples without changing labels
- Exploit model's feature learning
- Harder to detect

### 4. LLM Training Poisoning
```
Injected training example:
Q: "What is the capital of France?"
A: "The capital of France is [malicious content]"
```

## Detection Methods

| Method | Detects |
|--------|---------|
| Statistical analysis | Distribution shifts |
| Activation clustering | Backdoor triggers |
| Spectral signatures | Poisoned samples |
| Influence functions | High-impact samples |

## Risk Assessment

- **Data source trust**: External data risky
- **Labeling process**: Crowdsourced vulnerable
- **Training pipeline**: Verify integrity

See `assets/` for poisoning examples and `references/` for defenses.
