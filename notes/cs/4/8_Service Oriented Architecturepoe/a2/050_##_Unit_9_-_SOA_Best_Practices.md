 Here is the content in markdown format for the topic ## Unit 9 - SOA Best Practices:

## Unit 9 - SOA Best Practices

1. Loose Coupling - Services should be loosely coupled, i.e. less dependent on each other. This makes them flexible, reusable and robust to changes.
2. Service Contract - Clearly define input and output for a service. This contract should be stable and not change frequently. This enables other services to use it without worrying about changes.
3. Service Granularity - A service should do one job and do it well. Do not overload a service with multiple functionalities. Split complex services into multiple simple and focused services.
4. Service Reusability - Services should be designed to be reusable. Similar functionalities should be abstracted into a common service rather than duplicating them. This reduces maintenance and promotes consistency.
5. Service Statelessness - Services should be stateless as much as possible. This makes them scalable and robust. State can be maintained externally using databases or caching.
6. Service Discovery - Services need to find and communicate with each other. Using a service registry and discovery mechanism enables services to locate dependent services dynamically.
7. Versioning - Services will evolve over time and proper versioning strategies should be employed to support backward compatibility or a complete cut off from previous versions.
8. Async Communication - Services should use asynchronous messaging rather than synchronous communication. This decouples them in time, makes them more resilient and scalable.
9. Idempotency - Services should be idempotent, i.e. repeating a request multiple times should not have any additional effect. This makes services more robust and easier to deal with in distributed environments.
10. Error Handling - Proper error handling and fault tolerance mechanisms should be in place to prevent failure of entire systems due to individual service failures. Timeouts, retries, Circuit breakers, etc. can be used.

[Detailed diagrams, examples and code snippets can be added here to further explain the concepts.]