### Optimistic Concurrency Control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and avoids locking of data items that can reduce the performance of the system.
- OCC consists of three phases: read, validation and write.
  - In the read phase, the transaction reads the data items from the database and performs the necessary computations, but does not update the database.
  - In the validation phase, the transaction checks if any of the data items it has read have been modified by other transactions that committed after it started. If there is no conflict, the transaction can proceed to the write phase. Otherwise, the transaction is aborted and restarted.
  - In the write phase, the transaction updates the database with the new values of the data items it has modified.
- OCC has several advantages over locking-based concurrency control techniques:
  - It allows more concurrency, as transactions do not block each other by holding locks on data items.
  - It avoids deadlock, as transactions do not wait for locks to be released by other transactions.
  - It reduces the overhead of lock management, as transactions do not need to acquire and release locks on data items.
- OCC also has some disadvantages and challenges:
  - It may cause more aborts and restarts, as transactions may conflict with each other at the validation phase.
  - It may increase the complexity of the system, as transactions need to keep track of the data items they have read and modified, and the system needs to implement a validation mechanism.
  - It may not be suitable for applications that have high contention or low data availability, as transactions may have a low probability of passing the validation phase.
- OCC can be implemented in different ways, depending on how the validation phase is performed and how the data items are versioned:
  - Centralized OCC: The validation phase is performed by a central validator that maintains a global order of transactions and checks for conflicts among them.
  - Distributed OCC: The validation phase is performed by the transactions themselves, by contacting the sites that store the data items they have read or modified and checking for conflicts with other transactions.
  - Timestamp-based OCC: The data items are versioned by timestamps that indicate when they were last updated, and the transactions are assigned timestamps that indicate when they started. The validation phase is performed by comparing the timestamps of the data items and the transactions, and ensuring that the transactions have read the latest versions of the data items.