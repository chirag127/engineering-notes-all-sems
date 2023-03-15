## Unit 5 - Concurrency Control Techniques

Concurrency control techniques are used to ensure the consistency and correctness of data in a database when multiple transactions are being executed simultaneously. Some of the common concurrency control techniques are:

1. **Locking**: This technique involves placing locks on data items to prevent multiple transactions from accessing the same data item simultaneously. There are different types of locks, such as shared locks, exclusive locks, and update locks.

2. **Timestamp ordering**: This technique assigns a unique timestamp to each transaction and uses the timestamps to determine the order in which transactions are executed. Transactions with earlier timestamps are executed before transactions with later timestamps.

3. **Optimistic concurrency control**: This technique assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. At the end of the transaction, the system checks for conflicts and rolls back the transaction if a conflict is detected.

4. **Multiversion concurrency control**: This technique maintains multiple versions of data items and allows transactions to read older versions of data items while other transactions are updating the same data items.

These are some of the common concurrency control techniques used in database systems to ensure the consistency and correctness of data. Each technique has its own advantages and disadvantages and the choice of technique depends on the specific requirements of the system.