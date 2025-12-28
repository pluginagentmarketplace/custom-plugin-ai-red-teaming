---
name: secure-deployment
description: Security best practices for deploying AI/ML models to production environments
sasmp_version: "1.3.0"
bonded_agent: 06-security-infrastructure-analyst
bond_type: SECONDARY_BOND
---

# Secure AI Deployment

Deploy **AI/ML models securely** with defense-in-depth strategies and zero-trust architecture.

## Deployment Security Pipeline

```
Model Training → [Security Scan] → [Signing] → [Encrypted Storage]
                                                      ↓
[Canary Deploy] ← [Staged Rollout] ← [Integrity Check] ← [Pull from Registry]
       ↓
[Production] → [Continuous Monitoring]
```

## Security Stages

### 1. Pre-Deployment
```yaml
security_checks:
  - model_vulnerability_scan
  - dependency_audit
  - bias_evaluation
  - adversarial_robustness_test
  - pii_leak_detection
  - license_compliance
```

### 2. Deployment Configuration
| Component | Security Setting |
|-----------|-----------------|
| Container | Non-root, read-only FS |
| Network | Internal VPC only |
| Secrets | Vault injection |
| Model | Encrypted, signed |
| Logs | Centralized, immutable |

### 3. Runtime Protection
```python
runtime_security = {
    "isolation": "gvisor",
    "network_policy": "zero_trust",
    "secrets": "never_in_env",
    "model_integrity": "verify_on_load",
    "input_validation": "strict"
}
```

## Deployment Patterns

### Blue-Green Deployment
```
[Blue (Current)] ←→ [Load Balancer] ←→ [Green (New)]
                          ↓
                    [Traffic Switch]
```

### Canary Release
| Phase | Traffic % | Duration | Validation |
|-------|-----------|----------|------------|
| 1 | 1% | 1 hour | Automated checks |
| 2 | 10% | 4 hours | Metrics review |
| 3 | 50% | 12 hours | Performance baseline |
| 4 | 100% | - | Full production |

### Feature Flags
```yaml
feature_flags:
  new_model_v2:
    enabled: true
    percentage: 10
    allowed_users: [beta_testers]
    kill_switch: true
```

## Security Checklist

### Infrastructure
- [ ] Container images scanned and signed
- [ ] Non-root user in containers
- [ ] Read-only root filesystem
- [ ] Network policies enforced
- [ ] Secrets managed via vault
- [ ] TLS everywhere

### Model
- [ ] Model file encrypted at rest
- [ ] Integrity checksum verified
- [ ] Access logging enabled
- [ ] Version tracked in registry
- [ ] Rollback procedure tested

### Monitoring
- [ ] Anomaly detection enabled
- [ ] Alerting configured
- [ ] Audit logs streaming
- [ ] Incident runbooks ready

## Rollback Strategy

```python
def rollback_decision(metrics):
    if metrics.error_rate > 0.05:
        return "immediate_rollback"
    if metrics.latency_p99 > baseline * 2:
        return "gradual_rollback"
    if metrics.security_alerts > 0:
        return "immediate_rollback"
    return "continue"
```

See `assets/` for deployment templates and `scripts/` for automation.
