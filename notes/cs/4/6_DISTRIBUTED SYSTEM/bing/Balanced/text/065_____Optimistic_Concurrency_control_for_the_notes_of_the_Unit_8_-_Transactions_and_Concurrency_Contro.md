### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or updating the database.
  - In the validation phase, the transaction checks if any other transaction has modified the data that it has read or written, using some validation rules.
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database, otherwise it aborts and restarts.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or limit the scalability of the system.
- OCC can improve the performance and throughput of the system, as transactions can execute concurrently without blocking or waiting for each other.
- However, OCC may also increase the abort rate and the response time of the system, as transactions may have to restart multiple times due to conflicts.
- To reduce the number of restarts, some OCC protocols use locking or timestamping techniques to guarantee a successful second execution for a failed transaction.