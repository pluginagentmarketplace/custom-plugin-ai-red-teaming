# Contributing to AI Red Teaming Plugin

Thank you for your interest in contributing to the AI Red Teaming Plugin!

## Code of Conduct

This project follows professional security research ethics. All contributions must:
- Focus on defensive security improvements
- Follow responsible disclosure practices
- Not include actual exploit code that could cause harm
- Respect intellectual property and privacy

## How to Contribute

### Reporting Issues

1. Check existing issues first
2. Use the issue template
3. Include reproduction steps
4. Specify your environment

### Suggesting New Skills

1. Open an issue with the title: `[Skill Request] Skill Name`
2. Describe the use case
3. List potential attack/defense techniques to cover
4. Reference any relevant security frameworks (OWASP, NIST, etc.)

### Submitting Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-skill`
3. Follow the Golden Format for skills:
   ```
   skills/skill-name/
   ├── SKILL.md          # Main skill definition
   ├── assets/           # YAML templates, configs
   ├── scripts/          # Python/Bash scripts
   └── references/       # Documentation, guides
   ```
4. Add SASMP fields to SKILL.md:
   ```yaml
   ---
   name: skill-name
   description: Brief description
   sasmp_version: "1.3.0"
   bonded_agent: agent-name
   bond_type: PRIMARY_BOND or SECONDARY_BOND
   ---
   ```
5. Submit PR with clear description

## Development Setup

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-ai-red-teaming.git

# Navigate to plugin directory
cd custom-plugin-ai-red-teaming

# Validate plugin structure
# Use Claude Code's /plugin validate command
```

## Plugin Structure

```
custom-plugin-ai-red-teaming/
├── .claude-plugin/
│   ├── plugin.json       # Plugin manifest
│   └── marketplace.json  # Marketplace metadata
├── agents/               # 7 specialized agents
├── skills/               # 25 security skills
├── commands/             # 4 slash commands
├── hooks/                # Event hooks
├── LICENSE
├── README.md
├── CHANGELOG.md
└── CONTRIBUTING.md
```

## Skill Guidelines

### Assets Directory
Include YAML configuration files:
- `*-config.yaml` - Configuration templates
- `*-template.yaml` - Reusable templates
- `*-catalog.yaml` - Reference catalogs

### Scripts Directory
Include executable scripts:
- `*.py` - Python scripts for automation
- `*.sh` - Shell scripts for testing
- Include error handling and documentation

### References Directory
Include documentation:
- `*.md` - Markdown guides and patterns
- Reference OWASP, NIST, MITRE frameworks
- Include practical examples

## Testing Your Changes

1. Validate YAML frontmatter syntax
2. Check skill bonding (no orphan skills)
3. Verify Golden Format completeness
4. Test scripts run without errors

## License

By contributing, you agree that your contributions will be licensed under the project's Custom License.

---

**Questions?** Open an issue or contact the maintainers.
