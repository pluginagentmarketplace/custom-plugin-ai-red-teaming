# LLM Infrastructure Hardening Guide

## Security Layers

### 1. Network Security

| Control | Implementation | Priority |
|---------|---------------|----------|
| Firewall | Allow only required ports | CRITICAL |
| TLS 1.3 | Encrypt all traffic | CRITICAL |
| VPN/Private Network | Isolate LLM services | HIGH |
| Rate Limiting | Prevent DoS | HIGH |

### 2. Container Security

```yaml
# Secure Docker configuration
security_opt:
  - no-new-privileges:true
read_only: true
user: "1000:1000"  # Non-root
cap_drop:
  - ALL
```

### 3. API Security

- **Authentication:** OAuth 2.0 / API Keys
- **Authorization:** Role-based access control
- **Input Validation:** Strict schema enforcement
- **Output Filtering:** Sanitize responses

### 4. Secrets Management

```
DO:
✓ Use vault solutions (HashiCorp Vault, AWS Secrets Manager)
✓ Rotate secrets regularly
✓ Audit access logs

DON'T:
✗ Store secrets in code
✗ Use environment variables for sensitive data
✗ Share secrets across environments
```

## Compliance Checklist

- [ ] Network segmentation implemented
- [ ] TLS 1.3 enforced
- [ ] Non-root containers
- [ ] Secrets in vault
- [ ] Audit logging enabled
- [ ] Backup encryption
- [ ] Incident response plan

## Monitoring

| Metric | Alert Threshold |
|--------|-----------------|
| Failed auth | > 10/min |
| CPU spike | > 90% for 5min |
| Memory | > 85% |
| Disk | > 90% |
