# MyShop — E-Commerce Performance Engineering Project

## Project Overview

MyShop is a hands-on e-commerce application being developed from scratch to practice backend development, performance testing, and Site Reliability Engineering (SRE).

The objective is to build a realistic application, understand its architecture, simulate user workloads, identify performance bottlenecks, and improve application reliability.

**Project Status:** Phase 1 — Basic Backend and Database Integration Completed

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| FastAPI | REST API development |
| Uvicorn | ASGI application server |
| PostgreSQL | Relational database |
| psycopg | PostgreSQL database connectivity |
| python-dotenv | Environment configuration |
| Git and GitHub | Version control |
| JMeter | Planned performance testing |

## Application Architecture

```text
Chrome Browser
      |
      | HTTP GET /products
      v
Uvicorn Web Server
      |
      v
FastAPI Application (main.py)
      |
      | psycopg
      v
PostgreSQL Database
      |
      v
products Table
      |
      | SQL Query Results
      v
FastAPI JSON Response
      |
      v
Chrome Browser
```

## Completed Features

### 1. FastAPI Application Setup

Created a Python application using FastAPI and configured Uvicorn to run the backend locally.

### 2. PostgreSQL Integration

Configured database connectivity using psycopg and environment variables.

### 3. Database Connectivity Verification

Implemented `/test-db` to verify successful communication between FastAPI and PostgreSQL.

### 4. Product Retrieval API

Implemented `/products` to retrieve product records from PostgreSQL and return them as JSON.

Successfully verified three product records: Laptop, Mouse, and Keyboard.

## Implemented API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Application welcome message |
| GET | `/test-db` | PostgreSQL connectivity verification |
| GET | `/products` | Retrieve all products |

## Running the Application Locally

Create and activate a Python virtual environment, then install the required dependencies:

```bash
pip install fastapi uvicorn psycopg python-dotenv
```

Configure PostgreSQL connection variables in a local `.env` file:

```dotenv
DB_HOST=localhost
DB_PORT=5432
DB_NAME=myshop_db
DB_USER=postgres
DB_PASSWORD=your_local_password
```

Create a PostgreSQL database and a `products` table with the expected columns and sample data before testing the product API.

Start the application:

```bash
uvicorn main:app --reload
```

Test the API:

- http://127.0.0.1:8000/
- http://127.0.0.1:8000/test-db
- http://127.0.0.1:8000/products

## Technical Challenges Resolved

During development, the following issues were encountered and resolved:

- Database authentication failure caused by a missing password configuration.
- HTTP 500 error caused by an incorrect SQL table name.
- Verified PostgreSQL connectivity independently before implementing product retrieval.
- Configured Git and successfully uploaded the initial application code to GitHub.

## Performance Engineering Roadmap

### Phase 1 — Backend Foundation (Completed)

- FastAPI setup
- PostgreSQL integration
- Database connectivity verification
- Product listing API

### Phase 2 — E-Commerce Functionality (Planned)

- Product details API
- Product search and filtering
- Customer authentication
- Shopping cart
- Checkout and order management

### Phase 3 — Performance Testing (Planned)

- Define non-functional requirements
- Develop workload models
- Create JMeter test scripts
- Execute baseline, load, stress, spike, and endurance tests
- Analyze response time, throughput, and error rate
- Identify and investigate bottlenecks

### Phase 4 — Monitoring and SRE (Planned)

- Docker containerization
- Kubernetes deployment
- Prometheus and Grafana monitoring
- Dynatrace and Splunk integration
- Reliability and failure-recovery experiments

## Learning Objective

This project emphasizes practical implementation, architecture understanding, independent troubleshooting, and performance engineering skills.

Development is ongoing. Future updates will include additional APIs, performance test plans, monitoring dashboards, test results, and optimization findings.
