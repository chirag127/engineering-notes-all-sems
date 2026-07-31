# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If so, the transaction is aborted and restarted, otherwise it proceeds to the write phase.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has some advantages over locking-based concurrency control techniques, such as:
  - It avoids the overhead of acquiring and releasing locks, which can improve the performance of the system.
  - It avoids the problem of deadlock, which can occur when two or more transactions are waiting for each other to release locks.
  - It allows more concurrency, as transactions can read and write data items without blocking each other.
- OCC also has some disadvantages, such as:
  - It may cause more aborts and restarts, especially when the contention for data items is high.
  - It may require more storage space, as transactions need to keep copies of the data items they have read and modified.
  - It may require more communication, as transactions need to validate their read sets with the database or other transactions.
- OCC is suitable for distributed systems, where locking-based techniques may be impractical or inefficient due to the network latency and the possibility of node failures.
- OCC can be implemented in different ways, such as using timestamps, versions, or validation protocols . The choice of the implementation depends on the characteristics of the system and the application .