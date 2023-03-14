 Here is the content in markdown format for the topic ### SOA Development – Best Practices for the notes of the Unit 9 - SOA Best Practices in the subject of Service Oriented Architecture:

### SOA Development – Best Practices

1. Loose Coupling - Services should be loosely coupled so that they can be developed, deployed and scaled independently. This ensures high reusability and fault tolerance.
2. Service Contracts - Services should have explicit service contracts defined that include information such as operations, input and output messages, pre-conditions, post-conditions, etc. This ensures proper communication and compatibility between services.
3. Shared Schemas - Services should share common data types and schemas whenever possible to reduce complexity and facilitate integration.
4. Service Versioning - Services should follow a versioning strategy that allows multiple versions to co-exist and clients to use newer service versions without breaking existing compatibility. This enables continuous improvement of services.
5. Service Granularity - Services should exhibit the right level of granularity such that they are not too big or too small. Large services reduce reusability while too many fine-grained services introduce complexity.
6. Service Autonomy - Services should be designed to be as autonomous as possible such that they can be developed and managed independently. This increases scalability and reduces bottlenecks.
7. Service Statelessness - Services should be stateless wherever possible such that request processing does not depend on the previous request state. This enhances scalability by allowing request to be load-balanced and served by multiple service instances.
8. Service Composability - Services should be designed to be composable so that they can be used in conjunction with other services to build more complex applications and processes. This increases reusability.
9. Well-defined Interfaces - Services should have well-defined, technology-agnostic interfaces that mask the underlying implementation details. This increases portability across different platforms and systems.
10. Service Discovery - There should be a service discovery mechanism in place for client applications to locate available service instances dynamically. This enhances fault tolerance by routing requests to available service instances.

The above points cover some of the key best practices to follow for SOA development. Adhering to these best practices leads to a robust, scalable and maintainable SOA solution. Let me know if you would like me to elaborate on any of the points or include additional details.