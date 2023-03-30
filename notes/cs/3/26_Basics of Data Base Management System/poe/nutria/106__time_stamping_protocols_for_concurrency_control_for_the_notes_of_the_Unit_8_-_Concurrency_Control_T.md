
### Time Stamping Protocols for Concurrency Control
Time stamping protocols are used to control concurrent access to a shared resource in a distributed database system. These protocols ensure that all transactions are executed in the correct order and that no transaction is executed more than once.

1. **Lamport's Logical Clock:** This protocol uses a logical clock to assign a unique time stamp to each transaction. The clock is incremented each time a transaction is initiated, and the time stamp is used to order the transactions.

2. **Vector Clock:** This protocol uses a vector of time stamps to order transactions. Each component of the vector is incremented each time a transaction is initiated, and the vector is used to order the transactions.

3. **Multi-Version Concurrency Control:** This protocol uses multiple versions of the same data item to maintain consistency. Each transaction is given a unique time stamp, and the most recent version of the data item is used for the transaction.

4. **MVCC (Multi-Version Concurrency Control):** This protocol uses multiple versions of the same data item to maintain consistency. Each transaction is given a unique time stamp, and the most recent version of the data item is used for the transaction.

5. **Timestamp Ordering Protocol:** This protocol uses a timestamp to order the transactions. The timestamp is assigned to each transaction, and the transactions are executed in the order of their timestamps.