### Highly available services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- Highly available services are those that can provide continuous and reliable access to data and functionality even in the presence of failures, network partitions, or high demand.
- Replication is a technique that involves creating and maintaining multiple copies of the same data or service on different nodes in a distributed system.
- Replication can improve the availability, performance, fault tolerance, and scalability of distributed services .
- Replication can be classified into two types: eager replication and lazy replication .
  - Eager replication: updates are propagated to all replicas as soon as they occur, ensuring strong consistency .
  - Lazy replication: updates are propagated to replicas only when needed, allowing temporary inconsistency .
- Replication can also be classified into two modes: active replication and passive replication .
  - Active replication: all replicas execute the same operations in the same order, ensuring that they have the same state .
  - Passive replication: one replica (called the primary) executes the operations and sends the results to the other replicas (called the backups) .
- Replication can be implemented at different levels of abstraction, such as data replication, service replication, or process replication .
  - Data replication: copies of the same data are stored on different nodes, such as in a distributed database .
  - Service replication: copies of the same service are provided by different nodes, such as in a load balancing system .
  - Process replication: copies of the same process are executed on different nodes, such as in a fault-tolerant system .
- Replication can be coordinated by different protocols, such as primary-backup protocol, quorum protocol, or gossip protocol .
  - Primary-backup protocol: one replica (the primary) is responsible for receiving and propagating updates to the other replicas (the backups) .
  - Quorum protocol: each replica needs to obtain a majority of votes from other replicas before performing an update or a read .
  - Gossip protocol: each replica randomly exchanges updates with other replicas in a probabilistic manner .
- Replication can have different trade-offs, such as consistency, availability, and partition tolerance (CAP theorem) .
  - Consistency: all replicas have the same view of the data at any given time .
  - Availability: all replicas can respond to requests at any given time .
  - Partition tolerance: the system can tolerate network failures that split the system into disjoint partitions .
  - According to the CAP theorem, it is impossible to achieve all three properties at the same time in a distributed system .
- Replication can have different challenges, such as concurrency control, conflict resolution, replica management, and security .
  - Concurrency control: ensuring that concurrent updates do not violate the integrity or consistency of the data .
  - Conflict resolution: resolving the discrepancies that may arise due to concurrent or delayed updates .
  - Replica management: creating, deleting, locating, and synchronizing replicas .
  - Security: protecting the data and the replicas from unauthorized access, modification, or deletion .

: https://hevodata.com/learn/data-replication-in-distributed-system/
: https://dl.acm.org/doi/10.1145/138873.138877
: https://raima.com/rdme-high-availability-database/
: https://link.springer.com/chapter/10.1007/978-3-7091-9198-9_4
: https://www.geeksforgeeks.org/what-is-replication-in-distributed-system/