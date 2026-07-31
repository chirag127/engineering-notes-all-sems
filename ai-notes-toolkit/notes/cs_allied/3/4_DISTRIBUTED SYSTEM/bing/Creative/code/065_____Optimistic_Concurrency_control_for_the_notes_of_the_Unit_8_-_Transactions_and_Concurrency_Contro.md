### Optimistic Concurrency Control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and therefore does not require locking or timestamping techniques to prevent conflicts .
- Instead, OCC allows transactions to execute without restrictions until they are committed, and then validates them to ensure that no conflicts have occurred.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of repeated conflicts .
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or checking any timestamps.
  - In the validation phase, the transaction checks if any of the data it has read or written has been modified by another transaction that committed earlier. This can be done by comparing the versions or timestamps of the data items, or by using a validation server that keeps track of the committed transactions .
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database and commits. Otherwise, the transaction aborts and restarts.
- OCC has some advantages and disadvantages compared to other concurrency control methods  :
  - Advantages:
    - OCC avoids locking overhead and deadlock problems, as transactions do not block each other or hold any resources .
    - OCC allows more concurrency and throughput, as transactions can execute in parallel without waiting for locks or timestamps .
    - OCC is suitable for distributed systems, where locking or timestamping may be costly or impractical due to network delays or failures  .
  - Disadvantages:
    - OCC may incur more aborts and restarts, especially when the data contention is high or the transactions are long .
    - OCC may waste more resources and computation, as transactions may perform unnecessary work before being aborted .
    - OCC may have lower consistency and freshness, as transactions may read stale or uncommitted data .