---
name: system-design
description: Master system design, large-scale architectures, design patterns, API design, scalability, and distributed systems. Essential for architect roles and senior positions. Use for designing systems, architecture decisions, and technical interviews.
---

# System Design & Architecture Mastery

**Design large-scale systems, master architectural patterns, and make strategic architecture decisions** that enable growth and reliability.

## Quick Start: URL Shortener System Design

### **Problem Statement**
- **Functional:** POST to create short URL, GET to redirect
- **Non-functional:** 1 million requests/day, 99.9% uptime, <100ms latency
- **Storage:** 500M URLs, 100 bytes per entry = 50GB

### **Architecture**

```
┌──────────────────────────────────────┐
│         Client (Web/Mobile)          │
└────────────┬─────────────────────────┘
             │
┌────────────▼─────────────────────────┐
│      API Gateway / Load Balancer      │
└────────────┬─────────────────────────┘
             │
     ┌───────┴───────┐
     │               │
┌────▼────┐      ┌───▼────┐
│API Srv 1 │      │API Srv 2 │ (Multiple servers for scalability)
└────┬────┘      └───┬────┘
     │               │
     │               │ (Read replicas for scale)
     └───────┬───────┘
             │
        ┌────▼──────────────────────┐
        │   Primary Database         │
        │  (PostgreSQL)              │
        │  Table: urls               │
        │    - id (PK)               │
        │    - short_code (unique)   │
        │    - long_url              │
        │    - created_at            │
        │  Index: short_code         │
        └────┬──────────────────────┘
             │
        ┌────▼──────────────┐
        │  Read Replicas    │
        │  (3 instances)    │
        └───────────────────┘
             │
        ┌────▼──────────┐
        │  Redis Cache  │
        │  (Hot URLs)   │
        │  TTL: 24h     │
        └───────────────┘
```

### **Algorithm for Short Code**
```python
import random
import string

def generate_short_code(length=6):
    """Generate random short code"""
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# With custom mapping for compactness
BASE62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode_base62(num):
    """Convert number to base62"""
    if num == 0:
        return "0"
    result = []
    while num > 0:
        result.append(BASE62[num % 62])
        num //= 62
    return ''.join(reversed(result))

# Use auto-increment ID, convert to base62
def create_short_url(long_url):
    # Insert into DB, get auto-increment ID
    url_id = db.insert(long_url)
    # Convert to short code
    short_code = encode_base62(url_id)
    return f"https://short.url/{short_code}"
```

## CAP Theorem in Practice

```
CAP Theorem: Choose 2 of 3

       ┌──────────────────────────────┐
       │         CONSISTENCY          │ (All nodes see same data)
       └──────────────────────────────┘
                    ▲
                   / \
                  /   \
                 /     \
    ┌───────────────────────────────┐  ┌──────────────────────────┐
    │   AVAILABILITY                │  │  PARTITION TOLERANCE     │
    │(System always responsive)     │  │ (Tolerates node failures)│
    └───────────────────────────────┘  └──────────────────────────┘

System Types:
- CP: Consistency + Partition Tolerance (PostgreSQL, MongoDB)
  - Sacrifice availability: Stop serving if partition occurs
  - Use for: Banking, critical data

- AP: Availability + Partition Tolerance (Cassandra, DynamoDB)
  - Sacrifice consistency: Eventual consistency
  - Use for: Real-time systems, social media

- CA: Consistency + Availability (Traditional SQL)
  - Sacrifice partition tolerance: No distributed systems
  - Use for: Single datacenter
```

## Design Patterns

### **Monolithic vs Microservices**
```yaml
Monolithic:
  ├── Single codebase
  ├── Single database
  ├── Single deployment
  ├── Pros: Simplicity, easier debugging
  └── Cons: Limited scalability, technology lock-in

Microservices:
  ├── Multiple codebases
  ├── Multiple databases
  ├── Independent deployment
  ├── Pros: Scalability, flexibility, team autonomy
  └── Cons: Complexity, distributed systems challenges
```

### **Event-Driven Architecture**
```yaml
Publisher-Subscriber Pattern:
┌──────────────┐
│   Service A  │ (Publishes event)
└──────┬───────┘
       │
       │ Event: UserCreated
       │
   ┌───▼────────────────────────────┐
   │      Message Queue (Kafka)     │
   └───┬────────────────────────────┘
       │
       ├─► Service B (Subscribes: Send welcome email)
       ├─► Service C (Subscribes: Create user profile)
       └─► Service D (Subscribes: Initialize settings)
```

### **CQRS (Command Query Responsibility Segregation)**
```yaml
Traditional:
  Single Model
  ├── Read queries
  └── Write commands

CQRS:
  Write Model (Commands)      Read Model (Queries)
  ├── Normalize for writes    ├── Denormalized for reads
  ├── Validate input          ├── Optimized for queries
  ├── Update primary DB       ├── Updated via events
  └── Emit events             └── Serve read requests
```

## Scalability Strategies

### **Vertical vs Horizontal Scaling**
```
Vertical Scaling (Scale Up):
  1 Server 2GB RAM   →   1 Server 16GB RAM
  Pros: Simple
  Cons: Limited by hardware, downtime during upgrades

Horizontal Scaling (Scale Out):
  1 Server 2GB RAM   →   10 Servers 2GB RAM each
  Pros: Unlimited growth
  Cons: More complexity (load balancing, consistency)
```

### **Database Sharding**
```python
# Shard by user_id
def get_shard_id(user_id):
    num_shards = 10
    return user_id % num_shards

# Store user in shard 3, 7, etc. based on ID
def get_user(user_id):
    shard_id = get_shard_id(user_id)
    db = connect(f"shard_{shard_id}")
    return db.query(f"SELECT * FROM users WHERE id = {user_id}")

# Pros: Horizontal scalability
# Cons: Cross-shard queries complex, data rebalancing needed
```

## API Design Patterns

### **Versioning Strategies**
```
URL versioning:
GET /api/v1/users
GET /api/v2/users

Header versioning:
GET /api/users
Header: API-Version: 2

Parameter versioning:
GET /api/users?version=2
```

### **Rate Limiting**
```
Token Bucket Algorithm:
- Bucket capacity: 100 requests
- Refill rate: 10 requests/second
- Each request consumes 1 token
- If bucket empty, reject request

HTTP Headers:
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1609459200
```

## Performance Optimization

### **Caching Strategy**
```
Cache Hierarchy:
1. Browser Cache (HTTP cache)
2. CDN Cache (Global distribution)
3. Application Cache (Redis, Memcached)
4. Database Query Cache
5. Database (Disk I/O)

Decision Tree:
- Static content? → Use CDN
- User-specific? → Application cache with TTL
- Expensive query? → Query cache (Cache-Aside pattern)
- Frequently accessed? → Redis cluster
```

### **N+1 Query Problem**
```python
# BAD: N+1 queries
users = db.query("SELECT * FROM users LIMIT 10")
for user in users:
    posts = db.query(f"SELECT * FROM posts WHERE user_id = {user.id}")
    # 1 query for users + 10 queries for posts = 11 queries!

# GOOD: Join query
users_with_posts = db.query("""
    SELECT u.*, p.* FROM users u
    LEFT JOIN posts p ON u.id = p.user_id
    LIMIT 10
""")
# 1 query!

# GOOD: Eager loading
users = db.query("SELECT * FROM users LIMIT 10").populate('posts')
# Uses database relationships efficiently
```

## Distributed Systems Concepts

### **Consistency Models**
```
Strong Consistency:
- All reads see latest write
- Example: Bank account balance
- Cost: Performance, latency

Eventual Consistency:
- Reads may see stale data temporarily
- Eventually all nodes converge
- Example: Social media likes
- Benefit: High performance, availability

Causal Consistency:
- Causally related operations in order
- Concurrent operations any order
- Balance of strong + eventual
```

### **Failure Handling**
```python
# Circuit Breaker Pattern
from pybreaker import CircuitBreaker

breaker = CircuitBreaker(
    fail_max=5,
    reset_timeout=60
)

@breaker
def call_external_service():
    return requests.get("https://api.example.com")

# Behavior:
# 1. Closed: Normal operation
# 2. Open: Fails quickly after 5 failures
# 3. Half-Open: Test if service recovered
```

## When to Use This Skill

- User is **designing systems**
- User preparing for **system design interviews**
- User needs **architecture guidance**
- User wants to understand **scalability**
- User is making **architectural decisions**
- User needs **performance optimization**

---

Master architecture to build systems at scale!
