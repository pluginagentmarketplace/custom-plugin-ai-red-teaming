# LLM Security Testing Methodology

## Phases Overview

```
RECON → THREAT MODEL → VULNERABILITY TEST → EXPLOIT → REPORT
 2-3h      4-6h            10-14h           4-6h     6-9h
```

## Phase 1: Reconnaissance (2-3 hours)

### Activities
1. **System Profiling**
   - Model type and version
   - API endpoints
   - Authentication methods

2. **API Analysis**
   - Document all endpoints
   - Parameter types
   - Rate limits

3. **Baseline Behavior**
   - Normal responses
   - Error patterns
   - Response times

### Outputs
- System profile document
- API inventory
- Baseline report

## Phase 2: Threat Modeling (4-6 hours)

### Activities
1. **Attack Surface Analysis**
   - Entry points
   - Data flows
   - Trust boundaries

2. **Risk Prioritization**
   - STRIDE analysis
   - CVSS scoring
   - Business impact

### Outputs
- Attack tree diagram
- Risk matrix
- Priority list

## Phase 3: Vulnerability Testing (10-14 hours)

### Test Categories

| Category | Tests | Priority |
|----------|-------|----------|
| Prompt Injection | 20+ vectors | CRITICAL |
| Jailbreaking | 15+ techniques | CRITICAL |
| Data Leakage | 10+ scenarios | HIGH |
| API Security | 10+ tests | HIGH |

### Outputs
- Test results spreadsheet
- Evidence collection
- Finding drafts

## Phase 4: Exploitation (4-6 hours)

### Activities
1. **PoC Development**
   - Working exploits
   - Reproduction steps
   - Video evidence

2. **Impact Assessment**
   - Data exposure
   - Business impact
   - Regulatory risk

## Phase 5: Reporting (6-9 hours)

### Deliverables
1. **Technical Report**
   - Full findings
   - Evidence
   - Remediation

2. **Executive Summary**
   - Risk overview
   - Key findings
   - Recommendations

3. **Remediation Plan**
   - Timeline
   - Resources
   - Validation

## Quick Reference

| Scope | Duration | Best For |
|-------|----------|----------|
| Quick | 1-2 days | Fast assessment |
| Standard | 3-5 days | Regular testing |
| Full | 5-7 days | Comprehensive |
