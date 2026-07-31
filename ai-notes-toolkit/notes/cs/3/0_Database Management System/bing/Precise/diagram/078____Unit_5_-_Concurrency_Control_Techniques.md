## Unit 5 - Concurrency Control Techniques

Concurrency control is the process of managing simultaneous operations on a database without having them interfere with one another. There are several techniques used to achieve concurrency control, including:

1. **Locking**: This technique involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously. Locks can be shared or exclusive, depending on the type of operation being performed.

2. **Timestamp ordering**: This technique assigns a timestamp to each transaction and uses these timestamps to determine the order in which transactions are executed. Transactions with earlier timestamps are given priority over those with later timestamps.

3. **Optimistic concurrency control**: This technique assumes that conflicts between transactions are rare and allows transactions to execute without acquiring locks. If a conflict is detected, one of the conflicting transactions is rolled back and restarted.

4. **Multiversion concurrency control**: This technique maintains multiple versions of data items and allows transactions to access the version of the data that was current at the time the transaction started. This can help reduce conflicts between transactions.

These are some of the main techniques used for concurrency control in database systems. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the system.