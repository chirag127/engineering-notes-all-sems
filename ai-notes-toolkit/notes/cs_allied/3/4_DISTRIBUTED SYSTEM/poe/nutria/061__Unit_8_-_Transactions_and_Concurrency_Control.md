
## Unit 8 - Transactions and Concurrency Control

1. A **transaction** is an atomic unit of work that is performed against a database. It is a logical unit of work that includes one or more related SQL statements.

2. **Concurrency** is the ability of multiple users to access and modify the same data simultaneously.

3. **Isolation** is the property of a transaction that ensures that operations of concurrent transactions do not interfere with each other.

4. **ACID** (Atomicity, Consistency, Isolation, Durability) is a set of properties that guarantee that transactions are processed reliably.

5. **Locking** is a mechanism used to ensure that multiple transactions do not interfere with each other. It allows transactions to access and modify data in a consistent and reliable way.

6. **Deadlocks** occur when two or more transactions are waiting for each other to finish before they can proceed.

7. **Serializability** is the property of a system of transactions that guarantees that the results of the transactions will be the same as if the transactions were executed one at a time in some serial order.