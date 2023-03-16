### Concurrency Control

- Concurrency control is a database management systems (DBMS) concept that is used to address occur with a multi-user system.
- Concurrency control, when applied to a DBMS, is meant to coordinate simultaneous transactions while preserving data integrity.
- A transaction is a logical unit of work that accesses or modifies one or more data items in a database.
- A transaction is said to be successfully completed if and only if, it satisfies the ACID properties, namely, atomicity, consistency, isolation, and durability.
- A concurrent execution of a set of transactions is said to be serializable if and only if the database operations carried out by them is equivalent to some serial execution of these transactions.
- Serializability is a desirable property for concurrency control, as it ensures the correctness and consistency of the database state.

### Concurrency Control in Real-Time Database Systems

- A real-time database system (RTDBS) is a database system that supports applications with timing constraints, such as deadline, response time, and freshness.
- A real-time transaction is a transaction that has a deadline, which is the time by which it must be completed.
- A real-time transaction is said to be feasible if it can be completed within its deadline.
- A real-time transaction is said to be schedulable if it can be assigned a priority such that it is feasible under a given scheduling policy.
- A real-time transaction is said to be correct if it is both serializable and feasible.
- Concurrency control in RTDBS is about ensuring the correctness of real-time transactions by restricting concurrent transactions to be serializable and schedulable.
- Concurrency control in RTDBS faces many challenges, such as handling data conflicts, data freshness, data replication, data partitioning, and distributed transactions.
- Concurrency control in RTDBS can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control methods prevent data conflicts by locking data items before accessing them, and aborting transactions that violate the serializability or schedulability constraints.
- Optimistic concurrency control methods allow data conflicts to occur, but detect and resolve them at the end of transactions, by validating the serializability and schedulability constraints.
- Pessimistic concurrency control methods are suitable for applications with high data contention and low abort tolerance, while optimistic concurrency control methods are suitable for applications with low data contention and high abort tolerance.
- Some examples of pessimistic concurrency control methods for RTDBS are: priority inheritance protocol, priority ceiling protocol, two-phase locking protocol, and timestamp ordering protocol.
- Some examples of optimistic concurrency control methods for RTDBS are: optimistic concurrency control with backward validation, optimistic concurrency control with forward validation, and multiversion concurrency control.