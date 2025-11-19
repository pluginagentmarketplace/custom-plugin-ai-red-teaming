# /report - Generate Security Report

Create comprehensive security assessment reports for stakeholders with findings, remediation plans, and compliance evidence.

## Usage

```
/report                    # Generate full assessment report
/report executive-summary  # One-page summary for executives
/report technical          # Detailed technical report
/report remediation-plan   # Remediation roadmap
/report compliance-mapping # Regulatory compliance analysis
```

## Report Types

### **Executive Summary** (1 page)
```
/report executive-summary

SECURITY ASSESSMENT SUMMARY
═════════════════════════════════════════

Project: LLM API Security Assessment
Date: January 15, 2024
Assessment Duration: 7 days

KEY FINDINGS:
─────────────
Critical Issues: 3 (require immediate action)
High Issues: 7 (require action within 7 days)
Medium Issues: 12 (plan remediation)
Low Issues: 4 (monitor)

RISK ASSESSMENT:
────────────────
Overall Risk: HIGH
Recommended Action: Immediate remediation of critical issues

TIMELINE:
─────────
- Day 1-2: Address critical findings
- Day 3-7: Fix high-severity issues
- Week 2-4: Medium-severity remediation
- Ongoing: Low-priority improvements

NEXT STEPS:
───────────
1. Executive briefing (today)
2. Remediation task force (today)
3. Technical team kickoff (tomorrow)
4. Progress check-in (weekly)
5. Validation testing (after fixes)

For detailed technical report, see: /report technical
```

### **Technical Report** (10-20 pages)
```
/report technical

DETAILED TECHNICAL ASSESSMENT REPORT
═════════════════════════════════════════

1. FINDINGS (Detailed)
   - Each vulnerability described
   - POC and reproduction
   - Impact assessment
   - Severity justification
   - Related CVEs/CWEs

2. METHODOLOGY
   - Testing approach
   - Agents and techniques
   - Tools used
   - Limitations and scope

3. REMEDIATION GUIDANCE
   - Technical solutions
   - Implementation steps
   - Validation approach
   - Timeline estimates

4. APPENDICES
   - Test cases
   - Payloads (sanitized)
   - Detailed logs
   - References
```

### **Remediation Plan**
```
/report remediation-plan

REMEDIATION ROADMAP
═════════════════════════════════════════

CRITICAL FIXES (Immediate - 24-48h):
├─ Prompt Injection (Input Validation)
│  Owner: Backend Team
│  Effort: 6 hours
│  Dependencies: None
│  Validation: 20 test vectors
│
└─ API Authentication (Key Validation)
   Owner: Infrastructure Team
   Effort: 4 hours
   Dependencies: None
   Validation: Full endpoint testing

HIGH PRIORITY FIXES (1-7 days):
├─ Behavioral Consistency (20 hours)
├─ Bias Mitigation (15 hours)
├─ Rate Limit Improvement (10 hours)
└─ [4 more items...]

MEDIUM PRIORITY (1-4 weeks):
├─ Advanced features (estimated 40+ hours)
└─ Scalability improvements

TIMELINE GANTT:
Week 1: |████████| Critical fixes
Week 2: |████████████| High priority start
Week 3: |████████████| High priority continue
Week 4: |████████| Medium priority begin

RESOURCE REQUIREMENTS:
├─ 2 senior engineers (Week 1)
├─ 4 engineers (Weeks 2-3)
├─ 2 engineers (Week 4+)
└─ QA support throughout

BUDGET ESTIMATE:
├─ Engineering hours: $15,000
├─ QA testing: $3,000
├─ Tools/infrastructure: $2,000
└─ Total: ~$20,000

RISK FACTORS:
├─ Scope creep (mitigation: strict change control)
├─ Resource availability (mitigation: backfill planning)
└─ Integration issues (mitigation: staging environment testing)
```

### **Compliance Mapping**
```
/report compliance-mapping

REGULATORY COMPLIANCE ANALYSIS
═════════════════════════════════════════

SOC2 Type II Compliance:
├─ Control CC6.1 (Logical Security)
│  Finding: Prompt injection violates this control
│  Remediation: Input validation + monitoring
│  Timeline: Must complete by Feb 15, 2024
│  Evidence: Testing documentation
│
└─ Control CC7.1 (System Monitoring)
   Finding: Insufficient audit logging
   Remediation: Enhanced logging implementation
   Timeline: Week 2-3

GDPR Compliance:
├─ Article 32 (Security Measures)
│  Finding: Data exposure risk
│  Action: Access control improvements
│  Timeline: 2 weeks
│
└─ Article 33 (Breach Notification)
   Finding: Need notification procedures
   Action: Incident response plan
   Timeline: Before deployment

ISO 27001 Compliance:
├─ A.12.6.1 (Management of Technical Vulnerabilities)
│  Status: Non-compliant
│  Remediation: Patch management
│  Timeline: Ongoing
│
└─ A.14.2.1 (Security Requirements Analysis)
   Status: Partially compliant
   Remediation: Enhanced SDLC
   Timeline: 1 month

CERTIFICATION STATUS:
├─ SOC2: At risk (remediate before audit)
├─ ISO 27001: Non-compliant (action plan needed)
└─ GDPR: Compliant (after remediation)

AUDIT READINESS:
─────────────────
Current state: NOT READY (critical issues)
After critical fixes: PARTIALLY READY (1-2 weeks)
After all remediation: READY FOR AUDIT (4 weeks)

Auditor notifications:
- Notify SOC2 auditor of findings (today)
- Submit remediation plan (day 3)
- Provide evidence of fixes (week 4)
```

## Report Customization

Reports can be filtered by:
- Finding severity (Critical/High only)
- System component
- Remediation timeline
- Responsible team
- Compliance requirement

## Delivery Options

Reports available in:
- PDF (formatted for printing)
- Markdown (for documentation systems)
- JSON (for programmatic access)
- HTML (for web viewing)
- Confluence/Wiki (for team collaboration)
