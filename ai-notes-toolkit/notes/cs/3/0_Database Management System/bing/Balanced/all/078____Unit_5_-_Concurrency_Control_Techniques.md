# Unit 5 - Concurrency Control Techniques

- Concurrency control is the process of managing simultaneous operations on a shared database without compromising data integrity, consistency, and isolation.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by concurrent transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and timestamp-based methods.
- The choice of concurrency control technique depends on several factors, such as the degree of conflict, the overhead of locking and validation, the performance and scalability requirements, and the application characteristics.