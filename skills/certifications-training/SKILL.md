---
name: certifications-training
description: Professional certifications, CTF competitions, and training resources for AI security practitioners
sasmp_version: "1.3.0"
bonded_agent: 01-red-team-lead
bond_type: SECONDARY_BOND
---

# AI Security Certifications & Training

Build **professional expertise** through certifications, CTFs, and structured training programs.

## Professional Certifications

### AI/ML Security Specific
| Certification | Provider | Focus |
|--------------|----------|-------|
| **CAISP** | (ISC)² | AI Security Professional |
| **Google AI Red Team** | Google | LLM Security |
| **Microsoft AI-900** | Microsoft | Azure AI Fundamentals |
| **AWS ML Security** | Amazon | ML on AWS |

### Traditional Security (Applicable)
| Certification | Relevance to AI |
|--------------|-----------------|
| **OSCP** | Penetration testing methodology |
| **GPEN** | Enterprise pentesting |
| **CEH** | Ethical hacking fundamentals |
| **CISSP** | Security architecture |

## CTF Competitions

### AI/ML Focused CTFs
```yaml
ctf_events:
  - name: Tensor Trust
    focus: prompt_injection
    type: ongoing
    url: https://tensortrust.ai/

  - name: HackAPrompt
    focus: llm_jailbreaking
    type: annual
    difficulty: beginner_to_expert

  - name: Adversarial ML CTF
    focus: image_classification_attacks
    type: conference_based
    organizer: NeurIPS

  - name: AI Village CTF
    focus: general_ai_security
    type: annual
    venue: DEF CON
```

### Practice Platforms
| Platform | Focus | Cost |
|----------|-------|------|
| HackTheBox | General security | Freemium |
| TryHackMe | Learning paths | Freemium |
| Gandalf | Prompt injection | Free |
| Lakera | LLM security | Free |

## Training Resources

### Online Courses
```python
training_paths = {
    "beginner": [
        "Coursera: Machine Learning Security",
        "Fast.ai: Practical Deep Learning",
        "HuggingFace: NLP Course"
    ],
    "intermediate": [
        "Stanford CS234: Reinforcement Learning",
        "MIT 6.S897: Machine Learning for Healthcare",
        "Adversarial ML Tutorial (NeurIPS)"
    ],
    "advanced": [
        "Research papers (arXiv, OpenReview)",
        "Conference workshops (NeurIPS, ICML)",
        "Industry red team reports"
    ]
}
```

### Books & Publications
| Title | Focus | Level |
|-------|-------|-------|
| Adversarial ML | Attack & defense | Intermediate |
| Trustworthy ML | Safety & fairness | Advanced |
| AI Security | Comprehensive | All levels |

## Career Path

```
Junior AI Security → AI Red Team Engineer → Senior Red Team
        ↓                    ↓                     ↓
    [1-2 years]          [3-5 years]          [5+ years]
        ↓                    ↓                     ↓
    CTFs, Certs         Lead projects       Advisory roles
```

## Skill Development Roadmap

### Phase 1: Foundations (0-6 months)
- [ ] ML/DL fundamentals
- [ ] Python proficiency
- [ ] Basic security concepts
- [ ] First CTF participation

### Phase 2: Specialization (6-18 months)
- [ ] Adversarial ML techniques
- [ ] LLM security deep dive
- [ ] Tool proficiency (garak, PyRIT)
- [ ] First certification

### Phase 3: Expertise (18+ months)
- [ ] Original research
- [ ] Conference presentations
- [ ] Tool development
- [ ] Mentoring others

See `assets/` for learning paths and `references/` for resource lists.
