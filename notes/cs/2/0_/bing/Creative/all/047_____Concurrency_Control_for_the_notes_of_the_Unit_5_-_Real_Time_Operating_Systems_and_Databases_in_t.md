# Concurrency Control for the notes of the Unit 5 - Real Time Operating Systems and Databases in the subject of Real Time System

- Concurrency control is a procedure of managing simultaneous operations on a shared database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the respective database.
- Concurrency control is important for real-time database systems, which have to deal with both data consistency and timing constraints.
- A real-time database system must adapt to changes in the operating environment and guarantee the completion of critical transactions.
- Concurrency control in real-time database systems can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control prevents conflicts from occurring by locking data items before accessing them. Examples of pessimistic concurrency control are timestamp-based protocols and lock-based protocols.
- Optimistic concurrency control allows conflicts to occur and resolves them later by validating transactions before committing them. Examples of optimistic concurrency control are validation-based protocols and multiversion protocols.
- Concurrency control in real-time database systems can also be classified into two categories: centralized and distributed.
- Centralized concurrency control assumes that there is a single site that coordinates all the transactions and maintains the database. Centralized concurrency control is simpler and more efficient, but it has a single point of failure and a high communication overhead.
- Distributed concurrency control assumes that there are multiple sites that cooperate to execute transactions and maintain the database. Distributed concurrency control is more robust and scalable, but it has a higher complexity and a lower consistency.
- Concurrency control in real-time database systems should consider the following factors: transaction priority, deadline, data freshness, data availability, and system workload.
- Concurrency control in real-time database systems should balance the trade-off between performance and correctness. Performance refers to the ability to meet the timing constraints of transactions, while correctness refers to the ability to maintain the data consistency of the database.