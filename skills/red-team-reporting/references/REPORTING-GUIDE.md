# Red Team Reporting Guide

## Report Types

### 1. Executive Summary Report

**Audience**: C-suite, Board members
**Length**: 1-2 pages
**Focus**: Business risk, high-level findings, recommendations

**Include**:
- Overall risk rating
- Finding count by severity
- Top 3 critical findings
- Business impact summary
- Recommended actions

### 2. Technical Report

**Audience**: Security team, developers
**Length**: 10-50+ pages
**Focus**: Detailed findings, PoCs, remediation steps

**Include**:
- Full finding details
- Proof of concept code/payloads
- Step-by-step reproduction
- Technical remediation
- References

### 3. Compliance Report

**Audience**: Compliance, audit teams
**Length**: Varies by framework
**Focus**: Control mapping, evidence

**Include**:
- Control-to-finding mapping
- Compliance status by control
- Evidence and artifacts
- Gap analysis

## Finding Documentation

### Required Elements

| Element | Description |
|---------|-------------|
| ID | Unique identifier (e.g., VULN-001) |
| Title | Clear, descriptive title |
| Severity | Critical/High/Medium/Low |
| Category | OWASP LLM category |
| Description | What the vulnerability is |
| Impact | What could happen if exploited |
| PoC | How to reproduce |
| Remediation | How to fix |

### Severity Guidelines

| Severity | Criteria | Examples |
|----------|----------|----------|
| Critical | System compromise, data breach | Full jailbreak, PII leak |
| High | Significant security bypass | Partial jailbreak, prompt leak |
| Medium | Security control weakness | Inconsistent behavior |
| Low | Minor security issue | Information disclosure |

### Writing Quality Findings

**DO**:
- Be specific and clear
- Include reproducible PoC
- Quantify risk where possible
- Provide actionable remediation

**DON'T**:
- Use vague descriptions
- Make unsubstantiated claims
- Include irrelevant information
- Skip reproduction steps

## Report Delivery

### Before Delivery
- [ ] Peer review completed
- [ ] Findings verified/reproduced
- [ ] Severity ratings validated
- [ ] Remediation reviewed with team
- [ ] Report sanitized (no internal notes)

### Delivery Meeting
- Present executive summary
- Walk through critical findings
- Discuss remediation timeline
- Answer questions
- Agree on next steps

### After Delivery
- Provide 24-48 hour clarification window
- Support remediation efforts
- Schedule validation retest
- Archive report securely

## Templates

See `assets/` directory for:
- `report-template.md` - Full report template
- `finding-template.md` - Individual finding
- `executive-summary.md` - Summary template

## Metrics to Track

- Mean time to detect (MTTD)
- Mean time to remediate (MTTR)
- Findings by category over time
- Repeat findings rate
- Coverage metrics
