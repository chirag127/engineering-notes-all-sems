### System model and group communication for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as communication, failures, synchronization, and consistency.
- Group communication is a technique that allows a process to communicate with multiple processes in a distributed system at the same time, using abstractions such as groups, multicast, and broadcast.
- Replication is a mechanism that creates and maintains multiple copies of the same data or service in a distributed system, for the purposes of fault tolerance, availability, scalability, and performance.
- System model and group communication are closely related to replication, as they affect the design and implementation of replication schemes, such as:
  - How to define and manage groups of replicas
  - How to ensure consistent and reliable communication among replicas
  - How to handle failures and network partitions
  - How to achieve different levels of consistency and concurrency control
- Some examples of replication schemes that rely on system model and group communication are:
  - Primary copy replication: All client requests are directed to a single primary server, which coordinates the updates to the replicas. This scheme requires a reliable and ordered communication channel, and cannot handle network partitions.
  - Available copies replication: Reads can be performed by any available replica, but writes must be performed by all available replicas. This scheme can handle some failures, but requires additional concurrency control procedures, such as local validation, to ensure one-copy serializability.
  - Quorum consensus replication: Reads and writes are performed by a subset of replicas, called a quorum, that satisfies some conditions, such as majority or intersection. This scheme can handle network partitions, but requires a voting protocol to determine the quorums.
  - Virtual partition replication: Replicas are dynamically partitioned into groups, called virtual partitions, that have exclusive access to a subset of data items. This scheme can handle network partitions and concurrency control, but requires a group membership protocol to form and maintain the virtual partitions.

- A possible mnemonic to remember the four replication schemes is: **P**rimary **A**vailable **Q**uorum **V**irtual (PAQV).
- A possible learning trick to understand the trade-offs among the replication schemes is to use a table that compares them based on the following criteria:

| Replication scheme | Communication cost | Availability | Consistency | Concurrency control |
|--------------------|--------------------|--------------|-------------|---------------------|
| Primary copy       | Low for reads, high for writes | Low, depends on primary | Strong, linearizable | Centralized, two-phase commit |
| Available copies   | Low for reads, high for writes | High, depends on majority | Weak, eventual | Distributed, local validation |
| Quorum consensus   | Variable, depends on quorum size | Variable, depends on quorum intersection | Variable, depends on quorum freshness | Distributed, voting protocol |
| Virtual partition  | Low for reads and writes | High, depends on partition size | Strong, serializable | Distributed, group membership |