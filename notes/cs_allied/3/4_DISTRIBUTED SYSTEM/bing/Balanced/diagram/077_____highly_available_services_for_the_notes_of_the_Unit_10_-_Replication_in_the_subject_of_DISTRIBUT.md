### Highly Available Services

- A highly available service is a service that can provide continuous and reliable operation even in the presence of failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system .
- Replication can improve the availability, performance, scalability, and fault tolerance of a service .
- Replication can be classified into two types: eager replication and lazy replication .
  - Eager replication ensures that all replicas are updated as soon as a change occurs, thus providing strong consistency and fault tolerance, but at the cost of higher communication and synchronization overhead .
  - Lazy replication allows some replicas to be updated later than others, thus providing higher availability and performance, but at the cost of weaker consistency and possible conflicts .
- Replication can also be classified into two modes: active replication and passive replication .
  - Active replication executes the same request on all replicas in parallel, thus providing high availability and fault masking, but at the cost of higher resource consumption and possible non-determinism .
  - Passive replication executes the request on a primary replica and propagates the result to the backup replicas, thus providing lower resource consumption and deterministic behavior, but at the cost of lower availability and fault detection .
- Replication can be implemented at different levels of abstraction, such as data replication, process replication, or service replication.
  - Data replication focuses on replicating the state of the data objects, such as files, databases, or memory pages .
  - Process replication focuses on replicating the behavior of the application processes, such as servers, clients, or threads .
  - Service replication focuses on replicating the functionality of the service, such as web services, message queues, or distributed transactions .