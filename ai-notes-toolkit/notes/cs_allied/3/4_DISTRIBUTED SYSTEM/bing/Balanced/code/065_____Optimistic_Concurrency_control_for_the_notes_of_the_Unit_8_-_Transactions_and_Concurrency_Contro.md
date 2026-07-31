### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to check if any conflicts occurred with other transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads data from the database and performs computations, but does not write anything to the database.
  - In the validation phase, the transaction checks if any of the data it read has been modified by another transaction that committed after it started.
  - In the write phase, the transaction writes its updates to the database, if the validation phase was successful.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or limit scalability.
- OCC can improve performance and concurrency in distributed systems, especially when conflicts are rare or when transactions are short-lived .
- However, OCC may also cause high abort rates and wasted work, if conflicts are frequent or if transactions are long-lived .
- OCC can be implemented using various techniques, such as version numbers, timestamps, validation queries, or certification  .
- OCC requires a mechanism to detect and resolve conflicts, such as serializability, snapshot isolation, or causal consistency  .