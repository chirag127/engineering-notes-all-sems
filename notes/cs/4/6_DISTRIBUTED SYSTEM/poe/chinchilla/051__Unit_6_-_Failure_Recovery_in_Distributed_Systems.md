## Unit 6 - Failure Recovery in Distributed Systems

In this unit, we will focus on the various methods and techniques employed in the recovery of distributed systems in the event of failures. The following are some key points to consider when studying this topic:

1. Fault Tolerance:
   - Fault tolerance is the ability of a system to continue functioning even when one or more components fail.
   - There are two basic approaches to achieving fault tolerance: redundancy and replication.
   - Redundancy involves having multiple copies of the same component, while replication involves creating multiple independent components that perform the same function.

2. Recovery Techniques:
   - Recovery techniques are used to bring a system back to a normal state after a failure has occurred.
   - The three main recovery techniques are checkpointing, rollback, and forward recovery.
   - Checkpointing involves periodically saving the state of the system to a stable storage medium.
   - Rollback involves restoring the system to a previous state before the failure occurred.
   - Forward recovery involves continuing the system's processing from the point of failure using a pre-defined recovery procedure.

3. Consistency and Coherency:
   - Consistency refers to the state of a distributed system where all nodes or replicas have the same data.
   - Coherency refers to the state of a distributed system where all nodes or replicas have the same data and are aware of each other's state.
   - Maintaining consistency and coherency is critical to ensuring the proper functioning of the system after a failure.

4. Replication:
   - Replication is the process of creating multiple copies of data or components to improve fault tolerance and scalability.
   - Replication can be implemented in several ways, including active replication, passive replication, and primary-backup replication.
   - Active replication involves replicating all requests to all replicas and requires a consensus algorithm to ensure consistency.
   - Passive replication involves replicating requests to a primary replica, which then replicates the requests to the other replicas.
   - Primary-backup replication involves designating one replica as the primary and the others as backups. The primary handles all requests, and the backups take over in the event of a failure.

5. Recovery Protocols:
   - Recovery protocols are used to coordinate the recovery process in distributed systems.
   - The two primary recovery protocols are 2PC (Two-Phase Commitment) and 3PC (Three-Phase Commitment).
   - 2PC involves a coordinator node that communicates with all participants to ensure that they agree on a decision before committing it.
   - 3PC is an extension of 2PC that adds an extra phase to handle cases where the coordinator fails.

In conclusion, understanding failure recovery in distributed systems is critical for ensuring the proper functioning of these systems. The techniques and methods discussed in this unit provide a solid foundation for building fault-tolerant and scalable distributed systems.