## Unit 5 - Concurrency Control Techniques

- Concurrency control techniques are methods to ensure the consistency and isolation of transactions in a database system that allows multiple users to access and modify data simultaneously.
- Concurrency control techniques can be classified into two categories: pessimistic and optimistic.
- Pessimistic concurrency control techniques prevent conflicts from occurring by locking the data items that are accessed by transactions. Examples of pessimistic techniques are two-phase locking, timestamp ordering, and strict two-phase locking.
- Optimistic concurrency control techniques allow conflicts to occur and then detect and resolve them before committing the transactions. Examples of optimistic techniques are validation-based, multiversion, and snapshot isolation.
- The choice of concurrency control technique depends on the characteristics of the application, the workload, and the performance requirements. Some factors to consider are the degree of concurrency, the conflict rate, the overhead of locking and validation, and the response time.