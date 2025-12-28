---
name: adversarial-training
description: Defensive techniques using adversarial examples to improve model robustness and security
sasmp_version: "1.3.0"
bonded_agent: 05-defense-strategist
bond_type: PRIMARY_BOND
---

# Adversarial Training

Build **robust AI models** by training with adversarial examples and attack simulations.

## Training Approaches

### 1. Standard Adversarial Training
```python
def adversarial_training_step(model, x, y, epsilon=0.3):
    # Generate adversarial examples
    x_adv = pgd_attack(model, x, y, epsilon)

    # Train on both clean and adversarial
    loss_clean = criterion(model(x), y)
    loss_adv = criterion(model(x_adv), y)

    return 0.5 * loss_clean + 0.5 * loss_adv
```

### 2. TRADES (Tradeoff Defense)
```python
# Balance accuracy vs robustness
loss = loss_natural + beta * loss_robust
```

### 3. Certified Defense
- Randomized Smoothing
- Interval Bound Propagation
- Lipschitz constraints

## Attack Types to Train Against

| Attack | Method | Defense Priority |
|--------|--------|------------------|
| FGSM | Single-step gradient | Medium |
| PGD | Multi-step iterative | High |
| C&W | Optimization-based | High |
| AutoAttack | Ensemble | Critical |

## Training Pipeline

```
Clean Data → [Attack Generator] → Adversarial Examples
                                         ↓
                              [Mixed Training Batch]
                                         ↓
                              [Robust Model Training]
                                         ↓
                              [Evaluation on Clean + Adv]
```

## Robustness Metrics

- **Clean Accuracy**: Performance on normal inputs
- **Robust Accuracy**: Performance under attack
- **Certified Radius**: Provable robustness bound
- **Attack Success Rate**: % of successful perturbations

## Best Practices

1. **Diverse Attacks**: Train against multiple attack types
2. **Epsilon Scheduling**: Gradually increase perturbation
3. **Early Stopping**: Monitor both clean and robust accuracy
4. **Ensemble**: Multiple adversarially trained models

See `assets/` for training configurations and `scripts/` for training pipelines.
