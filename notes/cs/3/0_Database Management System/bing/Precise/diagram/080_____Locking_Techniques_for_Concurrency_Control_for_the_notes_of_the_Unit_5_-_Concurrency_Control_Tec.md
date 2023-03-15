### Locking Techniques for Concurrency Control

Locking techniques are used in concurrency control to ensure that transactions are executed in a way that maintains the consistency and integrity of the database. Here are some key points to remember about locking techniques for concurrency control:

1. **Locks** are used to control access to data items in the database. A lock can be placed on a data item to prevent other transactions from accessing it while it is being modified by a transaction.

2. **Lock modes** determine the level of access that a transaction has to a data item. The most common lock modes are shared locks and exclusive locks. A shared lock allows multiple transactions to read a data item, while an exclusive lock allows only one transaction to read and write to a data item.

3. **Lock compatibility** determines whether multiple transactions can hold locks on the same data item at the same time. For example, two transactions can hold shared locks on the same data item, but only one transaction can hold an exclusive lock on a data item.

4. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks on data items. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

5. **Two-phase locking** is a commonly used locking protocol that ensures serializability of transactions. In the first phase, a transaction acquires all the locks it needs, and in the second phase, it releases all the locks it holds.
