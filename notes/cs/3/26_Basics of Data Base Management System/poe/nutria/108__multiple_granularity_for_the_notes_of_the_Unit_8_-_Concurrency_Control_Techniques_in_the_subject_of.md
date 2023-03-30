
### Multiple Granularity for the Notes of Unit 8 - Concurrency Control Techniques in the Subject of Basics of Database Management System

1. Concurrency control is a technique used to ensure that multiple users can access and update a database at the same time without compromising the integrity of the data.

2. In order to achieve this, concurrency control techniques are used to manage the access and update operations.

3. The most common concurrency control techniques are two-phase locking, timestamp ordering, and optimistic concurrency control.

4. Two-phase locking (2PL) is a locking protocol that ensures that transactions acquire locks before they can access or modify data.

5. Timestamp ordering (TO) is a protocol that assigns a timestamp to each transaction and ensures that transactions are executed in the order of their timestamps.

6. Optimistic concurrency control (OCC) is a protocol that allows transactions to proceed without acquiring locks and then checks for conflicts at commit time.

7. In addition to the above techniques, there are also more advanced techniques such as multi-granularity locking, which allows locks to be acquired at different levels of granularity.

8. Multi-granularity locking is used to reduce the amount of time spent waiting for locks and to reduce the amount of data locked at any given time.

9. Finally, there are also techniques such as distributed transactions and distributed concurrency control which are used in distributed systems.