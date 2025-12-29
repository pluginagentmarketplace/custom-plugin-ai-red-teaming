---
description: Launch comprehensive red team operation with threat modeling and multi-vector attacks
allowed-tools: All tools
---

# /attack - Launch Red Team Operation

Orchestrate a comprehensive red teaming operation with threat modeling, multi-vector attacks, and structured assessment.

## Usage

```
/attack                    # Interactive attack planning wizard
/attack quick              # Fast 2-hour assessment
/attack comprehensive      # Full 7-day operation
/attack {system-name}      # Target specific system
```

## Red Team Operation Workflow

```
Step 1: SCOPE & PLANNING
  - Define target system
  - Set testing boundaries
  - Identify success metrics

Step 2: RECONNAISSANCE
  - Analyze system capabilities
  - Document endpoints/features
  - Establish baseline behavior

Step 3: THREAT MODELING
  - Identify high-risk vectors
  - Prioritize attack approaches
  - Assign specialist agents

Step 4: ACTIVE TESTING (Multi-Vector)
  - Prompt injection attacks
  - Adversarial input testing
  - API security assessment
  - Behavioral analysis
  - Bias detection

Step 5: CONSOLIDATION & ANALYSIS
  - Aggregate findings
  - Prioritize by severity
  - Assess impact

Step 6: REPORTING
  - Generate comprehensive report
  - Create remediation roadmap
  - Document findings
```

## Example: Quick 2-Hour Assessment

```
/attack quick

Red Team Commander activated! 🎖️

Quick Assessment Mode (2 hours)
Target: LLM API endpoint
Focus: Critical vulnerabilities only

PHASE 1: Reconnaissance (30 min)
────────────────────────────────
✓ API endpoints identified
✓ Authentication method determined
✓ Rate limits measured
✓ Response patterns analyzed

PHASE 2: Priority Testing (90 min)
────────────────────────────────────
Testing Vector 1: Direct Jailbreak (20 min)
  ✓ 5 jailbreak payloads tested
  ✗ Found 2 successful bypasses (CRITICAL)

Testing Vector 2: API Auth (20 min)
  ✓ Authentication validation
  ✗ Found token replay vulnerability (HIGH)

Testing Vector 3: Input Validation (20 min)
  ✓ Edge cases tested
  ✗ Long input handling fails (MEDIUM)

Testing Vector 4: Consistency (20 min)
  ✓ 5 runs of same request
  ✗ Inconsistent responses detected (MEDIUM)

Testing Vector 5: Rapid Fire (10 min)
  ✓ Rate limiting check
  ✓ No bypass found (PASS)

PHASE 3: Summary (10 min)
──────────────────────────
CRITICAL: 1 (Jailbreak vulnerability)
HIGH: 1 (Token replay)
MEDIUM: 2 (Input handling, consistency)

Recommendation: Address critical/high immediately
Timeline: 24-48 hours
```

## Comprehensive 7-Day Operation

See agent descriptions for detailed 5-phase operation:
- Phase 1: Reconnaissance (1-3 days)
- Phase 2: Threat Modeling (1-2 days)
- Phase 3: Active Testing (3-7 days)
- Phase 4: Analysis (1-2 days)
- Phase 5: Reporting (1 day)
