### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for creating and maintaining multiple copies of data or processes across different nodes in a distributed system.
- Replication can enhance the availability, performance, scalability, and fault tolerance of a service by reducing the dependency on a single point of failure or a single source of data.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all the replicas are updated synchronously whenever a change occurs in the data or the process. This guarantees strong consistency and high availability, but at the cost of increased latency and reduced scalability.
  - Lazy replication allows the replicas to be updated asynchronously after a change occurs in the data or the process. This improves the latency and scalability of the system, but may result in weak consistency and temporary unavailability.
- Replication can also be classified into two modes: active replication and passive replication.
  - Active replication involves executing the same request on all the replicas simultaneously and returning the same result to the client. This ensures that the replicas are always consistent and can tolerate any number of failures, as long as one replica remains alive.
  - Passive replication involves executing the request on a primary replica and propagating the updates to the backup replicas. This reduces the overhead of executing the same request multiple times, but requires a mechanism to elect a new primary in case of a failure.
- Replication can be implemented at different levels of abstraction, such as the application level, the middleware level, or the database level.
  - Application level replication involves designing the application logic to handle replication and consistency issues. This gives the application developer more control and flexibility, but also more complexity and responsibility.
  - Middleware level replication involves using a software layer that provides replication and consistency services to the application. This simplifies the application development and hides the replication details, but also introduces some performance and compatibility overhead.
  - Database level replication involves using a database management system that supports replication and consistency features. This enables the application to use a standard database interface and benefit from the database functionality, but also limits the replication options and policies to those supported by the database system.