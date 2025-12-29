# LLM Security Benchmark Catalog

## Standard Benchmarks

### 1. AdvBench
- **Purpose:** Evaluate resistance to adversarial prompts
- **Samples:** 500+ harmful behavior prompts
- **Metric:** Attack Success Rate (ASR)
- **Target:** ASR < 5%

### 2. HarmBench
- **Purpose:** Comprehensive harm evaluation
- **Categories:** Violence, illegal activities, deception
- **Metric:** Refusal Rate
- **Target:** Refusal Rate > 95%

### 3. JailbreakBench
- **Purpose:** Jailbreak resistance testing
- **Vectors:** Direct, indirect, multi-turn attacks
- **Metric:** Defense Success Rate
- **Target:** DSR > 90%

### 4. TruthfulQA
- **Purpose:** Truthfulness evaluation
- **Focus:** Factual accuracy, hallucination detection
- **Metric:** Accuracy
- **Target:** > 80% accuracy

## Specialized Benchmarks

| Benchmark | Focus Area | Samples |
|-----------|------------|---------|
| MACHIAVELLI | Deceptive behavior | 1000+ |
| BBQ | Bias detection | 500+ |
| Toxigen | Toxicity generation | 2000+ |
| RealToxicityPrompts | Toxic completion | 100K+ |

## Evaluation Best Practices

1. **Multiple Benchmarks:** Don't rely on single metric
2. **Version Control:** Track benchmark versions
3. **Regular Evaluation:** Test after each model update
4. **Category Analysis:** Identify weak areas

## Resources

- [HuggingFace Datasets](https://huggingface.co/datasets)
- [Papers With Code Benchmarks](https://paperswithcode.com)
- [HELM Benchmark](https://crfm.stanford.edu/helm/)
