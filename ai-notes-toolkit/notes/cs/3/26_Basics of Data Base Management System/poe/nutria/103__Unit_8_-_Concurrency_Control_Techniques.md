

## Unit 8 - Concurrency Control Techniques

1. Concurrency control is the process of managing simultaneous operations on a shared resource. It is used to ensure data integrity and to prevent data corruption in a multi-user environment. 

2. There are two main approaches to concurrency control: optimistic and pessimistic. Optimistic concurrency control assumes that conflicts are rare and is used when the probability of conflicts is low. Pessimistic concurrency control assumes that conflicts are likely and is used when the probability of conflicts is high.

3. The most common techniques for concurrency control are locking, timestamp ordering, and multi-version concurrency control (MVCC). 

4. Locking is the most basic technique for concurrency control. It involves granting exclusive access to a shared resource to one user at a time. The user is granted a lock on the resource, and other users are prevented from accessing it until the lock is released.

5. Timestamp ordering is a technique in which each transaction is assigned a timestamp. Transactions are then executed in the order of their timestamps. This ensures that transactions are executed in the order in which they were initiated, thus preventing conflicts.

6. Multi-version concurrency control (MVCC) is a technique in which multiple versions of a resource are maintained. Each version is assigned a timestamp, and transactions are executed on the version with the most recent timestamp. This ensures that transactions are executed on the most up-to-date version of the resource, thus preventing conflicts.