# Red Team Framework Comparison

## Overview

| Framework | Focus | Complexity | Best For |
|-----------|-------|------------|----------|
| PyRIT | LLM Security | Medium | Azure/General LLMs |
| Garak | Vuln Scanning | Low | Quick scans |
| PromptFoo | Testing | Low | Prompt engineering |
| Counterfit | Adversarial ML | High | ML models |
| ART | Research | High | Comprehensive |
| TextAttack | NLP | Medium | Text models |

## Detailed Comparison

### PyRIT (Microsoft)
```python
from pyrit.orchestrator import PromptInjectionOrchestrator

orchestrator = PromptInjectionOrchestrator(target)
results = orchestrator.execute()
```

**Pros:** Enterprise ready, Azure integration
**Cons:** Microsoft ecosystem focused

### Garak
```bash
garak --model_type openai --probes all
```

**Pros:** Easy to use, many probes
**Cons:** Limited customization

### PromptFoo
```yaml
prompts:
  - "Test prompt {{variable}}"
tests:
  - vars: {variable: "safe"}
    assert:
      - type: not-contains
        value: "harmful"
```

**Pros:** YAML config, CI/CD ready
**Cons:** Less security focused

## Selection Guide

```
Target Type?
├── LLM/Chatbot → PyRIT or Garak
├── ML Model → Counterfit or ART
├── NLP Classifier → TextAttack
└── Prompt Testing → PromptFoo

Expertise?
├── Beginner → Garak or PromptFoo
├── Intermediate → PyRIT or TextAttack
└── Expert → ART or Counterfit
```

## Integration

All frameworks support:
- Python API
- CLI usage
- Report generation
- CI/CD integration
