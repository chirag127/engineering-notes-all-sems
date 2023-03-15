 Here is the content in markdown format for the topic ### Transactions with replicated data for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM:

## Transactions with replicated data

- When data is replicated across multiple servers, transactions that access and update the data become challenging to handle.
- The key issues are:

1. Ensuring transaction atomicity: Either all updates from a transaction must be reflected on all replicas, or none at all.
2. Maintaining consistency: All replicas must have the same data value for any given item after a transaction completes.
3. Handling failures: The system must ensure that transactions complete even in the face of server and network failures.

- Two common approaches for handling transactions with replicated data:

1. Primary-backup approach: One replica (the primary) handles all writes. Updates are then sent to backups. If the primary fails, a backup is promoted. Simple but can result in loss of updates if the primary fails.
2. Multi-master replication: Allow writes at multiple replicas. Use a concurrency control mechanism to handle conflicting writes. Can improve availability and performance but significantly more complex to implement.

- Mnemonics: Think CAP theorem - you can't have consistency, availability, and partition tolerance all at once. There are tradeoffs in replicated systems.
- Learning tricks: Draw diagrams showing replicas, clients, and flows of updates/transactions. Think through failure scenarios to understand limitations of different approaches.

- Advantages: Increased availability, scalability, and performance.
- Disadvantages: Complexity of implementation, risk of inconsistency or lost updates, "split brain" problem if network is partitioned.
- Applications: Database replication, distributed file systems, load balancing, cloud computing.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.