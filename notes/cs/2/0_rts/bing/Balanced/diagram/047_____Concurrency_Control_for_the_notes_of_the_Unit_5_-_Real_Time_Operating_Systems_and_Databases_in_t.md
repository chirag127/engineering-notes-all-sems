### Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic concurrency control are two-phase locking, timestamp ordering, and priority inheritance protocols.
  - Optimistic concurrency control allows conflicts to occur and then resolves them by aborting or restarting the conflicting transactions. Examples of optimistic concurrency control are optimistic concurrency control with backward validation, optimistic concurrency control with forward validation, and multiversion concurrency control.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as the performance criteria, the assumptions, and the goals of different classes of RTS .
  - Performance criteria: RTS are more concerned with meeting deadlines and minimizing response time than maximizing throughput and minimizing abort rate.
  - Assumptions: RTS often have predictable workloads, periodic transactions, and static data, while database systems often have unpredictable workloads, non-periodic transactions, and dynamic data.
  - Goals: RTS often aim to achieve predictability, schedulability, and feasibility, while database systems often aim to achieve serializability, recoverability, and consistency.
- Concurrency control techniques for RTS should consider the following factors:
  - The correctness criteria for the transactions, such as serializability, linearizability, or precedence graph correctness.
  - The priority assignment for the transactions, such as fixed priority, dynamic priority, or earliest deadline first.
  - The synchronization mechanism for the transactions, such as blocking, non-blocking, or wait-free.
  - The conflict resolution policy for the transactions, such as abort, restart, or compensation.
  - The data replication strategy for the transactions, such as primary copy, majority voting, or quorum consensus.
- Concurrency control techniques for RTS should also be compatible with the scheduling algorithms and the communication protocols used in the system.