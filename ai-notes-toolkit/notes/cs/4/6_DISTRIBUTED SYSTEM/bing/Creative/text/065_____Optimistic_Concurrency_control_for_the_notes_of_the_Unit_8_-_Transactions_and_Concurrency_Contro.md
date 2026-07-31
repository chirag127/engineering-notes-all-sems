### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or updating the database.
  - In the validation phase, the transaction checks if any other transaction has modified the data that it has read or written, using some validation rules.
  - In the write phase, if the validation succeeds, the transaction writes its updates to the database, otherwise it aborts and restarts.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or introduce delays.
- OCC can improve the performance and scalability of distributed transaction systems, by allowing more concurrency and reducing blocking and waiting .
- However, OCC may also incur high costs of aborting and restarting transactions, especially if the conflict rate is high or the transactions are long and complex .
- Therefore, OCC should be used carefully, depending on the characteristics of the workload and the system .