 Here is the content in markdown format for the topic ### SOA Strategy – Best Practices for the notes of the Unit 9 - SOA Best Practices in the subject of Service Oriented Architecture:

### SOA Strategy – Best Practices

1. Clearly define your Service boundaries: It is important to clearly define what functionality/business capability each service provides. This helps in avoiding overlapping functionality across services and prevents monolith like services. Some techniques for defining service boundaries are:
- Identify the key business capabilities/domains - Each capability/domain can map to a service
- Identify the key entities of the business - Each entity can translate to a service
- Look for the key verbs/actions on these entities - Each verb/action can indicate a separate service

2. Standardize service contracts: It is a good practice to standardize the service contracts (interfaces and schemas) across the enterprise to enable reuse and interoperability. Some recommendations:
- Define canonical data models/schemas using an industry standard format like XML or JSON.
- Define consistent service interface paradigms - Recommend REST APIs with consistent URI patterns and common operations (CRUD)
- Use an enterprise service bus to transform between different service contracts and enable mediation

3. Adopt service granularity principles: The granularity of services is important to get right. Fine-grained services lead to excessive service dependencies and chatty interactions while coarse-grained services may contain unrelated functionality. Some key principles to follow:
- The Single Responsibility Principle - Services should have single well-defined responsibilities
- The Common Closure Principle - Services should be structured around common changes in requirements
- The Common Reuse Principle - Services should be structured around common reuse scenarios

4. Choose the right communication protocols: The communication protocols/mechanisms chosen for service interaction have a significant impact on service characteristics like latency, scalability, extensibility, etc. Some recommendations:
- Use asynchronous messaging for asynchronous and decoupled communication
- Use REST over HTTP for synchronous request-response style interactions
- Use web sockets for real-time bi-directional communication
- Ensure the protocols can work over the enterprise network, security constraints, etc.

5. Design for resiliency and fault-tolerance: Services in an SOA need to be resilient and fault-tolerant to handle errors, latency variations, and failures. Some recommended practices:
- Design services to fail fast and fail gracefully
- Include retry logic and timeouts to handle transient failures
- Include circuit breakers to prevent cascading failures
- Include fallback and degradation options for dependent services
- Include logging and monitoring to detect and diagnose issues