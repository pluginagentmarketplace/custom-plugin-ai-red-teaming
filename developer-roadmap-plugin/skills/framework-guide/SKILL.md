---
name: framework-expertise
description: Master frontend, backend, and specialized frameworks. Covers React, Vue, Angular, Node.js, Django, Spring Boot, and ecosystem tools. Use when learning frameworks, choosing between options, or need best practices.
---

# Framework Expertise & Ecosystem Mastery

**Master 20+ frameworks and libraries** across frontend, backend, and specialized domains with structured learning paths and best practices.

## Quick Start: React (Most Popular Frontend)

```jsx
// Function Components with Hooks
import { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);
  const [data, setData] = useState(null);

  // Fetch data on mount
  useEffect(() => {
    fetch('/api/data')
      .then(r => r.json())
      .then(d => setData(d));
  }, []);

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      {data && <p>Data: {JSON.stringify(data)}</p>}
    </div>
  );
}
```

## Frontend Frameworks

### **React (Most Popular)**
- **Learning Time:** 2-3 weeks basics, 2-3 months mastery
- **Ecosystem:** Next.js, Redux, TanStack Query, Tailwind
- **Best For:** Large apps, job market demand, flexibility
- **Key Concepts:** Components, Hooks, Virtual DOM
- **Advanced:** Code splitting, SSR, performance optimization

### **Vue.js (Easiest to Learn)**
- **Learning Time:** 1-2 weeks basics, 2-3 months mastery
- **Ecosystem:** Nuxt.js, Pinia, Vue Router
- **Best For:** Quick learning, productivity, single-page apps
- **Key Concepts:** Templates, Reactive data, Composition API
- **Advanced:** Plugins, state management, SSR with Nuxt

### **Angular (Most Structured)**
- **Learning Time:** 3-4 weeks basics, 3-4 months mastery
- **Ecosystem:** TypeScript first, RxJS, dependency injection
- **Best For:** Large teams, enterprise apps, structure
- **Key Concepts:** Modules, Services, Decorators, Observables
- **Advanced:** Change detection, performance, architectural patterns

### **Other Frontend Frameworks**
- **Svelte** - Compiler-based, very efficient
- **Astro** - Static site generation, island architecture
- **Solid.js** - Fine-grained reactivity
- **Web Components** - Browser standard, framework-agnostic

## Backend Frameworks

### **Express.js (Most Flexible)**
```javascript
const express = require('express');
const app = express();

app.use(express.json());

// Middleware
app.use((req, res, next) => {
  console.log(`${req.method} ${req.path}`);
  next();
});

// Routes
app.get('/users', (req, res) => {
  res.json({ users: [] });
});

app.post('/users', (req, res) => {
  // Handle creation
  res.status(201).json({ id: 1 });
});

app.listen(3000, () => console.log('Server running'));
```

### **FastAPI (Modern Python)**
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

@app.get("/users")
async def get_users():
    return {"users": []}

@app.post("/users")
async def create_user(user: User):
    return {"id": 1, **user.dict()}
```

### **Django (Batteries-Included Python)**
- ORM with migrations
- Admin interface
- Authentication built-in
- Good for rapid development
- Large ecosystem

### **Spring Boot (Enterprise Java)**
- Dependency injection
- Auto-configuration
- Actuator for monitoring
- Large enterprise ecosystem
- Excellent scalability

### **Go Frameworks (Modern & Fast)**
- **Gin** - Popular, fast routing
- **Echo** - Lightweight, flexible
- **Fiber** - Express.js-like for Go

## Framework Selection Matrix

| Criteria | Best | Runner-up | Trade-off |
|----------|------|-----------|-----------|
| **Learning Speed** | Vue | Svelte | Ecosystem vs Simplicity |
| **Performance** | Svelte | Astro | Efficiency vs Features |
| **Job Market** | React | Vue | Demand vs Learning ease |
| **Enterprise** | Angular | React | Structure vs Flexibility |
| **Startup Speed** | Express | Fastify | Minimalism vs Features |
| **Data Heavy** | FastAPI | Spring Boot | Modern vs Mature |

## Full-Stack Frameworks

### **Next.js (React Full-Stack)**
- Server-side rendering
- API routes
- File-based routing
- Static generation
- Fast-growing ecosystem

### **Nuxt.js (Vue Full-Stack)**
- Auto-routing
- Middleware
- Modules ecosystem
- Module auto-import
- Growing ecosystem

### **Full Stack Benefits**
- Shared code between frontend/backend
- Type safety (TypeScript)
- Simplified deployment
- Better developer experience
- Easier code organization

## Database & ORM Frameworks

### **Prisma (Modern ORM)**
```javascript
import { PrismaClient } from '@prisma/client';
const prisma = new PrismaClient();

// Type-safe, auto-generated client
const user = await prisma.user.create({
  data: { name: 'Alice', email: 'alice@example.com' }
});
```

### **Other ORMs**
- TypeORM (TypeScript)
- Sequelize (Node.js)
- SQLAlchemy (Python)
- Hibernate (Java)

## Testing Frameworks

### **Jest (JavaScript)**
```javascript
describe('Calculator', () => {
  it('should add two numbers', () => {
    const result = add(2, 3);
    expect(result).toBe(5);
  });
});
```

### **Other Testing Frameworks**
- Vitest (Vite-native)
- pytest (Python)
- JUnit (Java)
- Cypress/Playwright (E2E)

## Framework Learning Path

**Month 1: Fundamentals**
- Official tutorial (full completion)
- Create 2-3 small projects
- Understand component lifecycle
- Learn state management basics

**Month 2: Intermediate**
- Build medium-sized project (5-10 components)
- Advanced routing
- Forms and validation
- API integration
- Testing basics

**Month 3: Advanced**
- Performance optimization
- Code splitting and lazy loading
- Advanced state management
- Server-side rendering (if applicable)
- Production deployment

## When to Use This Skill

- User is **choosing a framework**
- User is **learning a new framework**
- User needs **framework best practices**
- User wants to **optimize framework usage**
- User is **comparing framework ecosystems**

---

Master frameworks to build production-ready applications!
