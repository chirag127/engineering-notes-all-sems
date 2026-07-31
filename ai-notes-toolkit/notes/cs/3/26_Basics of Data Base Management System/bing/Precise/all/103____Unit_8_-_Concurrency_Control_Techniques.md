## Unit 8 - Concurrency Control Techniques

Concurrency control is the process of managing simultaneous operations on a database without having them interfere with one another. This is important to ensure the consistency and integrity of data in a database. There are several techniques used to achieve concurrency control, including:

1. **Locking:** This technique involves placing locks on data items to prevent multiple transactions from accessing the same data simultaneously. Locks can be shared or exclusive, and can be placed on different levels of granularity, such as rows, pages, or tables.

2. **Timestamp ordering:** This technique assigns a timestamp to each transaction, and the order of execution is determined by the timestamps. Transactions with earlier timestamps are given priority over those with later timestamps.

3. **Optimistic concurrency control:** This technique assumes that conflicts between transactions are rare, and allows transactions to execute without acquiring locks. Before committing, a transaction checks if any conflicts have occurred, and if so, the transaction is rolled back and restarted.

4. **Multiversion concurrency control:** This technique allows multiple versions of data to exist simultaneously, and transactions can access the version of the data that was current at the time the transaction started. This can reduce the need for locking and improve performance.

These are some of the main techniques used for concurrency control in databases. Each technique has its own advantages and disadvantages, and the choice of technique depends on the specific requirements of the database system.