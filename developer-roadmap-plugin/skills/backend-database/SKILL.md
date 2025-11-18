---
name: backend-architecture
description: Design and build scalable backend systems, master database technologies, design APIs, implement authentication, and optimize performance. Use for backend design, database selection, API development, and scaling strategies.
---

# Backend Architecture & Database Mastery

**Design scalable backend systems, master databases, and build production-ready APIs** with proven patterns and best practices.

## Quick Start: REST API with Express & PostgreSQL

```javascript
// Express API Server
const express = require('express');
const { Pool } = require('pg');
const app = express();

app.use(express.json());

// Database connection pool
const pool = new Pool({
  connectionString: 'postgresql://user:password@localhost/mydb'
});

// Middleware: Authentication
const auth = (req, res, next) => {
  const token = req.headers.authorization?.split(' ')[1];
  if (!token) return res.status(401).json({ error: 'Unauthorized' });
  // Verify token
  next();
};

// Routes
app.get('/users', async (req, res) => {
  try {
    const result = await pool.query('SELECT * FROM users');
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post('/users', auth, async (req, res) => {
  const { name, email } = req.body;
  try {
    const result = await pool.query(
      'INSERT INTO users(name, email) VALUES($1, $2) RETURNING *',
      [name, email]
    );
    res.status(201).json(result.rows[0]);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

app.listen(3000);
```

## Database Selection Guide

### **PostgreSQL (Most Versatile)**
- **Best For:** Complex queries, ACID compliance, complex data
- **Strengths:** Full-featured, reliable, extensible
- **Weaknesses:** Requires careful configuration for massive scale
- **Use When:** Data integrity critical, complex relationships
- **Connection:** `postgresql://user:pass@host/db`

### **MongoDB (Document Database)**
```javascript
const db = client.db('mydb');
const users = db.collection('users');

// Insert
await users.insertOne({ name: 'Alice', email: 'alice@example.com' });

// Query
const user = await users.findOne({ email: 'alice@example.com' });

// Update
await users.updateOne(
  { email: 'alice@example.com' },
  { $set: { name: 'Alice Updated' } }
);
```
- **Best For:** Flexible schema, rapid prototyping, unstructured data
- **Strengths:** Flexible, scalable, easy to start
- **Weaknesses:** No transactions (older versions), can use more storage
- **Use When:** Schema flexibility needed, rapid iteration

### **Redis (In-Memory Cache)**
- **Best For:** Caching, real-time data, sessions, leaderboards
- **Strengths:** Extremely fast, simple operations
- **Weaknesses:** Not persistent, limited data structures
- **Use When:** Speed critical, temporary data

### **Elasticsearch (Search Engine)**
- **Best For:** Full-text search, log analysis, analytics
- **Strengths:** Powerful search, distributed, analytics
- **Weaknesses:** Complex, resource-hungry
- **Use When:** Search functionality needed

## API Design Patterns

### **RESTful API Design**
```
Resource-oriented URLs:
GET    /api/users          # List all users
GET    /api/users/:id      # Get specific user
POST   /api/users          # Create user
PUT    /api/users/:id      # Update user
DELETE /api/users/:id      # Delete user

Query parameters for filtering:
GET /api/users?role=admin&limit=10&offset=20

Status codes:
200 OK               - Successful request
201 Created          - Resource created
400 Bad Request      - Invalid input
401 Unauthorized     - Not authenticated
403 Forbidden        - Not authorized
404 Not Found        - Resource not found
500 Server Error     - Server problem
```

### **GraphQL API Design**
```graphql
# Query - Read operations
query {
  users {
    id
    name
    email
    posts {
      id
      title
    }
  }
}

# Mutation - Write operations
mutation {
  createUser(input: { name: "Alice", email: "alice@example.com" }) {
    id
    name
    email
  }
}

# Subscription - Real-time
subscription {
  userCreated {
    id
    name
  }
}
```

**GraphQL Advantages:**
- No over/under-fetching
- Strong type system
- Introspection for documentation
- Single query for related data

## Authentication & Authorization

### **JWT (JSON Web Tokens)**
```javascript
const jwt = require('jsonwebtoken');

// Create token
const token = jwt.sign(
  { userId: 123, role: 'admin' },
  'secret-key',
  { expiresIn: '24h' }
);

// Verify token
const decoded = jwt.verify(token, 'secret-key');
console.log(decoded); // { userId: 123, role: 'admin', ... }
```

### **Authorization Patterns**
- **Role-Based Access Control (RBAC):** Users have roles (admin, user, guest)
- **Permission-Based Access Control (PBAC):** Users have specific permissions
- **OAuth 2.0:** Third-party authentication (Google, GitHub)

## Caching Strategies

### **Cache Levels**
1. **Application Cache** (In-memory)
   - Use case: Frequently accessed, rarely changing data
   - Tool: Node.js Map, Python dict

2. **Distributed Cache** (Redis)
   - Use case: Shared cache across servers
   - TTL: 5 min - 24 hours depending on data

3. **Database Query Cache**
   - Use case: Expensive queries
   - Pattern: Check cache, if miss query DB, store in cache

4. **HTTP Cache** (Browser/CDN)
   - Use case: Static content
   - Headers: Cache-Control, ETag

```javascript
// Redis caching pattern
async function getUser(userId) {
  // Check cache
  const cached = await redis.get(`user:${userId}`);
  if (cached) return JSON.parse(cached);

  // Query DB if not cached
  const user = await db.query('SELECT * FROM users WHERE id = ?', [userId]);

  // Store in cache for 1 hour
  await redis.setex(`user:${userId}`, 3600, JSON.stringify(user));

  return user;
}
```

## Scaling Patterns

### **Horizontal Scaling**
- **Load Balancing:** Distribute traffic across multiple servers
- **Database Replication:** Multiple database copies for reads
- **Caching:** Reduce database load
- **Message Queues:** Async processing

### **Database Optimization**
- **Indexing:** Speed up queries
- **Query Optimization:** Reduce expensive operations
- **Connection Pooling:** Reuse database connections
- **Read Replicas:** Separate read/write traffic

## ORM Example: Prisma

```javascript
// schema.prisma
model User {
  id    Int     @id @default(autoincrement())
  name  String
  email String  @unique
  posts Post[]
}

model Post {
  id    Int     @id @default(autoincrement())
  title String
  authorId Int
  author User @relation(fields: [authorId], references: [id])
}

// Usage
const user = await prisma.user.create({
  data: {
    name: 'Alice',
    email: 'alice@example.com',
    posts: {
      create: [
        { title: 'First Post' },
        { title: 'Second Post' }
      ]
    }
  },
  include: { posts: true }
});
```

## When to Use This Skill

- User is **designing backend systems**
- User needs **database selection help**
- User is building **REST or GraphQL APIs**
- User wants **caching strategies**
- User needs **authentication implementation**
- User is **optimizing database queries**
- User wants to understand **scaling patterns**

---

Build robust, scalable backend systems!
