 Here is the content in markdown format for the topic - ### Considerations for Service-oriented Applications:

### Considerations for Service-oriented Applications

Following are some key considerations for service-oriented applications:

1. Loose Coupling - Services should be loosely coupled so that they can be independently developed, deployed and managed without affecting other services. This makes the system flexible, robust and adaptable to changes.
2. Service Granularity - Services should be designed to the right level of granularity. Too fine-grained services may lead to excessive inter-service communication and latency while too coarse-grained services may lack functional cohesion. The granularity should strike a balance between these two extremes.
3. Service Autonomy - Services should be autonomous and encapsulate a business function or process. They should not expose internal implementations but only communicate via interfaces. This enables them to be reused and evolve independently.
4. Service Statelessness - Services should be stateless as far as possible to enable scaling, high availability and simplification of failover procedures. Any state information should be externalized as soon as possible.
5. Service discoverability - There should be mechanisms to discover available services and their interfaces at runtime. This enables loose coupling and dynamic systems where services can come and go.
6. Service Composition - There should be capabilities to compose multiple services into higher-level business processes and workflows to implement end-to-end functionality. This is typically done via service choreography or orchestration.
7. Service Governance - Appropriate governance should be in place to manage the service lifecycles, quality, security, organization policies, etc. This is especially important for enterprise-wide service-oriented systems with many services and teams.

Some mnemonics or learning tricks for the considerations could be:

- THINK LOOSE - for Loose Coupling, Service Granularity, Service Autonomy
- BE STATELESS - for Service Statelessness
- FIND ME - for Service Discoverability
- COMPOSE ME - for Service Composition
- GOVERN ME - for Service Governance

Hope this helps! Let me know if you would like me to elaborate on any of the points or include additional details.