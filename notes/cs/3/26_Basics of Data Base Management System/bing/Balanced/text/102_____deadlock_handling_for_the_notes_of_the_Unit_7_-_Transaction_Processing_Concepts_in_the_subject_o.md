### Deadlock Handling

- A deadlock is a situation where a set of transactions are blocked, waiting for each other to release locks on the data items they need.
- A deadlock can occur when two or more transactions request locks on the same data items in a conflicting mode, such as exclusive or shared.
- A deadlock can also occur when transactions hold locks on multiple data items and request more locks in a circular manner, such as T1 holds a lock on A and requests a lock on B, while T2 holds a lock on B and requests a lock on A.
- Deadlocks are undesirable because they waste system resources and reduce concurrency and throughput.
- There are three main methods to handle deadlocks: prevention, avoidance, and detection and recovery.

#### Deadlock Prevention

- Deadlock prevention is a technique that ensures that deadlocks never occur by imposing some restrictions on how transactions can acquire locks.
- One common method of deadlock prevention is to use a **timestamp ordering** protocol, which assigns a unique timestamp to each transaction when it starts, and uses the timestamps to order the lock requests.
- Another common method of deadlock prevention is to use a **wait-die** or **wound-wait** protocol, which compares the timestamps of the requesting and holding transactions, and either aborts or delays the requesting transaction based on the comparison.
- Deadlock prevention has the advantage of simplicity and low overhead, but it may also cause unnecessary aborts or delays, and reduce concurrency and performance.

#### Deadlock Avoidance

- Deadlock avoidance is a technique that allows transactions to acquire locks dynamically, but avoids granting a lock request that may lead to a deadlock in the future.
- One common method of deadlock avoidance is to use a **wait-for graph**, which is a directed graph that represents the waiting relationships among transactions. A node in the graph is a transaction, and an edge from Ti to Tj means that Ti is waiting for Tj to release a lock.
- The system maintains the wait-for graph and checks for cycles whenever a lock request is made. If granting a lock request would create a cycle in the graph, the system denies the request and makes the transaction wait.
- Deadlock avoidance has the advantage of allowing more concurrency and flexibility than deadlock prevention, but it also requires more overhead and complexity to maintain and check the wait-for graph.

#### Deadlock Detection and Recovery

- Deadlock detection and recovery is a technique that allows transactions to acquire locks freely, but periodically checks for the existence of deadlocks and takes actions to resolve them.
- One common method of deadlock detection is to use a **timeout** mechanism, which sets a limit on how long a transaction can wait for a lock. If the limit is exceeded, the system assumes that the transaction is involved in a deadlock and aborts it.
- Another common method of deadlock detection is to use a **wait-for graph**, as in deadlock avoidance, but only construct and check the graph periodically, rather than for every lock request.
- Deadlock detection and recovery has the advantage of allowing the maximum concurrency and simplicity, but it also has the disadvantage of wasting system resources and causing cascading aborts when deadlocks occur.