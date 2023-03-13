### Optimistic Concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Optimistic concurrency control (OCC) is a method of managing concurrent access to shared data in a distributed system.
- OCC assumes that conflicts between transactions are rare and allows them to execute without locking or blocking any resources .
- OCC relies on validating the transactions at commit time to ensure that they do not violate any consistency rules .
- OCC has three phases: read phase, validation phase, and write phase  .
  - In the read phase, the transaction reads the data from the database and stores them in a local buffer. It also records the versions or timestamps of the data items that it reads  .
  - In the validation phase, the transaction checks if any of the data items that it read have been modified by another transaction that committed after it started. If so, the transaction is aborted and restarted. Otherwise, the transaction is allowed to proceed to the write phase  .
  - In the write phase, the transaction writes the updated data items to the database and commits  .
- OCC has several advantages over pessimistic concurrency control methods that use locking :
  - OCC reduces the overhead of locking and unlocking resources, which can improve the performance and scalability of the system .
  - OCC avoids deadlocks, since no transaction holds any locks while executing .
  - OCC allows more concurrency, since transactions can read and write data without blocking each other .
- OCC also has some disadvantages and limitations :
  - OCC may cause more aborts and restarts, especially if the conflict rate is high or the transactions are long-running .
  - OCC may not be suitable for applications that require strict serializability or isolation, since transactions may see inconsistent or stale data during the read phase .
  - OCC may not work well with distributed transactions that span multiple nodes or databases, since the validation phase may be complex and costly .
- OCC can be implemented using various techniques, such as timestamp ordering, version numbers, validation queries, or snapshot isolation   .
- OCC is widely used in many systems, such as relational database management systems, software transactional memory, and NoSQL databases   .