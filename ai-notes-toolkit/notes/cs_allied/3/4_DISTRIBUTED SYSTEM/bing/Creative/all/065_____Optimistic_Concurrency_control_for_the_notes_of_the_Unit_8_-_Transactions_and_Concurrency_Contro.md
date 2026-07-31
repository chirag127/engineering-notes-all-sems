# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not use locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of further conflicts .
- OCC has the advantage of allowing a high degree of concurrency and avoiding the overhead of locking or timestamping, but it also has the drawback of wasting resources and increasing latency when conflicts are frequent and transactions have to be restarted .
- OCC can be implemented in a centralized or distributed system, depending on where the validation and commit phases are performed .
- In a centralized system, there is a single validator that checks all the transactions before they are committed, and a single commit log that records the committed transactions.
- In a distributed system, there may be multiple validators and commit logs, each responsible for a subset of the data or transactions, and they may communicate with each other to ensure global consistency.
- A distributed OCC protocol may have different design choices, such as whether to use two-phase commit, how to handle network failures, how to acquire locks for the second execution, and how to optimize the validation and commit phases.
- A distributed OCC protocol should aim to minimize the number of restarts, the communication overhead, and the commit latency, while ensuring correctness and consistency of the transactions.