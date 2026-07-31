
## Unit 5 - Concurrency Control Techniques

1. Concurrency control is a set of techniques used to ensure the integrity of data when multiple users are accessing the same data at the same time.

2. The main goal of concurrency control is to ensure that concurrent transactions do not interfere with each other, resulting in data inconsistency.

3. Concurrency control techniques can be classified into two categories: pessimistic concurrency control and optimistic concurrency control.

4. Pessimistic concurrency control techniques use locks to prevent concurrent transactions from accessing the same data. These locks are released when the transaction is finished.

5. Optimistic concurrency control techniques allow concurrent transactions to access the same data, but use versioning to detect and resolve conflicts.

6. Examples of pessimistic concurrency control techniques include two-phase locking (2PL), strict two-phase locking (S2PL), and multi-version concurrency control (MVCC). 

7. Examples of optimistic concurrency control techniques include timestamp ordering (TO), serializability order (SO), and snapshot isolation (SI).