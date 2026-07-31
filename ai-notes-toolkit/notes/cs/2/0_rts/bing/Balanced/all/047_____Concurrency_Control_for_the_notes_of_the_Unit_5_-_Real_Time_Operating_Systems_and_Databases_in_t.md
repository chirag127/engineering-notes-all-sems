# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control techniques prevent conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and priority inheritance protocols.
  - Optimistic concurrency control techniques allow conflicts to occur and then resolve them by aborting or restarting the conflicting transactions. Examples of optimistic techniques are optimistic concurrency control, multiversion concurrency control, and wait-free synchronization.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as the performance criteria, the transaction model, the scheduling policy, the failure handling, and the correctness criteria.
  - Performance criteria: RTS are concerned with meeting deadlines and minimizing response time, while database systems are concerned with maximizing throughput and minimizing blocking time.
  - Transaction model: RTS transactions are often periodic, preemptive, and have different types of operations (such as read, write, and control), while database transactions are often sporadic, non-preemptive, and have only read and write operations.
  - Scheduling policy: RTS transactions are often scheduled by fixed or dynamic priority algorithms, while database transactions are often scheduled by first-come-first-served or round-robin algorithms.
  - Failure handling: RTS transactions are often required to complete within a deadline, and aborting or restarting them may not be feasible or desirable, while database transactions can be aborted or restarted without affecting the system functionality.
  - Correctness criteria: RTS transactions are required to satisfy both logical and temporal correctness, while database transactions are required to satisfy only logical correctness.
- Logical correctness of RTS transactions is usually defined by serializability, which means that the concurrent execution of transactions is equivalent to some serial execution of the same transactions.
- Temporal correctness of RTS transactions is usually defined by timeliness, which means that the transactions meet their deadlines and do not cause deadline misses of other transactions.
- There are different types of serializability and timeliness criteria for RTS transactions, depending on the assumptions and goals of different classes of RTS.
  - Serializability criteria: linearizability, sequential consistency, causal consistency, and eventual consistency.
  - Timeliness criteria: hard, firm, and soft deadlines.