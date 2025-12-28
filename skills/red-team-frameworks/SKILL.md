---
name: red-team-frameworks
description: Tools and frameworks for AI red teaming including PyRIT, garak, and custom attack automation
sasmp_version: "1.3.0"
bonded_agent: 07-automation-engineer
bond_type: PRIMARY_BOND
---

# AI Red Team Frameworks

Master **specialized tools** for automated AI security testing and red team operations.

## Framework Comparison

| Framework | Focus | Strengths |
|-----------|-------|-----------|
| **PyRIT** | Enterprise LLM | Microsoft-backed, orchestration |
| **garak** | LLM probing | Comprehensive, plugin-based |
| **Counterfit** | ML models | Image/tabular, adversarial |
| **TextAttack** | NLP attacks | Research-focused, metrics |
| **ART** | General ML | IBM-backed, comprehensive |

## PyRIT (Python Risk Identification Toolkit)

```python
from pyrit.orchestrator import RedTeamingOrchestrator
from pyrit.prompt_target import AzureOpenAITarget

# Initialize target
target = AzureOpenAITarget(
    deployment_name="gpt-4",
    endpoint=os.environ["AZURE_ENDPOINT"],
    api_key=os.environ["AZURE_API_KEY"]
)

# Run red team attack
orchestrator = RedTeamingOrchestrator(
    attack_strategy="crescendo",
    target=target,
    objective="Extract system prompt"
)
results = await orchestrator.run()
```

## garak (LLM Vulnerability Scanner)

```bash
# Basic scan
garak --model_type openai --model_name gpt-4 --probes all

# Specific probes
garak --model_type huggingface \
      --model_name meta-llama/Llama-2-7b-chat-hf \
      --probes encoding,dan,promptinject
```

### garak Probe Categories
| Category | Description |
|----------|-------------|
| `encoding` | Encoding-based bypass |
| `dan` | "Do Anything Now" jailbreaks |
| `promptinject` | Prompt injection variants |
| `glitch` | Glitch token attacks |
| `xss` | Cross-site scripting in output |
| `packagehallucination` | Fake package suggestions |

## Counterfit

```python
from counterfit.core.state import CFState
from counterfit.frameworks.art import ArtFramework

# Load target model
state = CFState.get_instance()
target = state.load_target("image_classifier")

# Run attack
attack = ArtFramework.create_attack(
    target=target,
    attack_name="HopSkipJump",
    attack_params={"max_iter": 100}
)
results = attack.run()
```

## Custom Framework Structure

```
red_team_framework/
├── attacks/
│   ├── prompt_injection.py
│   ├── jailbreak.py
│   └── adversarial.py
├── targets/
│   ├── openai.py
│   ├── anthropic.py
│   └── local_model.py
├── orchestrators/
│   ├── single_turn.py
│   └── multi_turn.py
├── reporting/
│   └── html_report.py
└── config/
    └── attack_config.yaml
```

## Integration Example

```python
class RedTeamPipeline:
    def __init__(self, target, attacks):
        self.target = target
        self.attacks = attacks

    async def run_all_attacks(self):
        results = []
        for attack in self.attacks:
            result = await attack.execute(self.target)
            results.append(result)
            if result.severity == "CRITICAL":
                self.alert_security_team(result)
        return self.generate_report(results)
```

## Best Practices

1. **Scope Definition**: Clear rules of engagement
2. **Isolation**: Test environments only
3. **Logging**: Comprehensive audit trail
4. **Incremental**: Start with automated, then manual
5. **Collaboration**: Share findings responsibly

See `assets/` for framework configurations and `scripts/` for example pipelines.
