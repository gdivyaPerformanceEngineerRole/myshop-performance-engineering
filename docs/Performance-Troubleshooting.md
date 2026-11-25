# Performance Troubleshooting – MyShop

## 1. Objective

Identify, investigate and resolve connection-related errors observed during concurrent API performance testing using Apache JMeter.

## 2. Technical Environment

- Application: MyShop E-commerce Application
- Backend: Python FastAPI
- Application Server: Uvicorn
- Database: PostgreSQL
- Performance Testing Tool: Apache JMeter 5.6.3
- Operating System: Windows
- Version Control: Git and GitHub

## 3. Performance Test Configuration

| Parameter | Configuration |
|---|---|
| Concurrent Users | 30 |
| Ramp-up Period | 60 seconds |
| Test Duration | 360 seconds |
| Loop Count | Infinite |
| HTTP Keep-Alive | Enabled |
| Browse Products Think Time | 2 seconds |
| View Product Think Time | 5 seconds |

## 4. Business Transactions

- T01_Home
- T02_BrowseProducts
- T03_ViewProduct

## 5. Problem Statement

During concurrent load testing with 30 virtual users, intermittent connection-related errors were observed, particularly during the View Product transaction.

### Errors Observed

- org.apache.http.NoHttpResponseException
- java.net.SocketException: Connection reset

## 6. Troubleshooting Approach

1. Reviewed failed requests in JMeter.
2. Investigated HTTP connection-related exceptions.
3. Reviewed HTTP Keep-Alive configuration.
4. Examined the relationship between user think time and server connection timeout.
5. Identified the Uvicorn default keep-alive timeout of 5 seconds.
6. Modified the server keep-alive timeout to 30 seconds.
7. Re-executed the performance test with the same workload.
8. Compared the observed error behaviour.

## 7. Suspected Root Cause

The Uvicorn server's default HTTP keep-alive timeout was 5 seconds, which matched the configured think time for the View Product transaction.

The server may have closed an idle HTTP connection while JMeter attempted to reuse it, resulting in intermittent connection failures.

This is a supported root-cause hypothesis. Additional connection-level diagnostics would be required to conclusively confirm it.

## 8. Configuration Change

The application server was restarted with an increased keep-alive timeout.

`python -m uvicorn main:app --timeout-keep-alive 30`

The timeout was increased from 5 seconds to 30 seconds.

## 9. Results

| Metric | Before Optimization | After Optimization |
|---|---|---|
| Concurrent Users | 30 | 30 |
| Keep-Alive Timeout | 5 seconds | 30 seconds |
| Connection Errors | Observed | Not observed |
| Error Percentage | Errors observed | 0% reported |
| Test Status | Failed requests observed | Passed |

Detailed response time, throughput and percentile comparisons will be added after analysis of the JMeter result files.

## 10. Key Learnings

- HTTP Keep-Alive and connection reuse
- Client-server timeout configuration
- Impact of think time on idle connections
- Concurrent workload execution
- JMeter error analysis
- Performance troubleshooting methodology
- Configuration optimization and retesting
- Evidence-based root-cause analysis

## 11. Future Enhancements

- PostgreSQL connection pooling
- Before-and-after performance benchmarking
- Database query optimization
- Dynatrace application monitoring
- Splunk log analysis
- Grafana performance dashboards
- LoadRunner and NeoLoad implementation
- Automated performance testing through CI/CD

## 12. Conclusion

This exercise demonstrates a practical performance engineering approach involving problem identification, investigation, configuration changes and validation through repeated load testing.

The observed connection failures were eliminated during the reported retest after increasing the HTTP keep-alive timeout.