### Service Run-time Governance

- Service run-time governance is a subset of service governance that focuses on the management and monitoring of service interactions at run time.
- Service run-time governance aims to ensure that the service-oriented architecture (SOA) system meets the quality of service (QoS) requirements, such as availability, performance, reliability, security, and scalability.
- Service run-time governance involves three main phases:
  - Policy definition: specifying the rules and expectations for the service behavior and interactions.
  - Policy enforcement: applying the policies to the service endpoints and intermediaries, such as service registries, service brokers, service proxies, and service gateways.
  - Policy execution: monitoring and auditing the service activities and outcomes, and taking corrective actions if needed.
- Service run-time governance can leverage the platform capabilities to provide agentless and transparent policy enforcement and execution.
- Service run-time governance can benefit from the following best practices :
  - Independent services: design and deploy services that are loosely coupled and self-contained, and avoid sharing data or dependencies with other services.
  - API gateway: use a centralized component that handles common run-time governance tasks, such as authentication, authorization, throttling, routing, caching, and logging.
  - Service discovery: enable services to dynamically register and discover each other, and use load balancing and failover mechanisms to ensure availability and performance.
  - Data management: adopt a polyglot persistence approach that allows each service to use the most suitable data store for its needs, and use event-driven architectures to synchronize data across services.