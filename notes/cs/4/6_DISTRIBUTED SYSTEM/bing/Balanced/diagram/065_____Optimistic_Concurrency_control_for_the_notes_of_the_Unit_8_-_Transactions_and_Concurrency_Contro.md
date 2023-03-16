### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
- In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
- In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
- In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has the advantage of allowing a high degree of concurrency and avoiding deadlocks, but it may incur a high cost of aborting and restarting transactions if conflicts are frequent.
- OCC can be implemented in a centralized or distributed manner, depending on the architecture of the system.
- In a centralized system, there is a single validation server that maintains the versions of the data items and validates the transactions before they commit.
- In a distributed system, there are multiple validation servers that communicate with each other to ensure the consistency of the data items and the correctness of the transactions.
- A distributed OCC protocol may use different strategies to reduce the number of restarts, such as acquiring locks, using timestamps, or applying voting mechanisms.