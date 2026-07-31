### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that may be accessed by multiple jobs in a real time system.
- Data objects have consistency requirements that must be maintained by the concurrency control mechanism.
- Concurrency control aims to prevent data conflicts and ensure serializability of transactions that access data objects.
- Serializability means that the concurrent execution of transactions is equivalent to some sequential execution of the same transactions.
- Concurrency control can be classified into two categories: pessimistic and optimistic.
  - Pessimistic concurrency control prevents data conflicts by locking data objects before accessing them and releasing them after accessing them.
  - Optimistic concurrency control allows data conflicts to occur and resolves them by validating and aborting transactions at the end of their execution.
- Pessimistic concurrency control can use different locking protocols, such as two-phase locking, priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol .
  - Two-phase locking requires that a transaction acquires all the locks it needs before releasing any lock.
  - Priority inheritance protocol assigns the priority of a blocked transaction to the blocking transaction until the lock is released.
  - Priority ceiling protocol assigns a priority ceiling to each data object and prevents a transaction from locking an object if its priority is lower than the current system ceiling, which is the highest priority ceiling of all locked objects.
  - Convex ceiling protocol assigns a convex ceiling to each data object and prevents a transaction from locking an object if its priority is lower than the current system ceiling, which is the highest convex ceiling of all locked objects.
- Optimistic concurrency control can use different validation protocols, such as basic timestamp ordering, wait-die, wound-wait, and multiversion timestamp ordering.
  - Basic timestamp ordering assigns a timestamp to each transaction and validates it by checking if it accessed any data object that was modified by a later transaction.
  - Wait-die and wound-wait are deadlock prevention protocols that use timestamps to decide whether a transaction should wait for a lock or abort and restart.
  - Multiversion timestamp ordering maintains multiple versions of each data object and assigns a timestamp to each version and each transaction. It validates a transaction by checking if it accessed the correct version of each data object according to its timestamp.
- Concurrency control in real time systems should consider both data consistency and timing constraints of transactions .
- Concurrency control in real time systems should also adapt to changes in the operating environment and guarantee the completion of critical transactions.
- Concurrency control in real time systems is a challenging and active research area that requires trade-offs between performance, predictability, and flexibility.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real-Time Database Systems
: Controlling Concurrent Access to Data Objects - Bench Partner
: Concurrency Control in Real-Time Database Systems