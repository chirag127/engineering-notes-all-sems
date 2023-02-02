### Concurrency control in distributed transactions for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM
Concurrency control in distributed transactions is a technique to manage simultaneous access to shared resources in a distributed system. It ensures that transactions are executed in a consistent and correct manner, even in the presence of failures or delays.

There are two main approaches to concurrency control in distributed transactions:
1. Two-phase locking (2PL)
2. Optimistic concurrency control (OCC)

1. Two-phase locking (2PL):
- Transactions acquire locks on shared resources before accessing them
- Transactions release locks after they have finished accessing the resources
- Locks are acquired in two phases:
  - Growing phase: transactions acquire locks
  - Shrinking phase: transactions release locks
- 2PL ensures that transactions are executed in a serializable manner, but can lead to deadlocks if not managed properly.

2. Optimistic concurrency control (OCC):
- Transactions access shared resources without acquiring locks
- Transactions are executed optimistically, assuming that no conflicts will occur
- Conflicts are detected during the validation phase, when transactions try to commit their changes
- If a conflict is detected, the transaction is rolled back and retried later
- OCC can improve performance compared to 2PL, but requires more complex algorithms to detect and resolve conflicts.

In summary, concurrency control in distributed transactions is crucial to ensure the consistency and correctness of transactions in a distributed system. Both 2PL and OCC have their advantages and disadvantages, and the choice of approach depends on the specific requirements of the system.
