### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not require locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, otherwise it is committed.
- OCC has three phases: read, validation and write.
  - In the read phase, the transaction reads the data from the database and performs its operations, without acquiring any locks or checking any timestamps.
  - In the validation phase, the transaction checks if any of the data it has read or written has been modified by another concurrent transaction that has committed earlier.
  - In the write phase, the transaction writes its updates to the database, if the validation phase succeeds, otherwise it aborts and restarts.
- OCC is suitable for distributed systems, where locking or timestamping may incur high communication overhead or introduce delays.
- OCC can improve the performance and scalability of distributed transaction systems, by allowing more concurrency and reducing blocking and waiting .
- However, OCC may also incur high costs of validation and aborting, especially when the conflict rate is high or the transactions are long and complex .
- Therefore, OCC should be used carefully, depending on the characteristics of the workload and the system .

: https://en.wikipedia.org/wiki/Optimistic_concurrency_control
: https://people.cs.rutgers.edu/~pxk/417/notes/concurrency.html
: https://ieeexplore.ieee.org/document/77186/
: https://www.geeksforgeeks.org/concurrency-control-techniques/
: https://www.slideshare.net/mridulmishra2/optimistic-concurrency-control-in-distributed-systems