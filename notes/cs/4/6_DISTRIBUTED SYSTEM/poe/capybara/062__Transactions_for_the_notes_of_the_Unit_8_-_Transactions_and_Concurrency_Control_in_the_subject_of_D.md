### Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM

Transactions are an essential part of distributed systems. They are a set of operations that are executed as a single unit of work. The purpose of transactions is to ensure that the data in a distributed system remains consistent and accurate. Transactions have four key properties: atomicity, consistency, isolation, and durability.

1. **Atomicity**: Transactions must be atomic, meaning that they are either completed entirely or not at all. If any part of the transaction fails, the entire transaction is rolled back, and the system returns to its previous state.

2. **Consistency**: Transactions must ensure that the data in the system remains consistent throughout the transaction. This means that the data must satisfy all the constraints and rules defined by the system.

3. **Isolation**: Transactions must be isolated from one another. This means that the changes made by one transaction must not be visible to other transactions until the first transaction is completed.

4. **Durability**: Transactions must be durable, meaning that once they are completed, the changes made by the transaction are permanent and cannot be undone.

Concurrency control is another important aspect of distributed systems. Concurrency control is used to ensure that multiple transactions can access the same data without causing conflicts or inconsistencies. There are various techniques used for concurrency control, such as locking and optimistic concurrency control.

1. **Locking**: Locking is a technique used to prevent conflicts between transactions. When a transaction accesses a piece of data, it acquires a lock on that data. This lock prevents other transactions from accessing the same data until the first transaction releases the lock.

2. **Optimistic concurrency control**: Optimistic concurrency control is a technique used to avoid conflicts between transactions. It assumes that conflicts are rare and allows transactions to proceed without acquiring locks. If conflicts do occur, the system detects them and rolls back the transactions.

Overall, transactions and concurrency control are crucial for ensuring the consistency and accuracy of data in distributed systems. It is essential to understand these concepts thoroughly to design and implement effective distributed systems.