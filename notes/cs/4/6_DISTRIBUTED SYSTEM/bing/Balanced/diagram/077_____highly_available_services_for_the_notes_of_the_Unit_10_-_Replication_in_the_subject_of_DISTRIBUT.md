### Highly Available Services

- A highly available service is a service that can provide continuous and reliable operation despite failures or faults in the system.
- Replication is a technique for achieving high availability by creating and maintaining multiple copies of the same data or service on different nodes in a distributed system.
- Replication can improve availability by allowing the system to tolerate node failures, network partitions, or data corruption, as long as a sufficient number of replicas remain accessible and consistent.
- Replication can also improve performance by reducing the load on a single node, increasing the concurrency of operations, and reducing the latency of accessing data or service.
- Replication can be classified into two types: eager replication and lazy replication.
  - Eager replication ensures that all replicas are updated synchronously or atomically whenever a write operation occurs, thus providing strong consistency guarantees.
  - Lazy replication allows replicas to be updated asynchronously or periodically, thus providing weaker consistency guarantees but higher availability and scalability.
- Replication can be implemented at different levels of abstraction, such as data replication, process replication, or service replication.
  - Data replication involves replicating the state or content of a data object, such as a file, a record, or a table, across multiple nodes.
  - Process replication involves replicating the execution or behavior of a process, such as a server, a client, or a component, across multiple nodes.
  - Service replication involves replicating the functionality or interface of a service, such as a web service, a database service, or a messaging service, across multiple nodes.
- Replication can be managed by different protocols or algorithms, such as primary-backup, quorum-based, or consensus-based protocols.
  - Primary-backup protocols assign a primary replica to handle all write operations and propagate them to backup replicas, which handle read operations and take over the primary role in case of failure.
  - Quorum-based protocols require a minimum number of replicas, called a quorum, to agree on each write or read operation, thus ensuring consistency and availability.
  - Consensus-based protocols require all replicas to reach a common agreement on each write operation, thus ensuring strong consistency and fault tolerance.
- Replication can be challenged by various issues, such as replica consistency, replica synchronization, replica placement, replica selection, or replica recovery.
  - Replica consistency refers to the degree of agreement or divergence among replicas regarding the state or content of the data or service.
  - Replica synchronization refers to the process of updating or reconciling replicas to ensure consistency or convergence.
  - Replica placement refers to the decision of where to locate replicas in the network to optimize availability, performance, or cost.
  - Replica selection refers to the decision of which replica to access or update for a given operation to optimize availability, performance, or consistency.
  - Replica recovery refers to the process of restoring or repairing replicas after a failure or a fault to ensure availability and consistency.

: https://hevodata.com/learn/data-replication-in-distributed-system/
: https://techcommunity.microsoft.com/t5/sql-server-blog/replication-enhancement-8211-distribution-database-in/ba-p/385882
: https://raima.com/rdme-high-availability-database/
: https://link.springer.com/chapter/10.1007/978-3-7091-9198-9_4
: https://link.springer.com/article/10.1007/BF01762124
: https://dl.acm.org/doi/10.1145/138873.138877
: https://www.cs.cornell.edu/courses/cs5412/2012sp/lectures/lec25.pdf
: https://www.cs.cmu.edu/~dga/15-440/F10/lectures/15-replication.pdf