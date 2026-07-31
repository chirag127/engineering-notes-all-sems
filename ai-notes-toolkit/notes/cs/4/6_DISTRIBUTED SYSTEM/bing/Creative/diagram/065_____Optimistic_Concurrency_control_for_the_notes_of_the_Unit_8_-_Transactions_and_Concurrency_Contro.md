### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has several advantages over locking-based concurrency control techniques, such as:
  - It allows more concurrency, as transactions do not block each other by holding locks.
  - It avoids deadlock, as transactions do not wait for locks to be released.
  - It reduces the overhead of lock management, as transactions do not need to acquire and release locks.
- OCC also has some disadvantages, such as:
  - It may cause more aborts and restarts, as transactions may conflict with each other at the validation phase.
  - It may increase the response time, as transactions have to perform the validation phase before committing.
  - It may not be suitable for applications that have high contention, as transactions are more likely to fail the validation phase.
- OCC can be implemented in distributed systems, where transactions may access data items stored in different nodes of the network.
  - One approach is to use a centralized validator, which collects the read and write sets of all transactions and performs the validation phase for them.
  - Another approach is to use a distributed validator, which partitions the data items among the nodes and performs the validation phase locally for each partition.
  - Both approaches have their trade-offs in terms of communication cost, scalability and fault tolerance.