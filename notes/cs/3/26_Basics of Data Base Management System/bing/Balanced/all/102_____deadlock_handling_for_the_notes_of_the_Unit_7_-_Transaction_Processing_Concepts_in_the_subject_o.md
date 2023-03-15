# Deadlock Handling

- A deadlock is a situation where a set of transactions are blocked waiting for each other to release locks on the data items they need.
- Deadlocks can occur in a concurrent transaction processing system when transactions use locking for concurrency control.
- Deadlocks are undesirable because they waste system resources and reduce throughput.
- There are three main methods for handling deadlocks: prevention, avoidance, and detection and recovery.

## Deadlock Prevention

- Deadlock prevention is a method that ensures that at least one of the four necessary conditions for deadlock does not hold.
- The four necessary conditions for deadlock are: mutual exclusion, hold and wait, no preemption, and circular wait.
- Deadlock prevention can be achieved by imposing some constraints on how transactions acquire and release locks.
- Some examples of deadlock prevention techniques are:

  - Timestamp ordering: transactions are assigned timestamps when they start, and they must request locks in the order of their timestamps. This prevents circular wait.
  - Conservative locking: transactions must request all the locks they need before they start execution. This prevents hold and wait.
  - Two-phase locking with lock conversion: transactions must acquire all the locks they need in a growing phase, and then release them in a shrinking phase. They can also convert a shared lock to an exclusive lock, or vice versa, in the growing phase. This prevents hold and wait and circular wait.

## Deadlock Avoidance

- Deadlock avoidance is a method that allows transactions to acquire locks dynamically, but checks whether granting a lock request will lead to a potential deadlock.
- Deadlock avoidance requires the system to have some knowledge of the future requests of transactions, such as the set of data items they will access.
- Deadlock avoidance can be achieved by using a deadlock detection algorithm, such as the wait-for graph or the banker's algorithm, to determine whether granting a lock request is safe or unsafe.
- A lock request is safe if it does not create a circular wait among the transactions. A lock request is unsafe if it may create a circular wait in the future.
- If a lock request is safe, the system grants it. If a lock request is unsafe, the system delays it until it becomes safe.

## Deadlock Detection and Recovery

- Deadlock detection and recovery is a method that allows transactions to acquire locks without any constraints, but periodically checks whether a deadlock has occurred.
- Deadlock detection and recovery does not require the system to have any knowledge of the future requests of transactions.
- Deadlock detection and recovery can be achieved by using a deadlock detection algorithm, such as the wait-for graph or the wound-wait scheme, to identify the transactions involved in a deadlock.
- A wait-for graph is a directed graph where the nodes are transactions and the edges are wait-for relationships. An edge from Ti to Tj means that Ti is waiting for Tj to release a lock. A cycle in the wait-for graph indicates a deadlock.
- A wound-wait scheme is a priority-based scheme where transactions are assigned priorities based on their timestamps. A transaction with a higher priority can either wait for or wound a transaction with a lower priority. Wounding means aborting and restarting the transaction with the same timestamp. A deadlock occurs when two or more transactions are waiting for each other and none of them can wound the others.
- Once a deadlock is detected, the system must perform some recovery actions to resolve it. Some examples of recovery actions are:

  - Victim selection: the system chooses one or more transactions to abort and restart. The choice can be based on criteria such as the amount of work done, the number of locks held, the priority, or the estimated remaining time.
  - Rollback: the system restores the database to a consistent state by undoing the effects of the aborted transactions. The rollback can be total, where the transaction is restarted from the beginning, or partial, where the transaction is restarted from a savepoint.
  - Lock release: the system releases the locks held by the aborted transactions and grants them to the waiting transactions. The system must ensure that the lock release does not violate the serializability or the recoverability of the transactions.