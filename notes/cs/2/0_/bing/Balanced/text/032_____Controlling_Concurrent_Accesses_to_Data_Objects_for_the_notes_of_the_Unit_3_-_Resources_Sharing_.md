### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts by locking data objects before accessing them and releasing them after finishing the access. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and resolve them by aborting and restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- The choice of concurrency control algorithm depends on the characteristics of the real time system, such as the degree of data sharing, the number of processors, the workload, and the performance metrics.