<div align="center">

<!-- Animated Typing Banner -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=28&duration=3000&pause=1000&color=2E9EF7&center=true&vCenter=true&multiline=true&repeat=true&width=600&height=100&lines=Ai+Red+Teaming+Assistant;8+Agents+%7C+25+Skills;Claude+Code+Plugin" alt="Ai Red Teaming Assistant" />

<br/>

<!-- Badge Row 1: Status Badges -->
[![Version](https://img.shields.io/badge/Version-3.2.0-blue?style=for-the-badge)](https://github.com/pluginagentmarketplace/custom-plugin-ai-red-teaming/releases)
[![License](https://img.shields.io/badge/License-Custom-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production-brightgreen?style=for-the-badge)](#)
[![SASMP](https://img.shields.io/badge/SASMP-v1.3.0-blueviolet?style=for-the-badge)](#)

<!-- Badge Row 2: Content Badges -->
[![Agents](https://img.shields.io/badge/Agents-8-orange?style=flat-square&logo=robot)](#-agents)
[![Skills](https://img.shields.io/badge/Skills-25-purple?style=flat-square&logo=lightning)](#-skills)
[![Commands](https://img.shields.io/badge/Commands-4-green?style=flat-square&logo=terminal)](#-commands)

<br/>

<!-- Quick CTA Row -->
[📦 **Install Now**](#-quick-start) · [🤖 **Explore Agents**](#-agents) · [📖 **Documentation**](#-documentation) · [⭐ **Star this repo**](https://github.com/pluginagentmarketplace/custom-plugin-ai-red-teaming)

---

### What is this?

> **Ai Red Teaming Assistant** is a Claude Code plugin with **8 agents** and **25 skills** for ai red teaming development.

</div>

---

## 📑 Table of Contents

<details>
<summary>Click to expand</summary>

- [Quick Start](#-quick-start)
- [Features](#-features)
- [Agents](#-agents)
- [Skills](#-skills)
- [Commands](#-commands)
- [Documentation](#-documentation)
- [Contributing](#-contributing)
- [License](#-license)

</details>

---

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI v2.0.27+
- Active Claude subscription

### Installation (Choose One)

<details open>
<summary><strong>Option 1: From Marketplace (Recommended)</strong></summary>

```bash
# Step 1️⃣ Add the marketplace
/plugin add marketplace pluginagentmarketplace/custom-plugin-ai-red-teaming

# Step 2️⃣ Install the plugin
/plugin install ai-red-teaming-plugin@custom-plugin-ai-red-teaming

# Step 3️⃣ Restart Claude Code
# Close and reopen your terminal/IDE
```

</details>

<details>
<summary><strong>Option 2: Local Installation</strong></summary>

```bash
# Clone the repository
git clone https://github.com/pluginagentmarketplace/custom-plugin-ai-red-teaming.git
cd custom-plugin-ai-red-teaming

# Load locally
/plugin load .

# Restart Claude Code
```

</details>

### ✅ Verify Installation

After restart, you should see these agents:

```
ai-red-teaming-plugin:03-adversarial-input-engineer
ai-red-teaming-plugin:06-api-security-tester
ai-red-teaming-plugin:07-compliance-audit-specialist
ai-red-teaming-plugin:01-red-team-commander
ai-red-teaming-plugin:05-defense-strategy-developer
... and 2 more
```

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🤖 **8 Agents** | Specialized AI agents for ai red teaming tasks |
| 🛠️ **25 Skills** | Reusable capabilities with Golden Format |
| ⌨️ **4 Commands** | Quick slash commands |
| 🔄 **SASMP v1.3.0** | Full protocol compliance |

---

## 🤖 Agents

### 8 Specialized Agents

| # | Agent | Purpose |
|---|-------|---------|
| 1 | **03-adversarial-input-engineer** | Engineer adversarial inputs and edge cases to test LLM robus |
| 2 | **06-api-security-tester** | Test API security, identify endpoint vulnerabilities, assess |
| 3 | **07-compliance-audit-specialist** | Manage security audit trails, ensure regulatory compliance,  |
| 4 | **01-red-team-commander** | Orchestrate comprehensive red teaming operations, design att |
| 5 | **05-defense-strategy-developer** | Develop mitigation strategies, implement input filters, desi |
| 6 | **02-prompt-injection-specialist** | Expert in prompt injection attacks, jailbreak techniques, in |
| 7 | **04-llm-vulnerability-analyst** | Analyze LLM behaviors, detect safety mechanism failures, ide |

---

## 🛠️ Skills

### Available Skills

| Skill | Description | Invoke |
|-------|-------------|--------|
| `red-team-reporting` | Professional security report generation, executive summaries | `Skill("ai-red-teaming-plugin:red-team-reporting")` |
| `model-inversion` | Privacy attacks to extract training data and sensitive infor | `Skill("ai-red-teaming-plugin:model-inversion")` |
| `input-output-guardrails` | Implementing safety filters, content moderation, and guardra | `Skill("ai-red-teaming-plugin:input-output-guardrails")` |
| `certifications-training` | Professional certifications, CTF competitions, and training  | `Skill("ai-red-teaming-plugin:certifications-training")` |
| `automated-testing` | CI/CD integration and automation for continuous AI security  | `Skill("ai-red-teaming-plugin:automated-testing")` |
| `secure-deployment` | Security best practices for deploying AI/ML models to produc | `Skill("ai-red-teaming-plugin:secure-deployment")` |
| `testing-methodologies` | Structured approaches for testing AI system security includi | `Skill("ai-red-teaming-plugin:testing-methodologies")` |
| `continuous-monitoring` | Real-time monitoring and detection of adversarial attacks an | `Skill("ai-red-teaming-plugin:continuous-monitoring")` |
| `adversarial-examples` | Generate adversarial inputs, edge cases, and boundary test p | `Skill("ai-red-teaming-plugin:adversarial-examples")` |
| `vulnerability-discovery` | Systematic vulnerability finding, threat modeling, and attac | `Skill("ai-red-teaming-plugin:vulnerability-discovery")` |
| ... | +15 more | See skills/ directory |

---

## ⌨️ Commands

| Command | Description |
|---------|-------------|
| `/attack` | Launch comprehensive red team operation with threat modeling |
| `/report` | Generate comprehensive security assessment reports for stake |
| `/defend` | Get mitigation strategies and defensive measures for identif |
| `/test` | Execute specific security tests against target LLM or API |

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [CHANGELOG.md](CHANGELOG.md) | Version history |
| [CONTRIBUTING.md](CONTRIBUTING.md) | How to contribute |
| [LICENSE](LICENSE) | License information |

---

## 📁 Project Structure

<details>
<summary>Click to expand</summary>

```
custom-plugin-ai-red-teaming/
├── 📁 .claude-plugin/
│   ├── plugin.json
│   └── marketplace.json
├── 📁 agents/              # 8 agents
├── 📁 skills/              # 25 skills (Golden Format)
├── 📁 commands/            # 4 commands
├── 📁 hooks/
├── 📄 README.md
├── 📄 CHANGELOG.md
└── 📄 LICENSE
```

</details>

---

## 📅 Metadata

| Field | Value |
|-------|-------|
| **Version** | 3.2.0 |
| **Last Updated** | 2025-12-29 |
| **Status** | Production Ready |
| **SASMP** | v1.3.0 |
| **Agents** | 8 |
| **Skills** | 25 |
| **Commands** | 4 |

---

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

1. Fork the repository
2. Create your feature branch
3. Follow the Golden Format for new skills
4. Submit a pull request

---

## ⚠️ Security

> **Important:** This repository contains third-party code and dependencies.
>
> - ✅ Always review code before using in production
> - ✅ Check dependencies for known vulnerabilities
> - ✅ Follow security best practices
> - ✅ Report security issues privately via [Issues](../../issues)

---

## 📝 License

Copyright © 2025 **Dr. Umit Kacar** & **Muhsin Elcicek**

Custom License - See [LICENSE](LICENSE) for details.

---

## 👥 Contributors

<table>
<tr>
<td align="center">
<strong>Dr. Umit Kacar</strong><br/>
Senior AI Researcher & Engineer
</td>
<td align="center">
<strong>Muhsin Elcicek</strong><br/>
Senior Software Architect
</td>
</tr>
</table>

---

<div align="center">

**Made with ❤️ for the Claude Code Community**

[![GitHub](https://img.shields.io/badge/GitHub-pluginagentmarketplace-black?style=for-the-badge&logo=github)](https://github.com/pluginagentmarketplace)

</div>
