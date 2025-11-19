---
name: cloud-infrastructure
description: Deploy and manage cloud infrastructure, containerize applications with Docker, orchestrate with Kubernetes, implement CI/CD pipelines, and monitor systems. Use for cloud deployment, DevOps practices, infrastructure management, and scaling.
---

# Cloud Infrastructure & DevOps Mastery

**Deploy applications to cloud platforms, containerize with Docker, orchestrate with Kubernetes, and automate infrastructure** with industry-standard tools and practices.

## Quick Start: Docker

### **Dockerfile**
```dockerfile
# Use official Node.js runtime
FROM node:18-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Expose port
EXPOSE 3000

# Health check
HEALTHCHECK --interval=30s --timeout=3s \
  CMD node healthcheck.js

# Start application
CMD ["node", "server.js"]
```

### **Build and Run**
```bash
# Build image
docker build -t myapp:1.0 .

# Run container
docker run -p 3000:3000 --name myapp myapp:1.0

# View logs
docker logs myapp

# Stop container
docker stop myapp
```

### **Docker Compose (Multi-container)**
```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "3000:3000"
    environment:
      DATABASE_URL: postgresql://db:5432/mydb
    depends_on:
      - db

  db:
    image: postgres:15-alpine
    environment:
      POSTGRES_PASSWORD: password
      POSTGRES_DB: mydb
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

## Cloud Platforms Comparison

### **AWS (Most Popular)**
```bash
# EC2 - Virtual machines
aws ec2 run-instances --image-id ami-12345 --instance-type t3.micro

# Lambda - Serverless functions
aws lambda invoke --function-name myFunction output.json

# S3 - Object storage
aws s3 cp myfile.txt s3://mybucket/

# RDS - Managed database
aws rds create-db-instance --db-instance-identifier mydb
```

**Services:**
- **Compute:** EC2, Lambda, ECS, EKS
- **Storage:** S3, EBS, EFS
- **Database:** RDS, DynamoDB, ElastiCache
- **Networking:** VPC, CloudFront, Route53
- **Management:** CloudWatch, CloudTrail, IAM

### **Google Cloud Platform (GCP)**
- **Compute:** Compute Engine, Cloud Run, Cloud Functions
- **Storage:** Cloud Storage, Datastore, Firestore
- **Database:** Cloud SQL, Cloud Spanner, BigTable
- **Analytics:** BigQuery, Dataflow, Pub/Sub

### **Microsoft Azure**
- **Compute:** Virtual Machines, App Service, Functions
- **Storage:** Blob Storage, Table Storage
- **Database:** Azure SQL, Cosmos DB

## Kubernetes Fundamentals

### **Key Concepts**
```yaml
# Deployment - Manages replicas of pods
apiVersion: apps/v1
kind: Deployment
metadata:
  name: myapp
spec:
  replicas: 3
  selector:
    matchLabels:
      app: myapp
  template:
    metadata:
      labels:
        app: myapp
    spec:
      containers:
      - name: myapp
        image: myapp:1.0
        ports:
        - containerPort: 3000
        resources:
          requests:
            memory: "64Mi"
            cpu: "250m"
          limits:
            memory: "128Mi"
            cpu: "500m"

---
# Service - Exposes pods
apiVersion: v1
kind: Service
metadata:
  name: myapp-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 3000
  selector:
    app: myapp
```

### **Kubernetes Commands**
```bash
# Apply configuration
kubectl apply -f deployment.yaml

# View pods
kubectl get pods

# View deployments
kubectl get deployments

# Scale deployment
kubectl scale deployment myapp --replicas=5

# View logs
kubectl logs myapp-pod-name

# Port forward
kubectl port-forward svc/myapp-service 3000:80
```

### **StatefulSets (for stateful apps)**
```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mydb
spec:
  serviceName: mydb
  replicas: 3
  selector:
    matchLabels:
      app: mydb
  template:
    # ... pod template ...
```

## Infrastructure as Code: Terraform

```hcl
# Provider configuration
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Variables
variable "instance_type" {
  default = "t3.micro"
}

# Resources
resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = var.instance_type

  tags = {
    Name = "WebServer"
  }
}

resource "aws_security_group" "web" {
  name = "web-sg"

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Outputs
output "instance_ip" {
  value = aws_instance.web.public_ip
}
```

## CI/CD Pipeline: GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Set up Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm ci

      - name: Run tests
        run: npm test

      - name: Build
        run: npm run build

      - name: Build Docker image
        run: docker build -t myapp:latest .

      - name: Push to registry
        run: docker push myapp:latest

      - name: Deploy to Kubernetes
        run: kubectl set image deployment/myapp myapp=myapp:latest
```

## Monitoring & Observability

### **Prometheus Metrics**
```javascript
// Track metrics
const prometheus = require('prom-client');

const httpRequestDuration = new prometheus.Histogram({
  name: 'http_request_duration_seconds',
  help: 'Duration of HTTP requests in seconds',
  labelNames: ['method', 'route', 'status_code']
});

app.use((req, res, next) => {
  const start = Date.now();
  res.on('finish', () => {
    const duration = (Date.now() - start) / 1000;
    httpRequestDuration.labels(req.method, req.route?.path, res.statusCode).observe(duration);
  });
  next();
});
```

### **Logging: Winston (Node.js)**
```javascript
const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

logger.info('Application started');
logger.error('An error occurred', { userId: 123 });
```

## When to Use This Skill

- User wants to **deploy applications** to cloud
- User needs **containerization help**
- User is **managing infrastructure**
- User wants to **setup CI/CD pipelines**
- User is **scaling applications**
- User needs **monitoring and observability**

---

Master cloud infrastructure for production deployments!
