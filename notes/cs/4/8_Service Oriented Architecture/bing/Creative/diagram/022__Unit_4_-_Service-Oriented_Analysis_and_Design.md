## Unit 4 - Service-Oriented Analysis and Design

Service-oriented analysis and design (SOAD) is a methodology that refers to the modeling and design for service-oriented architecture (SOA) applications. SOAD is a holistic modeling methodology that builds upon existing, well-disciplined and proven methodologies: object-oriented analysis and design (OOAD), enterprise architecture frameworks and business process modeling (BPM). SOAD also considers the following important concepts and aspects: service categorization and aggregation, policies and aspects, meet-in-the middle processes, semantic brokering, service harvesting and knowledge brokering.

The following diagram illustrates the basic architecture of a SOAD process:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Service        |    |  Service        |
|  Identification |    |  Specification  |    |  Realization    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Service        |    |  Service        |
|  Categorization |    |  Design         |    |  Implementation |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       V                      V                      V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Service        |    |  Service        |    |  Service        |
|  Aggregation    |    |  Testing        |    |  Deployment     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The SOAD process consists of three main phases: service identification, service specification and service realization. Each phase has sub-phases that involve different activities and artifacts. The SOAD process is iterative and incremental, meaning that it can be repeated and refined as needed. The SOAD process also supports the service lifecycle, which includes service design, service testing, service deployment and service management.

The SOAD process aims to achieve the following goals:

- Identify and model the business processes and requirements that can be fulfilled by services and microservices
- Specify the service contracts and interfaces that define the functionality and quality of service of each service and microservice
- Realize the service implementations and integrations that provide the service functionality and quality of service
- Ensure the service compatibility and interoperability across different platforms and technologies
- Ensure the service reusability and composability across different domains and applications
- Ensure the service scalability and reliability across different environments and scenarios
- Ensure the service security and governance across different policies and regulations