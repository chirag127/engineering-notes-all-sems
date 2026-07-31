## Unit 8 - Concurrency Control Techniques

Concurrency control techniques are used to ensure the consistency and correctness of data in a database when multiple transactions are being executed simultaneously. Some of the common concurrency control techniques are:

1. **Locking**: This technique involves placing locks on data items to prevent multiple transactions from accessing the same data item simultaneously. There are different types of locks, such as shared locks and exclusive locks, that can be used depending on the operation being performed on the data item.

2. **Timestamp ordering**: This technique assigns a unique timestamp to each transaction and uses the timestamps to determine the order in which transactions are executed. Transactions with earlier timestamps are given priority over transactions with later timestamps.

3. **Optimistic concurrency control**: This technique assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. Before a transaction commits, it checks if any conflicts have occurred. If a conflict is detected, the transaction is rolled back and restarted.

4. **Multiversion concurrency control**: This technique maintains multiple versions of data items to allow transactions to read data without acquiring locks. Transactions can read the version of the data item that was current at the time the transaction started, while other transactions can update the data item without causing conflicts.

These are some of the common concurrency control techniques used in database systems to ensure the consistency and correctness of data when multiple transactions are being executed simultaneously. Each technique has its own advantages and disadvantages and the choice of technique depends on the specific requirements of the database system.