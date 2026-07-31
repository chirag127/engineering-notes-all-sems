### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for increasing the availability of a service by creating and maintaining multiple copies of the service's data or state across different nodes in a distributed system.
- Replication can also improve the performance, scalability, and fault tolerance of a service by reducing the load on a single node, allowing parallel processing of requests, and masking failures of some nodes.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all replicas are updated synchronously whenever a write operation occurs, thus providing strong consistency and fault tolerance, but at the cost of higher latency and lower availability.
  - Lazy replication allows replicas to be updated asynchronously after a write operation, thus providing higher availability and lower latency, but at the cost of weaker consistency and possible conflicts.
- Replication can be implemented using various protocols, such as primary-backup, quorum-based, state machine, and epidemic protocols.
  - Primary-backup protocols assign a primary replica to handle all write operations and propagate them to backup replicas, thus ensuring consistency and fault tolerance, but introducing a single point of failure and performance bottleneck.
  - Quorum-based protocols require a minimum number of replicas (a quorum) to agree on each read and write operation, thus allowing trade-offs between consistency, availability, and performance, but increasing the complexity and overhead of coordination.
  - State machine protocols model the service as a deterministic state machine and use a consensus algorithm to ensure that all replicas execute the same sequence of commands, thus providing strong consistency and fault tolerance, but requiring reliable and ordered communication.
  - Epidemic protocols disseminate updates among replicas using a probabilistic gossip mechanism, thus providing high availability and scalability, but allowing temporary inconsistencies and conflicts.
- Replication can be applied to various types of services, such as databases, file systems, web servers, and distributed applications.
  - Databases can use replication to improve the availability and performance of data access, as well as to support disaster recovery and load balancing.
  - File systems can use replication to ensure the durability and reliability of file storage, as well as to support caching and offline access.
  - Web servers can use replication to handle the increasing demand and traffic of web applications, as well as to provide faster and more reliable service to users.
  - Distributed applications can use replication to enhance the functionality and quality of service of their components, such as messaging, coordination, and computation.