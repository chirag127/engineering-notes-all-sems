
### Deadlock Handling

1. Deadlock is a situation where two or more transactions are waiting for each other to release a lock on a resource.
2. The deadlock occurs when a transaction requests a resource held by another transaction and the other transaction requests a resource held by the first transaction.
3. Deadlock detection is the process of identifying and resolving deadlocks.
4. The most common way to detect deadlocks is to use a wait-for graph.
5. The wait-for graph is a directed graph where each node represents a transaction and an edge from one node to another indicates that the first transaction is waiting for the second transaction to release a lock.
6. Deadlock prevention techniques include resource ordering, lock timeouts, and deadlock avoidance.
7. Resource ordering is a technique where all resources are ordered in a specific manner and locks are acquired in that order.
8. Lock timeouts are a technique where locks are released after a certain amount of time if the transaction has not completed.
9. Deadlock avoidance is a technique where transactions are allowed to acquire locks only if it can guarantee that no deadlock will occur.