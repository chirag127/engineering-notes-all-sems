
### Locks for the Notes of Unit 8 - Transactions and Concurrency Control in the Subject of DISTRIBUTED SYSTEM

1. Locks are mechanisms that are used to control access to resources in a distributed system.
2. In a distributed system, locks can be used to ensure that multiple processes do not access or modify the same resource at the same time.
3. Locks are used to ensure that transactions are atomic, meaning that either all of the operations in the transaction are completed or none of them are.
4. Locks can be used to prevent deadlock, which occurs when multiple processes are waiting for each other to release a lock.
5. Locks can be used to ensure that transactions are serializable, meaning that the results of the transactions are the same as if they were executed one after the other in some order.
6. Locks can be implemented using different strategies, such as locking the entire resource, locking parts of the resource, or using optimistic concurrency control.
7. Locks must be managed carefully to ensure that they are not held for too long, or that they are not released too soon.
8. Locks must also be managed carefully to ensure that they are not held by processes that are no longer active.