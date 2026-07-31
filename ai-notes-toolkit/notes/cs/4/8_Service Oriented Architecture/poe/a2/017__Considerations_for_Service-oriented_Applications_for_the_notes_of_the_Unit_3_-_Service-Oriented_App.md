 Here are the points I have noted for the given topic:

### Considerations for Service-oriented Applications

1. Service Granularity - Services should be coarse-grained and perform distinct and meaningful tasks. Fine-grained services lead to excessive service interactions and affect performance.
2. Service Autonomy - Services should be autonomous and loosely-coupled. They should not depend on the internal implementation of other services. This enables service reuse and parallel development.
3. Service Statelessness - Services should be stateless as far as possible. This allows for scalability and fault-tolerance since client state can be maintained externally. Stateful services limit scalability and fault-tolerance.
4. Service Discovery - There must be a service registry/directory to enable services to discover and interact with other services dynamically. This decouples service consumers from service providers.
5. Service Versioning - Services will evolve over time and hence a robust service versioning strategy is essential. Both backwards and forwards compatibility must be handled effectively to avoid versioning issues.
6. Service Security - Services must implement necessary security measures like authentication, authorization, confidentiality, integrity, accountability, etc. to ensure secure service interactions and data protection.
7. Service Monitoring - Services must be effectively monitored for performance metrics, errors, and other operational issues. This requires logging, reporting, alerting, and other monitoring capabilities for each service.
8. Service Documentation - Services must be well-documented to enable proper understanding and usage. This includes documentation of service APIs, non-functional aspects, dependencies, etc.
9. Service Reliability and Quality of Service - Services must meet necessary reliability and quality of service requirements like high availability, fault-tolerance, throughput, latency, etc. Appropriate architectural and operational practices must be employed to achieve this.