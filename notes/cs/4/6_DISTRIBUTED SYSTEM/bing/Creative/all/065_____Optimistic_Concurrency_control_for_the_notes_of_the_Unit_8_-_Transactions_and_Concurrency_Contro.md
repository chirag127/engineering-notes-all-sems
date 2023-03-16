# Optimistic Concurrency Control

- Optimistic concurrency control (OCC) is a concurrency control method applied to transactional systems such as relational database management systems and software transactional memory.
- OCC assumes that multiple transactions can frequently complete without interfering with each other, and does not require locking or timestamping techniques to prevent conflicts .
- Instead, a transaction is executed without restrictions until it is committed, and then it is validated to ensure that no conflicts have occurred with other concurrent transactions.
- If a conflict is detected, the transaction is aborted and restarted, possibly with some backoff or priority adjustment mechanism to reduce the likelihood of further conflicts .
- OCC has the advantage of allowing a high degree of concurrency and avoiding the overhead of locking or timestamping, but it also has the drawback of wasting resources and increasing latency when conflicts are frequent and transactions have to be restarted .
- OCC can be implemented in a centralized or distributed manner, depending on the architecture of the transactional system .
- In a centralized system, there is a single validation server that checks the read and write sets of each transaction and decides whether to commit or abort it.
- In a distributed system, there are multiple validation servers that communicate with each other to detect and resolve conflicts among transactions that access data stored in different sites.
- OCC can be further classified into different variants based on the validation phase, such as basic OCC, forward validation, backward validation, and hybrid validation.
- Each variant has different trade-offs in terms of concurrency, complexity, and performance.