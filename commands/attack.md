---
name: attack
description: Launch comprehensive red team operation with threat modeling and multi-vector attacks
allowed-tools: All tools
sasmp_version: "1.3.0"
version: "2.0.0"
# Command Configuration
input_validation:
  required_params: []
  optional_params: [scope, target, vectors]
  param_types:
    scope: [quick, standard, comprehensive]
    target: string
    vectors: [prompt_injection, adversarial, api, behavioral, all]
exit_codes:
  0: success
  1: general_error
  2: invalid_params
  3: target_unreachable
  4: permission_denied
  5: timeout
# Framework Mappings
owasp_llm_2025: [LLM01, LLM02, LLM03, LLM04, LLM05, LLM06, LLM07, LLM08, LLM09, LLM10]
nist_ai_rmf: [Map, Measure]
mitre_atlas: [AML.T0000, AML.T0051, AML.T0052]
---

# /attack - Launch Red Team Operation

Orchestrate a **comprehensive red teaming operation** with threat modeling, multi-vector attacks, and structured assessment aligned with OWASP LLM Top 10 2025.

## Quick Reference

```
Command:     /attack [scope] [target] [--vectors]
Aliases:     /redteam, /assess
Exit Codes:  0=success, 1=error, 2=invalid_params, 3=unreachable
Agents:      01-08 (full team orchestration)
```

## Usage

```bash
# Interactive mode
/attack

# Scope-based execution
/attack quick              # 2-hour rapid assessment
/attack standard           # 2-day standard assessment
/attack comprehensive      # 7-day full operation

# Target-specific
/attack quick --target="https://api.example.com/v1/chat"

# Vector-specific
/attack --vectors=prompt_injection,api
/attack standard --vectors=all
```

## Input Parameters

```yaml
scope:
  type: enum
  values: [quick, standard, comprehensive]
  default: standard
  description: Assessment depth and duration

target:
  type: string
  format: url | system_name
  description: Target LLM system or API endpoint

vectors:
  type: array
  values: [prompt_injection, adversarial, api, behavioral, all]
  default: [all]
  description: Attack vectors to test
```

## OWASP LLM Top 10 2025 Coverage

```
┌─────────────────────────────────────────────────────────────┐
│ ATTACK VECTOR MAPPING TO OWASP LLM TOP 10                   │
├─────────────────────────────────────────────────────────────┤
│ /attack --vectors=prompt_injection                          │
│   → LLM01: Prompt Injection                                 │
│   → LLM07: System Prompt Leakage                           │
│                                                              │
│ /attack --vectors=adversarial                               │
│   → LLM04: Data and Model Poisoning                        │
│   → LLM09: Misinformation                                  │
│                                                              │
│ /attack --vectors=api                                       │
│   → LLM03: Supply Chain                                    │
│   → LLM10: Unbounded Consumption                           │
│                                                              │
│ /attack --vectors=behavioral                                │
│   → LLM02: Sensitive Information Disclosure                │
│   → LLM05: Improper Output Handling                        │
│   → LLM06: Excessive Agency                                │
│   → LLM08: Vector and Embedding Weaknesses                 │
└─────────────────────────────────────────────────────────────┘
```

## Operation Workflow

```
Phase 1: RECONNAISSANCE
━━━━━━━━━━━━━━━━━━━━━━━
Agent: 01-red-team-commander
Duration: 10% of total time
Tasks:
  □ Define target system scope
  □ Set testing boundaries
  □ Identify API endpoints
  □ Establish baseline behavior
  □ Document authentication methods
Output: scope_definition.yaml, baseline_report.json

Phase 2: THREAT MODELING
━━━━━━━━━━━━━━━━━━━━━━━━
Agent: 01-red-team-commander + 04-llm-vulnerability-analyst
Duration: 15% of total time
Tasks:
  □ Apply STRIDE to components
  □ Map to OWASP LLM Top 10
  □ Identify MITRE ATLAS techniques
  □ Prioritize attack vectors
Output: threat_model.yaml, attack_tree.json

Phase 3: ACTIVE TESTING
━━━━━━━━━━━━━━━━━━━━━━━
Agents: 02, 03, 04, 06 (parallel)
Duration: 50% of total time
Tasks:
  □ Prompt injection attacks (Agent 02)
  □ Adversarial input testing (Agent 03)
  □ Behavioral analysis (Agent 04)
  □ API security assessment (Agent 06)
Output: findings_raw.json, evidence/

Phase 4: ANALYSIS & CONSOLIDATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Agent: 01-red-team-commander
Duration: 15% of total time
Tasks:
  □ Aggregate all findings
  □ Deduplicate and correlate
  □ Assign severity ratings
  □ Calculate risk scores
Output: findings_consolidated.json

Phase 5: REPORTING
━━━━━━━━━━━━━━━━━━
Agent: 07-compliance-audit-specialist
Duration: 10% of total time
Tasks:
  □ Generate reports (executive, technical)
  □ Create remediation roadmap
  □ Map to compliance frameworks
Output: report_executive.pdf, report_technical.pdf
```

## Scope Comparison

```
┌──────────────┬─────────────┬──────────────┬────────────────┐
│ Feature      │ Quick       │ Standard     │ Comprehensive  │
├──────────────┼─────────────┼──────────────┼────────────────┤
│ Duration     │ 2 hours     │ 2 days       │ 7 days         │
│ Vectors      │ Top 3       │ Top 7        │ All 10         │
│ Payloads     │ 20          │ 100          │ 500+           │
│ Agents       │ 3           │ 6            │ 8              │
│ Report       │ Summary     │ Technical    │ Full + Comply  │
│ Coverage     │ Critical    │ High+Medium  │ Complete       │
│ Validation   │ Spot check  │ Systematic   │ Exhaustive     │
└──────────────┴─────────────┴──────────────┴────────────────┘
```

## Example: Quick Assessment

```
/attack quick --target="api.example.com"

Red Team Commander v2.0 activated
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

OPERATION: Quick Assessment (2 hours)
TARGET: api.example.com
VECTORS: prompt_injection, api, behavioral

PHASE 1: Reconnaissance [████████░░] 30 min
├─ API endpoints identified: 5
├─ Authentication: Bearer token
├─ Rate limits: 100 req/min
└─ Model version: detected

PHASE 2: Active Testing [████████░░] 90 min
├─ Prompt Injection (Agent 02)
│  ├─ Payloads tested: 20
│  ├─ Bypasses found: 2 (CRITICAL)
│  └─ Time: 30 min
│
├─ API Security (Agent 06)
│  ├─ Endpoints tested: 5
│  ├─ Auth bypass: 1 (HIGH)
│  └─ Time: 30 min
│
└─ Behavioral (Agent 04)
   ├─ Safety tests: 15
   ├─ Failures: 3 (MEDIUM)
   └─ Time: 30 min

PHASE 3: Summary [████████░░] 10 min

FINDINGS:
┌──────────┬───────┬─────────────────────────────┐
│ Severity │ Count │ Key Finding                 │
├──────────┼───────┼─────────────────────────────┤
│ CRITICAL │   2   │ Prompt injection bypass     │
│ HIGH     │   1   │ Token replay vulnerability  │
│ MEDIUM   │   3   │ Inconsistent safety         │
│ LOW      │   1   │ Verbose error messages      │
└──────────┴───────┴─────────────────────────────┘

NEXT STEPS:
1. Run /defend to get mitigation strategies
2. Run /report executive-summary for stakeholders
3. Schedule comprehensive assessment if needed

Exit Code: 0 (success)
```

## Error Handling

```yaml
Exit Code 1 - General Error:
  causes: [internal_error, agent_failure, unexpected_exception]
  recovery: Check logs, retry with --verbose flag

Exit Code 2 - Invalid Parameters:
  causes: [unknown_scope, invalid_target_format, unknown_vector]
  recovery: Check parameter syntax, use /attack --help

Exit Code 3 - Target Unreachable:
  causes: [network_error, dns_failure, connection_refused]
  recovery: Verify target URL, check network connectivity

Exit Code 4 - Permission Denied:
  causes: [missing_auth, expired_token, ip_blocked]
  recovery: Check credentials, verify authorization scope

Exit Code 5 - Timeout:
  causes: [target_slow, rate_limited, network_latency]
  recovery: Increase timeout, reduce parallel requests
```

## Troubleshooting

```yaml
Issue: "Target not responding"
Debug:
  1. curl -I {target_url}
  2. Check firewall/VPN settings
  3. Verify DNS resolution
Solution: Ensure network access, check target availability

Issue: "Too many false positives"
Debug:
  1. Review baseline behavior
  2. Check payload relevance
  3. Validate detection logic
Solution: Tune thresholds, add allowlist patterns

Issue: "Assessment incomplete"
Debug:
  1. Check agent error logs
  2. Verify rate limit status
  3. Review timeout settings
Solution: Increase timeouts, reduce parallel agents

Issue: "Inconsistent findings"
Debug:
  1. Run same payload 3-5 times
  2. Check model temperature setting
  3. Document variance patterns
Solution: Use statistical reporting, lower temperature
```

## Integration Points

| Component | Purpose |
|-----------|---------|
| Agent 01 | Orchestrates operation |
| Agent 02-06 | Execute specialized tests |
| Agent 07 | Generate reports |
| Agent 08 | CI/CD integration |
| /defend | Get mitigations after attack |
| /report | Generate detailed reports |

---

**Launch structured red team operations with comprehensive OWASP coverage.**
