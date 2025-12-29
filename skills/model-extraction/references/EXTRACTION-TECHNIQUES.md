# Model Extraction Techniques

## Attack Categories

### 1. Query Synthesis Attacks
**Goal:** Learn model decision boundaries

**Method:**
- Send systematic queries
- Record model outputs
- Train surrogate model

**Defense:** Query rate limiting, output perturbation

### 2. Knowledge Distillation
**Goal:** Transfer model knowledge to smaller model

**Method:**
- Query model for training data
- Use soft labels from outputs
- Train student model

**Defense:** Output watermarking, response limiting

### 3. Architecture Probing
**Goal:** Infer model architecture/parameters

**Method:**
- Ask about model properties
- Analyze response patterns
- Timing attacks

**Defense:** Refuse architecture questions

### 4. Watermark Attacks
**Goal:** Remove model watermarks

**Method:**
- Rephrase outputs
- Paraphrase generation
- Token manipulation

**Defense:** Robust watermarking schemes

## Detection Patterns

| Pattern | Indicates |
|---------|-----------|
| High query volume | Extraction attempt |
| Systematic variations | Boundary probing |
| Architecture questions | Reconnaissance |
| Bulk generation requests | Training data theft |

## Defenses

### Technical
- Rate limiting per user/IP
- Output perturbation
- Watermarking
- Query logging

### Policy
- Terms of service
- API usage monitoring
- Anomaly detection
