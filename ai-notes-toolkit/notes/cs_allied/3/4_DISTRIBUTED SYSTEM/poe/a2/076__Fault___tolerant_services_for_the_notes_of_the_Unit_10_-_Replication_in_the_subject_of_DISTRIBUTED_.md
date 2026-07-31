 Here is the content in markdown format without any feeling or friendliness:

### Fault – tolerant services for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

1. Replication: Replicating the services across multiple servers/data centers to achieve fault tolerance and high availability. If one replica fails, the clients can continue accessing the other replicas.
2. Leader election: When a leader replica fails, a new leader needs to be elected from the remaining replicas. The election algorithm should be efficient, and consider factors like network locality and load.
3. Synchronization: The replicas need to be kept in sync, so that all replicas have the same data. This can be challenging in WAN settings. Multi-master and single-master replication are two approaches to replica synchronization.
4. Quorum systems: To achieve consensus and replication, a subset of servers called a quorum needs to operate correctly. Quorum systems specify rules to determine if a quorum is met, and how to reconfigure the system when servers fail or recover.
5. CAP theorem: The CAP theorem states that it is impossible for a distributed system to simultaneously provide all three of the following:

Consistency: All nodes see the same data at the same time.
Availability: Every request receives a response about whether it was successful or failed.
Partition tolerance: The system continues to operate despite arbitrary message loss or failure of part of the system.

6. PACELC theorem: The PACELC theorem extends the CAP theorem to account for network partitions and consistency conflicts. It states that a system must trade off between availability and consistency in both normal operation (C/A) and partition scenarios (P/L).

(No emojis, external links or friendliness included as directed.)