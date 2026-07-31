### Controlling Concurrent Accesses to Data Objects

- Data objects are a special type of shared resources that store information and can be accessed by multiple jobs in a real time system.
- When jobs are scheduled preemptively, their accesses to data objects may be interleaved, which can cause data inconsistency and violate the correctness of the system.
- To prevent data inconsistency, concurrency control algorithms are needed to regulate the concurrent accesses to data objects and ensure data consistency.
- Concurrency control algorithms for real time systems should also consider the timing constraints of the jobs and avoid unnecessary blocking or aborting of critical jobs.
- There are two main types of concurrency control algorithms for real time systems: pessimistic and optimistic.
  - Pessimistic algorithms prevent data conflicts by locking the data objects before accessing them and releasing them after accessing them. Examples of pessimistic algorithms are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol .
  - Optimistic algorithms allow data conflicts to occur and detect them after accessing the data objects. If a conflict is detected, the conflicting jobs are aborted and restarted. Examples of optimistic algorithms are timestamp ordering, multiversion concurrency control, and validation-based protocols .
- The choice of concurrency control algorithm depends on the characteristics of the system, such as the number and size of data objects, the frequency and duration of data accesses, the degree of data contention, the criticality and deadline of the jobs, and the overhead of locking, aborting, and restarting .