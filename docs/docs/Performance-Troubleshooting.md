# MyShop – Performance Troubleshooting

## Case Study 01: HTTP Keep-Alive Connection Failure

### 1. Objective

Investigate intermittent HTTP connection failures observed during concurrent API performance testing and validate a server configuration change.

### 2. Technical Environment

- Application: MyShop
- Backend: Python FastAPI
- Application Server: Uvicorn
- Database: PostgreSQL
- Load Testing Tool: Apache JMeter 5.6.3
- Environment: Local Windows machine

### 3. Workload Configuration

| Parameter | Value |
|---|---|
| Concurrent users | 30 |
| Ramp-up period | 60 seconds |
| Test duration | 360 seconds |
| Steady-state duration | Approximately 300 seconds |
| Loop count | Infinite, controlled by duration |
| HTTP Keep-Alive | Enabled |

### 4. Business Transactions

| Transaction | Endpoint | Think Time |
|---|---|---|
| T01_Home | GET / | 0 seconds |
| T02_BrowseProducts | GET /products | 2 seconds |
| T03_ViewProduct | GET /products/2 | 5 seconds |

### 5. Problem Statement

During concurrent load testing, intermittent connection failures were observed.

Exceptions included:

- org.apache.http.NoHttpResponseException
- java.net.SocketException: Connection reset

### 6. Investigation

Reviewed the following:

- JMeter error responses
- HTTP Keep-Alive configuration
- Transaction-level think time
- Uvicorn server timeout configuration

Identified a potential mismatch between the five-second transaction think time and the default five-second Uvicorn idle keep-alive timeout.

The suspected cause was an attempt to reuse an HTTP connection that the server was closing or had already closed.

### 7. Configuration Change

Increased the Uvicorn HTTP keep-alive timeout from 5 seconds to 30 seconds.

Command used:

`.\.venv\Scripts\python.exe -m uvicorn main:app --reload --timeout-keep-alive 30`

### 8. Before and After Comparison

| Metric | Before | After |
|---|---|---|
| Concurrent users | 30 | 30 |
| Keep-alive timeout | 5 seconds | 30 seconds |
| Connection failures | Observed | Not observed |
| Error rate | Non-zero | 0% |

### 9. Conclusion

Increasing the HTTP keep-alive timeout eliminated the observed connection failures in the subsequent test.

The results support the suspected connection reuse issue. Additional network-level evidence would be required to conclusively establish the root cause.

### 10. Skills Demonstrated

- Concurrent API performance testing
- JMeter workload modelling
- HTTP connection management
- Error and exception analysis
- Server configuration tuning
- Hypothesis-driven troubleshooting
- Before-and-after performance validation

### 11. Next Steps

- Attach JMeter execution results and screenshots.
- Compare response time percentiles and throughput.
- Implement PostgreSQL database connection pooling.
- Conduct controlled performance comparison tests.
- Integrate application monitoring tools.