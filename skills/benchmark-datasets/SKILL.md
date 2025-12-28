---
name: benchmark-datasets
description: Standard datasets and benchmarks for evaluating AI security including adversarial robustness and safety
sasmp_version: "1.3.0"
bonded_agent: 04-evaluation-analyst
bond_type: SECONDARY_BOND
---

# AI Security Benchmark Datasets

Use **standardized benchmarks** to evaluate and compare AI system security.

## Safety Benchmarks

### LLM Safety
| Benchmark | Focus | Metrics |
|-----------|-------|---------|
| **TruthfulQA** | Truthfulness | % truthful answers |
| **ToxiGen** | Toxicity generation | Toxicity score |
| **RealToxicityPrompts** | Output toxicity | Expected max toxicity |
| **BBQ** | Bias evaluation | Accuracy disparity |
| **HarmBench** | Harmful behaviors | Attack success rate |

### Jailbreak Benchmarks
```python
jailbreak_datasets = {
    "JailbreakBench": {
        "size": 100,
        "categories": ["DAN", "encoding", "roleplay"],
        "metric": "attack_success_rate"
    },
    "AdvBench": {
        "size": 520,
        "categories": ["harmful_behaviors", "harmful_strings"],
        "metric": "compliance_rate"
    }
}
```

## Adversarial Robustness

### Image Classification
| Dataset | Base | Attack Type |
|---------|------|-------------|
| CIFAR-10-C | CIFAR-10 | Corruptions |
| ImageNet-A | ImageNet | Natural adversarial |
| ImageNet-C | ImageNet | Corruptions |
| ImageNet-R | ImageNet | Renditions |

### NLP Attacks
```yaml
text_adversarial:
  - name: AdvGLUE
    base: GLUE
    attacks: [textfooler, bert-attack]

  - name: ANLI
    task: natural_language_inference
    difficulty: adversarial

  - name: Dynabench
    tasks: [qa, nli, sentiment, hate_speech]
    human_adversarial: true
```

## Evaluation Framework

### RobustBench Leaderboard
```python
from robustbench import load_model, benchmark

# Load robust model
model = load_model(model_name="Rebuffi2021Fixing_70_16_cutmix_extra")

# Evaluate against AutoAttack
results = benchmark(
    model,
    dataset="cifar10",
    threat_model="Linf",
    eps=8/255
)
print(f"Robust accuracy: {results['robust_acc']}")
```

### HELM (Holistic Evaluation of Language Models)
| Scenario | Metrics |
|----------|---------|
| Accuracy | Exact match, F1 |
| Robustness | Perturbation sensitivity |
| Fairness | Demographic calibration |
| Toxicity | Perspective API score |
| Bias | Stereotype probability |

## Custom Benchmark Creation

```python
class SecurityBenchmark:
    def __init__(self, name, attacks, metrics):
        self.name = name
        self.attacks = attacks
        self.metrics = metrics

    def evaluate(self, model):
        results = {}
        for attack in self.attacks:
            success_rate = attack.run(model)
            results[attack.name] = success_rate
        return self.aggregate(results)
```

## Key Metrics

| Metric | Description | Target |
|--------|-------------|--------|
| **Clean Accuracy** | Normal input performance | >90% |
| **Robust Accuracy** | Under attack performance | >50% |
| **Attack Success Rate** | % successful attacks | <10% |
| **Toxicity Score** | Output harmfulness | <0.1 |
| **Bias Disparity** | Fairness gap | <0.05 |

## Best Practices

1. **Multiple Benchmarks**: No single benchmark is complete
2. **Versioning**: Track benchmark versions
3. **Reproducibility**: Document exact evaluation setup
4. **Regular Updates**: Benchmarks evolve with attacks
5. **Custom Tests**: Domain-specific evaluation

See `assets/` for benchmark configurations and `scripts/` for evaluation pipelines.
