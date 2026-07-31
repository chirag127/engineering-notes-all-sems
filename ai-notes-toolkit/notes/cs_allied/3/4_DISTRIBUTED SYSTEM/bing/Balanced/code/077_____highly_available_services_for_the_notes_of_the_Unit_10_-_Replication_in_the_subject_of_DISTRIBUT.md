### Highly Available Services for the Notes of the Unit 10 - Replication in the Subject of Distributed System

- A highly available service is a service that can provide continuous and reliable operation despite the presence of failures in the system.
- Replication is a technique for increasing the availability of a service by creating and maintaining multiple copies of the service state or data across different nodes or locations in a distributed system.
- Replication can also improve the performance, scalability, and fault tolerance of a service by reducing the load on a single node, allowing concurrent access to different copies, and masking or recovering from failures.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all the copies are updated as soon as a change occurs in the service state or data. This provides strong consistency but incurs high communication and synchronization overhead.
  - Lazy replication allows some copies to be updated later than others, after a change occurs in the service state or data. This provides weak consistency but reduces the communication and synchronization overhead.
- Replication can also be classified into two modes: active replication and passive replication.
  - Active replication executes the same operations on all the copies in the same order, using a group communication or a consensus protocol. This provides fault tolerance by masking failures, but requires more resources and coordination.
  - Passive replication executes the operations on a primary copy and propagates the changes to the backup copies, using a logging or a checkpointing protocol. This provides fault tolerance by recovering from failures, but requires a failure detection and a leader election mechanism.
- Replication can also be classified into two levels: full replication and partial replication.
  - Full replication maintains the entire service state or data on all the copies, providing uniform access and high availability, but requiring more storage and bandwidth.
  - Partial replication maintains only a subset of the service state or data on each copy, providing differentiated access and lower availability, but requiring less storage and bandwidth.