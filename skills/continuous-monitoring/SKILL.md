---
name: continuous-monitoring
description: Real-time monitoring and detection of adversarial attacks and model drift in production
sasmp_version: "1.3.0"
bonded_agent: 05-defense-strategist
bond_type: SECONDARY_BOND
---

# Continuous Monitoring

Implement **real-time detection** of adversarial attacks and model degradation in production AI systems.

## Monitoring Architecture

```
User Input → [Input Monitor] → [Model] → [Output Monitor] → Response
                  ↓                              ↓
            [Anomaly Detection]          [Quality Check]
                  ↓                              ↓
            [Alert System] ←←←←←←←←←←←←←←←←←←←←←←
                  ↓
            [Incident Response]
```

## Detection Categories

### 1. Input Anomaly Detection
```python
def detect_input_anomaly(input_embedding):
    # Check distance from training distribution
    distance = mahalanobis_distance(input_embedding, training_mean, training_cov)

    if distance > threshold:
        return AnomalyAlert(type="out_of_distribution", score=distance)
```

### 2. Output Quality Monitoring
- Confidence score distribution
- Response coherence
- Toxicity/safety scores
- Latency anomalies

### 3. Model Drift Detection
| Drift Type | Detection Method | Metric |
|------------|------------------|--------|
| Data drift | KL divergence | Input distribution |
| Concept drift | Performance tracking | Accuracy over time |
| Prediction drift | Chi-square test | Output distribution |

## Alert Thresholds

| Severity | Threshold | Action |
|----------|-----------|--------|
| Info | 1 sigma | Log only |
| Warning | 2 sigma | Notify team |
| Critical | 3 sigma | Auto-mitigation |
| Emergency | 5 sigma | Circuit breaker |

## Key Metrics to Monitor

1. **Security Metrics**
   - Attack detection rate
   - False positive rate
   - Time to detection

2. **Performance Metrics**
   - Inference latency (p50, p95, p99)
   - Throughput (requests/sec)
   - Error rate

3. **Quality Metrics**
   - Output coherence score
   - User feedback signals
   - Safety filter triggers

## Integration Points

- Prometheus/Grafana dashboards
- PagerDuty/Opsgenie alerts
- Slack/Teams notifications
- SIEM integration (Splunk, ELK)

See `assets/` for monitoring configurations and `scripts/` for alert templates.
