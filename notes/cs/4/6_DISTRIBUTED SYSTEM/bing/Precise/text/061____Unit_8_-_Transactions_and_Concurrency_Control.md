## Unit 8 - Transactions and Concurrency Control

1. **Transactions** are a sequence of database operations that are treated as a single logical unit of work.
2. The **ACID** properties of transactions ensure that the database remains in a consistent state even in the event of failures.
3. **Concurrency control** is the process of managing simultaneous access to a database by multiple users while maintaining the consistency and integrity of the data.
4. **Locking** is a common method of concurrency control, where locks are placed on data items to prevent multiple transactions from accessing the same data simultaneously.
5. **Deadlocks** can occur when two or more transactions are waiting for each other to release locks, and can be resolved using techniques such as deadlock detection and resolution, or by using timeouts.
6. **Optimistic concurrency control** is an alternative approach that assumes conflicts are rare and only checks for conflicts at the end of a transaction, rolling back and retrying if necessary.
7. **Isolation levels** determine the degree to which transactions are isolated from each other, with higher levels providing stronger guarantees but potentially reducing concurrency.