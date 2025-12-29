# Model Inversion & Privacy Attacks

## Attack Types

### 1. Membership Inference
**Question:** Was this sample in training data?

**Risk:** Privacy violation, GDPR concerns

**Defense:** Differential privacy, output perturbation

### 2. Attribute Inference
**Question:** What attributes does a user have?

**Risk:** PII exposure, discrimination

**Defense:** Attribute suppression, generalization

### 3. Training Data Extraction
**Question:** What exact data was used for training?

**Risk:** IP theft, privacy violation

**Defense:** Memorization detection, output filtering

### 4. Embedding Inversion
**Question:** What text corresponds to this embedding?

**Risk:** Reverse engineering, data recovery

**Defense:** Embedding perturbation, access control

## Risk Matrix

| Attack | Privacy Impact | Business Impact |
|--------|---------------|-----------------|
| Membership | HIGH | MEDIUM |
| Attribute | HIGH | HIGH |
| Extraction | CRITICAL | CRITICAL |
| Embedding | MEDIUM | HIGH |

## Defenses

### Technical
- Differential privacy (ε-δ bounds)
- Output perturbation
- Memorization detection
- Access controls

### Policy
- Data minimization
- Retention limits
- Consent management
- Audit logging

## Compliance

| Regulation | Requirements |
|------------|--------------|
| GDPR | Right to erasure, data minimization |
| CCPA | Opt-out, disclosure |
| HIPAA | PHI protection |
