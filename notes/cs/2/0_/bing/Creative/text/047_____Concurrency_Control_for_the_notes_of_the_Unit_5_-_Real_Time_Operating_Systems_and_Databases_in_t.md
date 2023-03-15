### Concurrency Control

- Concurrency control is a procedure of managing simultaneous operations on a database without conflicting with each other.
- Concurrency control ensures that database transactions are performed concurrently and accurately to produce correct results without violating data integrity of the database.
- Concurrency control is especially important for real-time database systems, where transactions have timing constraints and must be completed before their deadlines.
- Concurrency control in real-time database systems should consider both data consistency and timing constraints, and also adapt to changes in the operating environment and guarantee the completion of critical transactions.

### Concurrency Control Methods

- There are two main methods of concurrency control: locking-based and timestamp-based.
- Locking-based methods use locks to prevent concurrent transactions from accessing the same data item in conflicting modes (read or write). A lock is a mechanism that grants exclusive access to a data item to a transaction that requests it. Locks can be shared (for read-only access) or exclusive (for read or write access). Locks can also be applied at different levels of granularity, such as records, pages, tables, or databases.
- Timestamp-based methods use timestamps to order the transactions and ensure serializability. A timestamp is a unique identifier that reflects the start time or the priority of a transaction. Timestamps can be assigned by the system or by the application. Timestamps can be used to determine the precedence of transactions and resolve conflicts by aborting or delaying the transactions with later timestamps.
- Locking-based and timestamp-based methods have different advantages and disadvantages. Locking-based methods can avoid unnecessary aborts and ensure deadlock-freedom, but they may incur high overhead and blocking. Timestamp-based methods can avoid blocking and reduce overhead, but they may cause unnecessary aborts and starvation.

### Concurrency Control Protocols

- A concurrency control protocol is a set of rules that govern how transactions access and manipulate data items in a database. A concurrency control protocol should ensure serializability, which means that the concurrent execution of a set of transactions is equivalent to some serial execution of these transactions.
- There are many concurrency control protocols that have been proposed for real-time database systems, such as:
  - Two-phase locking (2PL): a locking-based protocol that requires a transaction to acquire all the locks it needs before releasing any lock. 2PL ensures serializability, but it may cause deadlocks, blocking, and priority inversion.
  - Timestamp ordering (TO): a timestamp-based protocol that orders the transactions according to their timestamps and ensures that the transactions access the data items in the same order. TO ensures serializability, but it may cause aborts, starvation, and inconsistency.
  - Optimistic concurrency control (OCC): a timestamp-based protocol that allows transactions to execute without locking and validates them at the end using their timestamps. OCC avoids blocking and reduces overhead, but it may cause aborts and inconsistency.
  - Priority ceiling protocol (PCP): a locking-based protocol that assigns a priority ceiling to each data item and prevents a transaction from locking a data item if its priority is lower than the ceiling. PCP ensures serializability, deadlock-freedom, and priority inheritance, but it may cause blocking and overhead.
  - High priority two-phase locking (HP-2PL): a locking-based protocol that allows high priority transactions to preempt low priority transactions and abort them if they hold conflicting locks. HP-2PL ensures serializability and timeliness, but it may cause aborts, starvation, and inconsistency.
  - Earliest deadline first concurrency control (EDF-CC): a timestamp-based protocol that assigns deadlines to transactions and orders them according to their deadlines. EDF-CC ensures serializability and timeliness, but it may cause aborts, starvation, and inconsistency.
  - Real-time optimistic concurrency control (RT-OCC): a timestamp-based protocol that combines OCC with EDF-CC and validates transactions according to their deadlines. RT-OCC avoids blocking and reduces overhead, but it may cause aborts and inconsistency.