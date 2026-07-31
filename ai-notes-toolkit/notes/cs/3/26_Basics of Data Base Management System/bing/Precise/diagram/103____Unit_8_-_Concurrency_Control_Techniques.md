## Unit 8 - Concurrency Control Techniques

Concurrency control is the process of managing simultaneous execution of transactions in a shared database, to ensure the consistency and isolation of the transactions. There are several techniques used to achieve concurrency control, including:

1. **Locking**: This technique involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously. Locks can be shared or exclusive, and can be placed on different levels of granularity, such as rows, pages, or tables.

2. **Timestamp ordering**: This technique assigns a unique timestamp to each transaction, and uses the timestamps to determine the order in which transactions are allowed to execute. Transactions with earlier timestamps are given priority over transactions with later timestamps.

3. **Optimistic concurrency control**: This technique assumes that conflicts between transactions are rare, and allows transactions to execute without acquiring locks. Before a transaction commits, the system checks if any conflicts have occurred, and if so, the transaction is rolled back and restarted.

4. **Multiversion concurrency control**: This technique maintains multiple versions of data items, allowing transactions to read older versions of data while other transactions are modifying the same data. This can improve concurrency by reducing the need for locking.

These are some of the main techniques used for concurrency control in database systems. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the system.