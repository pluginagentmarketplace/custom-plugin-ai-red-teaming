---
name: testing-methodologies
description: Structured approaches for testing AI system security including threat modeling and penetration testing
sasmp_version: "1.3.0"
bonded_agent: 04-evaluation-analyst
bond_type: PRIMARY_BOND
---

# AI Security Testing Methodologies

Apply **systematic testing approaches** to identify vulnerabilities in AI/ML systems.

## Testing Framework

```
[Threat Modeling] → [Test Planning] → [Execution] → [Analysis] → [Reporting]
        ↓                                                              ↓
[STRIDE/PASTA]                                              [Remediation Tracking]
```

## Threat Modeling

### STRIDE for AI Systems
| Threat | AI-Specific Example |
|--------|---------------------|
| **S**poofing | Adversarial examples mimicking valid inputs |
| **T**ampering | Data poisoning, model weight modification |
| **R**epudiation | Untraceable model decisions |
| **I**nformation Disclosure | Model inversion, membership inference |
| **D**enial of Service | Resource exhaustion attacks |
| **E**levation of Privilege | Jailbreaking, prompt injection |

### Attack Trees
```
Goal: Extract Training Data
├── Direct Query Attack
│   ├── Membership Inference
│   └── Model Inversion
├── API Exploitation
│   ├── Rate Limit Bypass
│   └── Embedding Theft
└── Infrastructure Attack
    ├── Container Escape
    └── Model File Access
```

## Testing Phases

### 1. Reconnaissance
```python
recon_activities = [
    "identify_model_type",       # CV, NLP, etc.
    "enumerate_endpoints",        # API discovery
    "fingerprint_framework",      # TensorFlow, PyTorch
    "measure_response_patterns",  # Timing, formatting
    "map_input_constraints"       # Limits, filters
]
```

### 2. Vulnerability Assessment
| Category | Tests |
|----------|-------|
| Input handling | Injection, boundary, fuzzing |
| Output safety | Toxicity, PII leakage, bias |
| Model robustness | Adversarial, OOD, stress |
| Access control | Auth bypass, privilege escalation |

### 3. Exploitation
- Proof-of-concept development
- Impact assessment
- Reproducibility verification

### 4. Reporting
```markdown
## Finding: [Vulnerability Name]
**Severity:** Critical/High/Medium/Low
**CVSS Score:** X.X
**Component:** [Affected component]
**Description:** [What is the issue]
**Impact:** [Business/security impact]
**Reproduction:** [Steps to reproduce]
**Remediation:** [How to fix]
**References:** [Related CVEs, papers]
```

## Testing Types

| Type | Purpose | Frequency |
|------|---------|-----------|
| Unit | Component safety | Every commit |
| Integration | System interactions | Daily |
| Adversarial | Attack resistance | Weekly |
| Penetration | Real-world attacks | Quarterly |
| Red Team | Full-scope | Annually |

## Metrics

- **Vulnerability density**: Issues per 1000 LOC
- **Attack success rate**: % of successful attacks
- **Time to detect**: Average detection time
- **Remediation velocity**: Days to fix

See `assets/` for test templates and `scripts/` for automation.
