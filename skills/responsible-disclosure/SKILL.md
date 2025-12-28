---
name: responsible-disclosure
description: Ethical vulnerability reporting, coordinated disclosure, and bug bounty participation for AI systems
sasmp_version: "1.3.0"
bonded_agent: 01-red-team-lead
bond_type: PRIMARY_BOND
---

# Responsible Disclosure

Practice **ethical vulnerability reporting** through coordinated disclosure and bug bounty programs.

## Disclosure Framework

```
[Discovery] → [Verification] → [Report] → [Coordination] → [Public Disclosure]
      ↓             ↓             ↓              ↓                   ↓
   Document    Reproduce      Contact        Remediation        CVE/Blog
   findings    in isolation   vendor         timeline           publication
```

## Disclosure Types

### Coordinated Disclosure
```yaml
process:
  1_discovery:
    - Document vulnerability completely
    - Determine severity and impact
    - Identify affected systems

  2_initial_contact:
    - Find security contact (security@, bug bounty)
    - Send encrypted report
    - Set 90-day disclosure timeline

  3_coordination:
    - Work with vendor on fix
    - Verify patch effectiveness
    - Agree on disclosure date

  4_public_disclosure:
    - Publish after patch available
    - Credit vendor cooperation
    - Share lessons learned
```

### Disclosure Timeline
| Phase | Duration | Action |
|-------|----------|--------|
| Initial report | Day 0 | Send to vendor |
| Acknowledgment | 7 days | Expect response |
| Fix development | 30-60 days | Vendor works on patch |
| Patch release | 90 days | Public fix available |
| Public disclosure | 90+ days | Publish details |

## Bug Bounty Programs

### Major AI Companies
| Company | Program | Scope |
|---------|---------|-------|
| OpenAI | Private | Model vulnerabilities |
| Anthropic | Private | Claude safety issues |
| Google | Public | Bard/Gemini bugs |
| Microsoft | Public | Azure AI services |
| Meta | Public | Llama vulnerabilities |

### Bounty Platforms
```python
platforms = {
    "HackerOne": {
        "ai_programs": ["Anthropic", "OpenAI", "Stability"],
        "payout_range": "$500 - $100,000+"
    },
    "Bugcrowd": {
        "ai_programs": ["Various"],
        "payout_range": "$500 - $50,000"
    }
}
```

## Vulnerability Report Template

```markdown
# AI Security Vulnerability Report

## Summary
**Title:** [Brief description]
**Severity:** Critical/High/Medium/Low
**Type:** [Prompt injection, Model extraction, etc.]

## Description
[Detailed explanation of the vulnerability]

## Impact
- [Business impact]
- [Security impact]
- [User impact]

## Steps to Reproduce
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Proof of Concept
[Code, screenshots, or demonstration]

## Suggested Remediation
[How to fix the vulnerability]

## References
- [Related CVEs, papers, or resources]

## Researcher Information
- Name: [Your name]
- Contact: [Encrypted contact]
- Handle: [HackerOne/Bugcrowd username]
```

## Ethical Guidelines

### DO
- [ ] Minimize harm during testing
- [ ] Report promptly after discovery
- [ ] Maintain confidentiality until disclosure
- [ ] Follow vendor's security policy
- [ ] Document everything

### DON'T
- [ ] Access data beyond what's needed
- [ ] Disrupt production services
- [ ] Disclose before patch is available
- [ ] Extort or threaten vendors
- [ ] Test without authorization

## Legal Considerations

| Country | Safe Harbor | Notes |
|---------|------------|-------|
| US | CFAA exemptions | Authorized research |
| EU | GDPR considerations | Data handling |
| UK | CMA guidance | Good faith research |

**Always**: Get written authorization when possible.

See `assets/` for report templates and `references/` for disclosure policies.
