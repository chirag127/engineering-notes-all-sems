### Concurrency control

- Concurrency control is the process of managing simultaneous operations on a database without compromising its integrity or consistency.
- Concurrency control is needed to ensure that concurrent transactions do not interfere with each other and violate the ACID properties of transactions (atomicity, consistency, isolation, and durability).
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and snapshot isolation.
- The choice of concurrency control technique depends on the characteristics of the application, the workload, and the performance requirements. Some factors to consider are the degree of concurrency, the conflict rate, the overhead of locking and validation, and the response time.