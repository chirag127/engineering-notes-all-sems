### Comparison of methods for concurrency control for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Concurrency control is an essential aspect of distributed systems as it ensures that multiple transactions can access a shared resource without causing inconsistencies. There are various methods for concurrency control, and each has its advantages and disadvantages. Here is a comparison of some of the commonly used methods:

1. **Lock-based Concurrency Control**: In this method, locks are used to ensure that transactions access a shared resource in a mutually exclusive manner. The locks can be either exclusive or shared, and they are released after the transaction has completed its task. Lock-based concurrency control is simple to implement but can lead to deadlocks and can also cause high contention.

2. **Timestamp-based Concurrency Control**: This method assigns a timestamp to each transaction, which determines the order of execution. Transactions with lower timestamps are executed first, and if a transaction tries to access a resource that is already locked, it is aborted. Timestamp-based concurrency control is efficient and avoids deadlocks, but it can cause starvation for long-running transactions.

3. **Optimistic Concurrency Control**: In this method, transactions assume that no other transactions will conflict with them and perform their operations. Before committing, the system checks whether any conflicts have occurred, and if so, the transaction is aborted. Optimistic concurrency control is suitable for systems with low contention but can lead to frequent aborts and rollbacks.

4. **Multi-version Concurrency Control**: This method allows multiple versions of a resource to exist, and each transaction can access a specific version. This approach reduces contention and avoids deadlocks, but it can lead to an explosion in the number of versions and can cause high overheads.

Mnemonics and learning tricks can be helpful in remembering the different concurrency control methods. One such mnemonic is "LOTO" which stands for Lock-based, Optimistic, Timestamp-based, and Multi-version concurrency control. Another trick is to remember the advantages and disadvantages of each method and to use them to choose the appropriate method based on the system's requirements.

Overall, choosing the appropriate concurrency control method depends on the system's characteristics, such as the number of transactions, the level of contention, and the types of operations performed. By understanding the different methods and their trade-offs, we can design distributed systems that are efficient, reliable, and scalable.