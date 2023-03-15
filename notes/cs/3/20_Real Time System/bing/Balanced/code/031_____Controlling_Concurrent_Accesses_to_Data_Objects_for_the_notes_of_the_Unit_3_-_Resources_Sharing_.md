### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, resulting in data inconsistency or deadlock.
- To prevent these problems, concurrency control algorithms are needed to coordinate the accesses to data objects and ensure data consistency and timing constraints.
- Concurrency control algorithms can be classified into two categories: pessimistic and optimistic.
  - Pessimistic algorithms prevent conflicts from occurring by locking data objects before accessing them. Examples are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
  - Optimistic algorithms allow conflicts to occur and then resolve them by aborting or restarting transactions. Examples are wait-free synchronization, timestamp ordering, and multiversion concurrency control.
- Pessimistic algorithms are suitable for hard real time systems where deadlines are strict and aborts are costly. Optimistic algorithms are suitable for soft real time systems where deadlines are flexible and aborts are acceptable.
- Some of the factors that affect the performance of concurrency control algorithms are blocking time, priority inversion, deadlock, abort rate, response time, and schedulability.