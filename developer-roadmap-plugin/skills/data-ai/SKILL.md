---
name: data-science-ai
description: Master machine learning, data engineering, LLMs, prompt engineering, AI agents, and MLOps. Covers Python ML libraries, data pipelines, LLM applications, and model deployment. Use for ML projects, data engineering, AI agent development, and ML system design.
---

# Data Science & AI Mastery

**Build machine learning systems, design data pipelines, master LLMs, engineer prompts, and deploy AI agents** with production-ready patterns and frameworks.

## Quick Start: Machine Learning with Scikit-learn

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

# 1. Load data
iris = load_iris()
X, y = iris.data, iris.target

# 2. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Preprocess
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 5. Evaluate
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
precision = precision_score(y_test, predictions, average='weighted')
recall = recall_score(y_test, predictions, average='weighted')

print(f"Accuracy: {accuracy:.2%}")
print(f"Precision: {precision:.2%}")
print(f"Recall: {recall:.2%}")
```

## ML Workflow

### **1. Data Collection & Exploration**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data.csv')

# Explore
print(df.head())
print(df.describe())
print(df.isnull().sum())

# Visualize
df['age'].hist(bins=30)
plt.show()
```

### **2. Data Preprocessing**
```python
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.impute import SimpleImputer

# Handle missing values
imputer = SimpleImputer(strategy='mean')
df['age'] = imputer.fit_transform(df[['age']])

# Encode categorical variables
encoder = LabelEncoder()
df['category'] = encoder.fit_transform(df['category'])

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```

### **3. Feature Engineering**
```python
# Create new features
df['age_squared'] = df['age'] ** 2
df['interaction'] = df['age'] * df['income']

# Select important features
from sklearn.feature_selection import SelectKBest, f_classif

selector = SelectKBest(f_classif, k=10)
X_selected = selector.fit_transform(X, y)
```

### **4. Model Training & Evaluation**
```python
from sklearn.model_selection import cross_val_score
from sklearn.metrics import confusion_matrix, classification_report

# Cross-validation
scores = cross_val_score(model, X, y, cv=5)
print(f"Mean accuracy: {scores.mean():.2%}")

# Detailed evaluation
cm = confusion_matrix(y_test, predictions)
print(classification_report(y_test, predictions))
```

## Deep Learning with PyTorch

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

# Define model
class NeuralNet(nn.Module):
    def __init__(self, input_size, hidden_size, num_classes):
        super().__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        return x

# Training loop
model = NeuralNet(784, 128, 10)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters())

for epoch in range(10):
    for batch_x, batch_y in train_loader:
        # Forward pass
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)

        # Backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```

## Prompt Engineering for LLMs

### **Prompt Techniques**
```python
from anthropic import Anthropic

client = Anthropic()

# 1. Zero-shot prompting
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": "What is machine learning?"
    }]
)

# 2. Few-shot prompting
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": """Classify sentiment (positive/negative):

Example 1: "I love this product!" - positive
Example 2: "This is terrible" - negative

Classify: "Amazing experience, highly recommend!"
"""
    }]
)

# 3. Chain of Thought
response = client.messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[{
        "role": "user",
        "content": """Solve step by step:
If there are 3 apples and you buy 5 more, then give away 2,
how many apples do you have?

Think through each step before giving your answer."""
    }]
)
```

## AI Agents with LangChain

```python
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_anthropic import ChatAnthropic
from langchain import hub

# Define tools
def calculator(expression: str) -> str:
    return str(eval(expression))

def web_search(query: str) -> str:
    # Implementation
    return "search results"

tools = [
    Tool(
        name="Calculator",
        func=calculator,
        description="Useful for math calculations"
    ),
    Tool(
        name="WebSearch",
        func=web_search,
        description="Search the web for information"
    )
]

# Create agent
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022")
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, tools=tools)

# Use agent
result = agent_executor.invoke({
    "input": "What is 25 * 4? Also, what are latest AI trends?"
})
print(result["output"])
```

## Data Engineering Pipeline

```python
# Apache Spark data processing
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("DataPipeline").getOrCreate()

# Read data
df = spark.read.csv("data.csv", header=True)

# Transform
df_cleaned = df.dropna()
df_processed = df_cleaned.filter(df_cleaned.age > 18)

# Aggregate
result = df_processed.groupBy("category").count()

# Write output
result.write.mode("overwrite").parquet("output/result")
```

## MLOps: Model Tracking with MLflow

```python
import mlflow
from mlflow import log_metric, log_param, log_model

# Track experiment
mlflow.start_run()

# Log parameters
mlflow.log_param("n_estimators", 100)
mlflow.log_param("max_depth", 10)

# Log metrics
mlflow.log_metric("accuracy", 0.95)
mlflow.log_metric("f1_score", 0.92)

# Log model
mlflow.sklearn.log_model(model, "model")

mlflow.end_run()

# View results
mlflow ui  # Open http://localhost:5000
```

## When to Use This Skill

- User is **building ML models**
- User needs **data pipeline design**
- User is working with **LLMs and prompts**
- User is **implementing AI agents**
- User wants **MLOps guidance**
- User needs **ML system design**
- User is **deploying ML models**

---

Build intelligent systems with ML and AI!
