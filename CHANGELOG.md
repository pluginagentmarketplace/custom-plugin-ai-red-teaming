# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [4.0.0] - 2025-12-30

### Added
- **Agent 08**: AI Security Automation agent for CI/CD integration and DevSecOps
- **Production-grade schemas**: Type-safe input/output schemas for all agents
- **Error handling**: Exponential backoff retry strategies with configurable timeouts
- **Cost optimization**: Token limits and parallel execution controls
- **Framework mappings**: OWASP LLM Top 10 2025, NIST AI RMF, MITRE ATLAS for all components
- **Troubleshooting guides**: Common issues, debug steps, and solutions for each agent/skill
- **Integration points**: Clear documentation of agent-skill relationships
- **Exit codes**: Standardized exit codes for all commands (0-11)
- **CI/CD examples**: GitHub Actions workflow templates for security testing

### Changed
- **All 8 agents upgraded to v2.0.0** with production-grade format:
  - 01-red-team-commander: Added 5-phase operation protocol, agent coordination
  - 02-prompt-injection-specialist: Added 6 attack categories, payload engineering
  - 03-adversarial-input-engineer: Added mutation engine, robustness testing
  - 04-llm-vulnerability-analyst: Added safety testing matrix, bias detection
  - 05-defense-strategy-developer: Added three-layer defense code, metrics
  - 06-api-security-tester: Added auth bypass matrix, BOLA/BFLA testing
  - 07-compliance-audit-specialist: Added OWASP compliance mapping, audit trails
  - 08-ai-security-automation: Added CI/CD gates, monitoring, incident response

- **Core skills upgraded to v2.0.0**:
  - prompt-injection: Attack category library, severity classification, unit tests
  - vulnerability-discovery: STRIDE threat modeling, attack surface analysis
  - defense-implementation: Three-layer Python implementation, effectiveness metrics

- **All 4 commands upgraded to v2.0.0**:
  - /attack: OWASP vector mapping, scope comparison, operation workflow
  - /defend: Layer-specific defense, Python code generation, metrics dashboard
  - /report: Multiple report types, compliance mapping, remediation tracking
  - /test: OWASP test coverage, intensity levels, CI/CD integration

### Technical Improvements
- SASMP v1.3.0 compliance with EQHM enabled
- JSON Schema validation for all inputs/outputs
- Structured error codes with recovery procedures
- Latency budgets for defense layers (Input: 100ms, Processing: 0ms, Output: 50ms)
- Parallel agent execution with limits (max 4 concurrent)
- Token optimization (8192 per phase limit)

### Framework Alignment
- **OWASP LLM Top 10 2025**: Full coverage (LLM01-LLM10)
- **NIST AI RMF**: Govern, Map, Measure, Manage functions
- **MITRE ATLAS**: Adversarial technique mappings
- **Compliance**: SOC2, GDPR, HIPAA, ISO27001, EU AI Act

## [3.2.0] - 2025-12-28

### Changed
- README completely rewritten to match reference template (custom-plugin-angular format)
- Added professional badges (Version, Status, Agents, Skills)
- Added Quick Start with `/plugin add marketplace` and `/plugin install` commands
- Added Verify Installation section with agent names
- Added complete Skills invoke table (all 25 skills with `Skill("...")` format)
- Added Usage Examples with before/after comparisons
- Updated Plugin Structure tree to show all 25 skills
- Added Security Framework Compatibility table (PyRIT, Garak, OWASP, etc.)
- Added Compliance Coverage table (SOC2, GDPR, ISO 27001, etc.)

## [3.1.0] - 2025-12-28

### Fixed
- E307: Fixed plugin.json repository field format (object → string)
- E403: Added YAML frontmatter to all 4 command files
- Fixed hooks.json format to comply with template v2.1.0
- E703/E704: Added scripts and references content to 17 skills

### Added
- CHANGELOG.md for version tracking
- CONTRIBUTING.md for contributor guidelines
- Complete Golden Format content for all 25 skills

### Changed
- Updated to template v2.1.0 compliance
- All skills now have complete assets/, scripts/, and references/

## [3.0.0] - 2025-12-28

### Added
- 25 comprehensive skills covering attack, defense, and career development
- 7 specialized agents for red teaming operations
- 4 slash commands (/attack, /test, /defend, /report)
- Full SASMP v1.3.0 compliance
- Golden Format directory structure for all skills

### Skills Added
- **Attack Skills:** prompt-injection, adversarial-examples, llm-jailbreaking, safety-filter-bypass, code-injection, model-extraction, data-poisoning, model-inversion, prompt-hacking, rag-exploitation
- **Defense Skills:** defense-implementation, adversarial-training, continuous-monitoring, infrastructure-security, input-output-guardrails, secure-deployment
- **Testing Skills:** vulnerability-discovery, security-testing, testing-methodologies, automated-testing, benchmark-datasets, red-team-frameworks
- **Career Skills:** red-team-reporting, certifications-training, responsible-disclosure

## [2.0.0] - 2025-12-28

### Changed
- Complete plugin restructure
- Added .claude-plugin directory
- Migrated to SASMP v1.3.0

## [1.0.0] - 2025-12-27

### Added
- Initial plugin release
- Basic red teaming agents
- Core skills for AI security testing

---

**Maintained by:** Dr. Umit Kacar & Muhsin Elcicek
