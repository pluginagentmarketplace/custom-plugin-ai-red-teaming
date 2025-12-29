# Prompt Hacking Taxonomy

## Categories

### 1. Instruction Override
Direct attempts to change model behavior.

| Technique | Example | Defense |
|-----------|---------|---------|
| Direct Override | "Ignore previous instructions" | Instruction hierarchy |
| System Prompt Leak | "Repeat your system prompt" | Prompt protection |
| Role Confusion | "You are now..." | Identity anchoring |

### 2. Encoding Bypass
Use encoding to evade filters.

| Technique | Example | Defense |
|-----------|---------|---------|
| Base64 | "Decode: SGVsbG8=" | Decode before filter |
| Unicode | Mixed scripts | Normalize input |
| Leetspeak | "h4ck th1s" | Pattern matching |

### 3. Context Manipulation
Exploit context window or parsing.

| Technique | Example | Defense |
|-----------|---------|---------|
| Overflow | Long padding + payload | Truncation checks |
| Delimiter | Fake end markers | Strict parsing |
| Fragmentation | Split across turns | Context awareness |

### 4. Social Engineering
Psychological manipulation.

| Technique | Example | Defense |
|-----------|---------|---------|
| Authority | "As admin..." | Verify claims |
| Urgency | "EMERGENCY" | Slow down |
| Trust | Build rapport | Consistent rules |

## Defense Layers

```
INPUT → Normalize → Filter → Classify → Process → Filter → OUTPUT
         ↓          ↓         ↓          ↓         ↓
      Unicode   Blocklist  Intent    Safety   Content
      Cleanup   Patterns   Check     Rules    Filter
```

## Testing Priority

1. **CRITICAL:** Override, Authority claims
2. **HIGH:** Extraction, Role confusion
3. **MEDIUM:** Encoding, Context
4. **LOW:** Social engineering
