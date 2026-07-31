### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts by locking data objects before accessing them and releasing them after finishing the access. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- Pessimistic algorithms have the advantage of avoiding unnecessary aborts and restarts, but they may incur blocking overhead and deadlock risk. Optimistic algorithms have the advantage of avoiding blocking and deadlock, but they may incur abort and restart overhead and waste system resources.
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, the predictability of workload, and the performance requirements.