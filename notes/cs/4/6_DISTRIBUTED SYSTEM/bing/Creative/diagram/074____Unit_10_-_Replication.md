## Unit 10 - Replication

Replication is the process of creating and maintaining multiple copies of the same data on different database servers. Replication can improve the availability, performance, and scalability of a database system.

Some benefits of replication are:

- Availability: Replication can provide fault tolerance and disaster recovery by allowing the system to continue functioning even if one or more servers fail or become inaccessible.
- Performance: Replication can reduce the load on the primary server by distributing read requests among multiple replicas. Replication can also reduce the network latency and bandwidth consumption by serving data from local replicas to geographically dispersed clients.
- Scalability: Replication can increase the capacity of the system by adding more replicas to handle more read requests. Replication can also enable horizontal partitioning or sharding, where different subsets of data are stored on different servers.

Some challenges of replication are:

- Consistency: Replication can introduce inconsistency among replicas if updates are not propagated or applied in the same order. Replication can also cause conflicts if concurrent updates are made to the same data on different replicas. Different replication strategies have different trade-offs between consistency and availability, such as synchronous versus asynchronous replication, and strong versus eventual consistency.
- Overhead: Replication can increase the complexity and cost of the system by requiring additional hardware, software, and network resources. Replication can also increase the workload on the primary server by requiring it to send updates to all replicas. Replication can also introduce additional latency and bandwidth consumption for update propagation.
- Management: Replication can require more administration and monitoring to ensure the health and synchronization of all replicas. Replication can also require more coordination and communication among replicas to handle failures, conflicts, and schema changes. Replication can also pose security and privacy risks if replicas are not properly protected or authorized.