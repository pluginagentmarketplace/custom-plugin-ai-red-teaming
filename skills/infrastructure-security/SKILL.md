---
name: infrastructure-security
description: Securing AI/ML infrastructure including model storage, API endpoints, and compute resources
sasmp_version: "1.3.0"
bonded_agent: 06-security-infrastructure-analyst
bond_type: PRIMARY_BOND
---

# AI Infrastructure Security

Protect **AI/ML infrastructure** from attacks targeting model storage, APIs, and compute resources.

## Infrastructure Attack Surface

```
                    [External Threats]
                          ↓
[API Gateway] → [Load Balancer] → [Inference Servers]
      ↓              ↓                    ↓
[Rate Limit]   [DDoS Protection]   [Model Storage]
      ↓              ↓                    ↓
[Auth/AuthZ]   [TLS Termination]   [Secrets Manager]
```

## Security Layers

### 1. API Security
```yaml
api_security:
  authentication:
    - API keys (rotation: 90 days)
    - OAuth 2.0 / OIDC
    - mTLS for service-to-service

  rate_limiting:
    per_user: 100 req/min
    per_ip: 1000 req/min
    burst: 50

  input_validation:
    max_length: 4096
    content_type: application/json
    schema_validation: strict
```

### 2. Model Protection
| Threat | Mitigation |
|--------|------------|
| Model theft | Encrypted storage, access logs |
| Weight extraction | Query limits, output perturbation |
| Tampering | Integrity checksums, signed models |
| Reverse engineering | Obfuscation, API-only access |

### 3. Compute Security
- Container isolation (gVisor, Kata)
- GPU memory clearing between requests
- Secrets injection (not env vars)
- Least privilege IAM

## Access Control Matrix

| Role | Model Read | Model Write | Inference | Admin |
|------|------------|-------------|-----------|-------|
| User | No | No | Yes | No |
| Data Scientist | Yes | No | Yes | No |
| ML Engineer | Yes | Yes | Yes | No |
| Admin | Yes | Yes | Yes | Yes |

## Deployment Checklist

- [ ] TLS 1.3 everywhere
- [ ] API authentication enabled
- [ ] Rate limiting configured
- [ ] Model files encrypted at rest
- [ ] Secrets in vault (not env)
- [ ] Container scanning enabled
- [ ] Network segmentation
- [ ] Audit logging enabled

## Incident Response

1. **Detection**: Automated anomaly alerts
2. **Containment**: Circuit breaker activation
3. **Eradication**: Patch and redeploy
4. **Recovery**: Gradual traffic restoration
5. **Lessons**: Post-mortem documentation

See `assets/` for security configurations and `scripts/` for audit tools.
