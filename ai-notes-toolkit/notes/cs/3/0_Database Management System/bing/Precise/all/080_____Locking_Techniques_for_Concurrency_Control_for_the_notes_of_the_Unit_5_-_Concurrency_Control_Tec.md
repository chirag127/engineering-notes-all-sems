# Locking Techniques for Concurrency Control

Locking techniques are used in concurrency control to ensure that transactions are executed in a way that maintains the consistency and integrity of the database. Here are some key points to remember about locking techniques for concurrency control:

1. **Locks** are used to control access to data items in a database. A lock can be placed on a data item to prevent other transactions from accessing it while it is being modified by a transaction.

2. **Lock modes** determine the level of access that a transaction has to a data item. The most common lock modes are shared locks and exclusive locks. A shared lock allows multiple transactions to read a data item simultaneously, while an exclusive lock allows only one transaction to read and write to a data item.

3. **Lock granularity** refers to the size of the data item that is being locked. Locks can be placed on individual data items, such as rows or columns, or on larger units of data, such as tables or entire databases.

4. **Two-phase locking** is a locking protocol that ensures serializability of transactions. In the first phase, a transaction acquires all the locks it needs before it starts executing. In the second phase, the transaction releases all its locks after it has finished executing.

5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks. Deadlock prevention and detection techniques can be used to avoid or resolve deadlocks.

These are some of the key points to remember about locking techniques for concurrency control in a database management system. It is important to understand these concepts in order to effectively manage concurrency and ensure the consistency and integrity of the database.