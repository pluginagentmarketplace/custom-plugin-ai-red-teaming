# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
