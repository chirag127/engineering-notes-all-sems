### Controlling Concurrent Accesses to Data Objects

- In real time systems, data objects are shared resources that can be accessed by multiple concurrent tasks or transactions.
- Controlling concurrent accesses to data objects is important to ensure data consistency and to meet timing constraints of real time tasks or transactions.
- There are two main approaches for controlling concurrent accesses to data objects: pessimistic and optimistic.
- Pessimistic approaches prevent conflicts by locking data objects before accessing them. Examples of pessimistic approaches are priority inheritance protocol, priority ceiling protocol, and convex ceiling protocol.
- Optimistic approaches allow conflicts to occur and resolve them later by aborting or restarting transactions. Examples of optimistic approaches are timestamp ordering, multiversion concurrency control, and validation .
- The choice of the concurrency control approach depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, and the available resources.
- The performance of the concurrency control approach can be measured by metrics such as the number of aborted transactions, the number of missed deadlines, the response time, and the throughput.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real-Time Database Systems - ResearchGate
: Concurrency Control in Real-Time Database Systems - Springer