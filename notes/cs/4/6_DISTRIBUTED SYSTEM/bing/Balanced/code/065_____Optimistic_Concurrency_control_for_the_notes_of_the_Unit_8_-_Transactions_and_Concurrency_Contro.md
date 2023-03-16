### Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not require locking or timestamping techniques.
- OCC consists of two or three phases: read, validation and write.
- In the read phase, a transaction reads the data from the database and performs its operations without any restrictions.
- In the validation phase, a transaction checks if it has any conflicts with other transactions that have committed since the read phase.
- A conflict occurs when two transactions access the same data item and at least one of them modifies it.
- If there are no conflicts, the transaction proceeds to the write phase, where it writes its updates to the database and commits.
- If there are conflicts, the transaction aborts and restarts from the beginning or from a checkpoint.
- OCC has the advantage of allowing high concurrency and avoiding deadlocks, as transactions do not hold any locks during their execution.
- OCC also reduces the communication overhead in distributed systems, as transactions do not need to coordinate with each other until the validation phase.
- OCC has the disadvantage of wasting resources and increasing latency, as transactions may have to abort and restart due to conflicts.
- OCC also requires a mechanism to detect and resolve conflicts, which can be challenging in distributed systems with partial failures and network delays.
- OCC is suitable for applications where conflicts are rare and transactions are short-lived, such as online shopping and social networking.
- OCC is not suitable for applications where conflicts are frequent and transactions are long-lived, such as banking and reservation systems.