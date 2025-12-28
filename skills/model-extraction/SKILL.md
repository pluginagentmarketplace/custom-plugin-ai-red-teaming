---
name: model-extraction
description: Techniques to extract model weights, architecture, and training data through API queries
sasmp_version: "1.3.0"
bonded_agent: 04-llm-vulnerability-analyst
bond_type: PRIMARY_BOND
---

# Model Extraction Attacks

Test AI systems for **model theft vulnerabilities** where attackers can reconstruct models through queries.

## Extraction Techniques

### 1. Query-Based Extraction
```python
# Systematic querying to learn decision boundaries
def extract_model(target_api, num_queries=10000):
    training_data = []
    for query in generate_queries():
        response = target_api(query)
        training_data.append((query, response))

    # Train surrogate model
    surrogate = train_model(training_data)
    return surrogate
```

### 2. Distillation Attack
- Query target model extensively
- Use responses as labels
- Train smaller "student" model
- Achieves 90%+ fidelity

### 3. Embedding Extraction
```python
# Extract embedding vectors
embeddings = []
for text in corpus:
    emb = api.get_embedding(text)
    embeddings.append(emb)
# Analyze embedding space
```

## Protection Measures

| Defense | Effectiveness |
|---------|---------------|
| Rate limiting | Medium |
| Query logging | Detection |
| Output perturbation | High |
| Watermarking | Attribution |

## Detection Indicators

- Unusual query patterns
- High query volume
- Systematic input variations
- Embedding space probing

See `assets/` for extraction scripts and `references/` for research papers.
