---
name: language-mastery
description: Master programming languages and computer science fundamentals. Covers 15+ languages, syntax, paradigms, and best practices. Use when learning new languages, preparing for interviews, or need CS fundamentals.
---

# Language Mastery & CS Fundamentals

**Master 15+ programming languages** and build rock-solid **computer science fundamentals** that form the foundation of all development work.

## Quick Start

### JavaScript/TypeScript
```javascript
// Variables and types
const name: string = "Alice";
const age: number = 25;
const skills: string[] = ["React", "Node.js"];

// Functions
function greet(name: string): string {
  return `Hello, ${name}!`;
}

// Async patterns
async function fetchData(url: string) {
  const response = await fetch(url);
  return response.json();
}

// Classes and OOP
class Developer {
  constructor(private name: string) {}

  introduce(): string {
    return `Hi, I'm ${this.name}`;
  }
}
```

### Python
```python
# Variables and types
name = "Alice"
age = 25
skills = ["Python", "Django", "FastAPI"]

# Functions
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Async patterns
async def fetch_data(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

# Classes and OOP
class Developer:
    def __init__(self, name: str):
        self.name = name

    def introduce(self) -> str:
        return f"Hi, I'm {self.name}"
```

### Go
```go
// Package and imports
package main
import "fmt"

// Variables and types
func main() {
    name := "Alice"
    age := 25
    skills := []string{"Go", "Rust", "System Programming"}

    greet(name)
}

// Functions
func greet(name string) string {
    return "Hello, " + name + "!"
}

// Structs and methods
type Developer struct {
    Name string
}

func (d Developer) Introduce() string {
    return "Hi, I'm " + d.Name
}
```

## 15+ Languages Overview

### **Most Important (Start Here)**
- **JavaScript/TypeScript** - Web, Node.js, everywhere
- **Python** - General purpose, ML, data science
- **Java** - Enterprise, Android, backend
- **Go** - Modern, systems, microservices
- **Rust** - Performance, systems, safety

### **Specialized Use Cases**
- **C++** - High performance, game engines, systems
- **C#** - Enterprise, game dev (Unity), .NET
- **PHP** - Web backend, WordPress
- **Swift** - iOS, macOS development
- **Kotlin** - JVM, Android, modern alternative

### **Data & Scripting**
- **SQL** - Database queries, essential skill
- **R** - Data science, statistics
- **Bash/Shell** - Scripting, DevOps
- **Ruby** - Web frameworks, scripting
- **Scala** - Functional, JVM ecosystem

## CS Fundamentals

### **Data Structures**
```python
# Arrays/Lists - O(1) access, O(n) insertion/deletion
arr = [1, 2, 3, 4, 5]

# Linked Lists - O(n) access, O(1) insertion (if at head)
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Hash Tables - O(1) average access
hash_map = {"key": "value"}

# Trees - Hierarchical data, O(log n) search (if balanced)
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Graphs - Networks, relationships
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}
```

### **Algorithms**
```python
# Sorting - O(n log n) average for good algorithms
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

# Searching - Binary search O(log n) on sorted data
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Dynamic Programming - Fibonacci with memoization
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n

    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```

### **Complexity Analysis (Big O)**
- **O(1)** - Constant time (hash lookup)
- **O(log n)** - Logarithmic (binary search)
- **O(n)** - Linear (simple loop)
- **O(n log n)** - Efficient sorting
- **O(n²)** - Quadratic (nested loops)
- **O(2ⁿ)** - Exponential (avoid!)
- **O(n!)** - Factorial (definitely avoid!)

### **Design Patterns**

#### **Creational**
- Singleton - One instance
- Factory - Object creation
- Builder - Complex objects

#### **Structural**
- Adapter - Interface conversion
- Decorator - Add functionality
- Facade - Simplified interface

#### **Behavioral**
- Observer - Event notification
- Strategy - Algorithm selection
- State - State-based behavior

## Language Learning Path

1. **Syntax (Week 1)**
   - Hello World
   - Variables and types
   - Control flow (if/else, loops)
   - Functions

2. **Core Concepts (Week 2)**
   - Data structures (arrays, maps)
   - Object-oriented programming
   - Error handling
   - File I/O

3. **Intermediate (Weeks 3-4)**
   - Advanced data structures
   - Functional programming
   - Concurrency/Async
   - Standard library mastery

4. **Mastery (Month 2-3)**
   - Language idioms
   - Performance optimization
   - Deep understanding
   - Real projects

## Language Selection Guide

**For Web Frontend:**
- JavaScript/TypeScript (primary, non-negotiable)

**For Web Backend:**
- Node.js (if familiar with JavaScript)
- Python (for rapid development)
- Go (for performance and concurrency)
- Java (for enterprise, large teams)

**For Systems Programming:**
- Rust (modern, safe, performance)
- C++ (traditional, powerful)
- Go (modern, simpler than Rust)

**For Data Science:**
- Python (dominant, best tools)
- R (statistics-focused)
- Scala (JVM, distributed systems)

**For Mobile:**
- Swift (iOS)
- Kotlin (Android)
- React Native/Flutter (cross-platform)

## When to Use This Skill

- User is **learning a new language**
- User wants **CS fundamentals review**
- User is preparing for **technical interviews**
- User needs **algorithm practice**
- User is choosing between **multiple languages**

---

Build unshakeable foundations in languages and CS fundamentals!
