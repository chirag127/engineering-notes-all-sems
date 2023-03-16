### Controlling Concurrent Accesses to Data Objects

- In real time systems, data objects are shared resources that can be accessed by multiple concurrent tasks or transactions.
- Controlling concurrent accesses to data objects is important to ensure data consistency and to meet timing constraints of real time tasks or transactions.
- There are two main approaches to control concurrent accesses to data objects: pessimistic and optimistic.
- Pessimistic approaches prevent conflicts by locking data objects before accessing them. Examples of pessimistic approaches are priority ceiling protocol, convex ceiling protocol, and priority inheritance protocol.
- Optimistic approaches allow conflicts to occur and then resolve them by aborting or restarting transactions. Examples of optimistic approaches are timestamp ordering, validation, and multiversion concurrency control .
- The choice of concurrency control approach depends on the characteristics of the real time system, such as the degree of data contention, the criticality of transactions, and the availability of resources.
- The performance of concurrency control approaches can be evaluated by metrics such as blocking time, response time, deadline miss ratio, and throughput.

: Controlling Concurrent Accesses To Data Objects - Skedsoft
: Concurrency Control Algorithms for Real Time Database Systems - ResearchGate
: Concurrency Control in Real Time Database Systems - Springer