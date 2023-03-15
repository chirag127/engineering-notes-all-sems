# Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real-time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the concurrent accesses to data objects and ensure data consistency and timeliness.
- Concurrency control algorithms for real-time systems can be classified into two categories: pessimistic and optimistic.
- Pessimistic algorithms prevent conflicts from occurring by enforcing mutual exclusion or serialization among conflicting accesses. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
- Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting some transactions. Examples of optimistic algorithms are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- The choice of concurrency control algorithm depends on the characteristics of the system, such as the degree of data contention, the number of data objects, the size of transactions, the deadline requirements, and the system overhead.