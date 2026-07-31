# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency is the tendency for things to happen at the same time in a system.
- Concurrency is a natural phenomenon in the real world, and many real-time systems (RTS) are inherently concurrent and typically manage shared data resources.
- Concurrency control is the process of ensuring that concurrent access to shared data does not result in inconsistency or violation of timing constraints.
- Concurrency control is essential for both logical and timing correctness of RTS.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control techniques prevent conflicts from occurring by locking or reserving the shared data before accessing it. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and priority inheritance protocols.
  - Optimistic concurrency control techniques allow conflicts to occur and then resolve them by aborting or restarting the conflicting transactions. Examples of optimistic techniques are optimistic concurrency control, multiversion concurrency control, and snapshot isolation.
- Concurrency control techniques for RTS differ from those for database systems in several aspects, such as performance considerations, timing constraints, correctness criteria, and transaction models.
  - Performance considerations: RTS require fast response time, low overhead, and high throughput, while database systems focus on data consistency, durability, and recovery.
  - Timing constraints: RTS have deadlines and temporal validity of data, while database systems have no explicit time requirements.
  - Correctness criteria: RTS have to satisfy both logical and timing correctness, while database systems only need to ensure logical correctness. Logical correctness means that the concurrent execution of transactions preserves the consistency of the database. Timing correctness means that the transactions meet their deadlines and access temporally valid data.
  - Transaction models: RTS have different types of transactions, such as hard, soft, and firm, with different characteristics and requirements, while database systems have a uniform transaction model based on the ACID properties (atomicity, consistency, isolation, and durability).
- Concurrency control techniques for RTS have to balance the trade-off between concurrency and correctness, and adapt to the dynamic and unpredictable nature of the real-time environment.
- Concurrency control techniques for RTS have to consider various factors, such as the priority of transactions, the temporal validity of data, the deadline of transactions, the abort rate of transactions, the blocking time of transactions, and the resource utilization.
- Concurrency control techniques for RTS have to be evaluated based on various metrics, such as the number of transactions completed, the number of transactions missed their deadlines, the number of transactions aborted, the response time of transactions, the overhead of concurrency control, and the throughput of the system.