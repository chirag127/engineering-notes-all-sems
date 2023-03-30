

### Transaction Management for Unit 1 - Introduction to Basics of Database Management System

1. A transaction is a set of operations that are performed as a single logical unit of work.
2. A transaction must be atomic, consistent, isolated, and durable.
3. Atomicity means that all operations within the transaction are completed successfully, or none of them are.
4. Consistency means that the transaction must leave all data in a consistent state.
5. Isolation means that the transaction must not interfere with other transactions that are running concurrently.
6. Durability means that the effects of a transaction must persist even if the system fails after the transaction has completed.
7. Transaction management is a key component of database systems, as it ensures the integrity of the data.
8. Transaction management is also known as concurrency control, which is the process of managing simultaneous access to shared data.
9. The most common concurrency control techniques are locking, timestamp ordering, and multiversion concurrency control.
10. Locking is the process of preventing other transactions from accessing data while a transaction is using it.
11. Timestamp ordering is the process of assigning a timestamp to each transaction and ensuring that transactions are executed in order.
12. Multiversion concurrency control is the process of creating multiple versions of data and allowing transactions to operate on the versions without interfering with each other.