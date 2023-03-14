### Dynamic voting protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Dynamic voting protocols are techniques for enforcing mutual exclusion and consistency in distributed systems that use replication of data or resources.
- The basic idea is to assign a number of votes to each node or copy of a data item, and require a quorum of votes to perform an operation on the data or resource.
- A quorum is the minimum number of votes that a distributed transaction has to obtain in order to be allowed to perform an operation in a distributed system.
- The quorum size and the vote distribution depend on the type of operation (read or write) and the desired properties of the system (availability, fault tolerance, consistency, etc.).
- Dynamic voting protocols allow the votes to be reassigned or adjusted upon node or link failures, in order to make the system more resilient and adaptable to changing conditions.
- Some examples of dynamic voting protocols are:

  - Protocols for dynamic vote reassignment , which allow nodes to select new vote values autonomously while still maintaining mutual exclusion requirements. These protocols are based on the concept of a safe set, which is a subset of nodes that can safely perform an operation without violating mutual exclusion.
  - Quorum-based voting for replica control , which uses different quorum sizes for read and write operations to ensure serializability and consistency of replicated data. These protocols are based on the concept of a version number, which is a timestamp that indicates the freshness of a data item.
  - A dynamic voting scheme in distributed systems , which uses a weighted voting scheme for consistency and recovery control of replicated files. These protocols are based on the concept of a generation number, which is a counter that indicates the number of updates performed on a file.

- Dynamic voting protocols have advantages and disadvantages compared to static voting protocols, which use fixed vote values and quorum sizes. Some of the advantages are:

  - Dynamic voting protocols can improve the availability and fault tolerance of the system by allowing operations to proceed even if some nodes or links fail or become partitioned.
  - Dynamic voting protocols can adapt to the changing workload and access patterns of the system by adjusting the vote values and quorum sizes accordingly.
  - Dynamic voting protocols can reduce the communication and synchronization overhead of the system by minimizing the number of nodes involved in an operation.

- Some of the disadvantages are:

  - Dynamic voting protocols can introduce complexity and overhead in the system by requiring additional mechanisms and algorithms to reassign or adjust the votes and quorums.
  - Dynamic voting protocols can increase the risk of inconsistency and deadlock in the system by allowing concurrent or conflicting operations to proceed under certain conditions.
  - Dynamic voting protocols can degrade the performance and scalability of the system by increasing the latency and contention of the operations.