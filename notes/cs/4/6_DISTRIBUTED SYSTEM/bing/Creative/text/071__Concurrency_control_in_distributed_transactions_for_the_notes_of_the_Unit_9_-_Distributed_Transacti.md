### Concurrency control in distributed transactions

- Concurrency control is the process of managing concurrent access to shared data in a distributed system, such that the consistency and isolation properties of transactions are preserved.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control assumes that conflicts are likely to occur and prevents them by locking the data items accessed by a transaction until it commits or aborts. Examples of pessimistic concurrency control are two-phase locking (2PL) and timestamp ordering (TO).
- Optimistic concurrency control assumes that conflicts are rare and allows transactions to execute without locking, but validates them before committing. If a conflict is detected, the transaction is aborted and restarted. Examples of optimistic concurrency control are validation-based protocols and multiversion concurrency control (MVCC).
- Concurrency control in distributed transactions faces additional challenges, such as:
  - Network delays and failures, which may cause transactions to wait indefinitely for locks or messages from other sites.
  - Distributed deadlock, which occurs when two or more transactions are waiting for locks held by each other in a cycle across different sites.
  - Global serialization, which is the problem of ensuring that the execution order of distributed transactions is equivalent to some serial order that respects the precedence of transactions based on their timestamps or commit order.
- To address these challenges, some possible solutions are:
  - Using timeout mechanisms to detect and resolve network failures and deadlocks.
  - Using distributed deadlock detection algorithms, such as edge-chasing or probe-based algorithms, to identify and break cycles of waiting transactions.
  - Using distributed commit protocols, such as two-phase commit (2PC) or three-phase commit (3PC), to coordinate the commit or abort decision of distributed transactions across multiple sites.
  - Using global concurrency control protocols, such as distributed 2PL, distributed TO, or distributed MVCC, to enforce a global serial order of distributed transactions.