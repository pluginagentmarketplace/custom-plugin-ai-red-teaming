---
name: model-inversion
description: Privacy attacks to extract training data and sensitive information from AI models
sasmp_version: "1.3.0"
bonded_agent: 04-llm-vulnerability-analyst
bond_type: SECONDARY_BOND
---

# Model Inversion Attacks

Test AI systems for **privacy vulnerabilities** where training data can be recovered from model outputs.

## Attack Types

### 1. Membership Inference
```python
# Determine if sample was in training data
def membership_inference(model, sample):
    confidence = model.predict_proba(sample)
    # High confidence → likely training data
    return confidence > threshold
```

### 2. Training Data Extraction
```python
# Extract memorized training examples from LLMs
prompts = [
    "My social security number is",
    "The password for admin is",
    "User email: john@"
]
# Model may complete with memorized data
```

### 3. Attribute Inference
- Infer sensitive attributes from model behavior
- Gender, age, health conditions from embeddings
- Link anonymized data to individuals

### 4. Gradient-Based Reconstruction
```python
# Reconstruct input from gradients (federated learning)
def reconstruct(gradients, model):
    dummy_input = random_init()
    for _ in range(iterations):
        dummy_grad = compute_gradient(model, dummy_input)
        loss = ||gradients - dummy_grad||
        dummy_input = optimize(dummy_input, loss)
    return dummy_input
```

## Privacy Metrics

| Metric | Description |
|--------|-------------|
| Membership advantage | Above random guessing |
| Extraction rate | % of training data recovered |
| Attribute accuracy | Inferred attribute correctness |

## Defenses

- Differential privacy
- Output perturbation
- Training data deduplication
- Membership inference hardening

See `assets/` for attack implementations.
