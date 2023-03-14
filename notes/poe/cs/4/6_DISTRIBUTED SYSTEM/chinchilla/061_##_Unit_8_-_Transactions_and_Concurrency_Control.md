## Unit 8 - Transactions and Concurrency Control

In the world of databases, transactions refer to a sequence of database operations that are executed as a single logical unit of work. Transactions are used to ensure data consistency and integrity in a database system. Concurrency control is the process of managing simultaneous access to shared resources, such as databases, to ensure data consistency and prevent data corruption.

Here are some important concepts related to transactions and concurrency control:

### ACID Properties

ACID stands for Atomicity, Consistency, Isolation, and Durability. These properties define the behavior of a transaction in a database system. 

- **Atomicity**: A transaction is atomic if it is executed as a single, indivisible unit of work. Either all the sub-operations in a transaction are executed successfully or none of them are executed at all.
- **Consistency**: A transaction should leave the database in a consistent state. This means that the data should satisfy all the constraints and rules defined in the database schema.
- **Isolation**: Transactions should be executed in isolation from each other. This means that the concurrent execution of multiple transactions should not interfere with each other.
- **Durability**: The results of a committed transaction should be permanent and persistent. The transaction should survive system failures, power outages, and other disasters.

### Concurrency Control

Concurrency control is the process of managing the access of multiple transactions to shared resources in a database system. The main goal of concurrency control is to ensure that transactions are executed in a correct and consistent manner.

- **Locking**: Locking is a technique used to prevent multiple transactions from accessing the same data at the same time. A lock can be obtained on a data item before it is accessed, and it is released only when the transaction is complete.
- **Serializability**: Serializability is a property of a database schedule that ensures that the execution of concurrent transactions is equivalent to a serial execution of the same transactions. In other words, the database system ensures that the order in which transactions are executed does not affect the outcome of the transactions.
- **Deadlock**: A deadlock occurs when two or more transactions are waiting for each other to release a resource that they need to complete their work. Deadlocks can be prevented by using locking protocols or by detecting and resolving them when they occur.

### Learning Tricks

- To remember the ACID properties, you can use the mnemonic "ACID test", where each letter stands for one of the properties.
- To remember the different types of locks, you can use the mnemonic "SLIDE": Shared Lock, Exclusive Lock, Intent Shared Lock, Intent Exclusive Lock.
- To understand serializability, you can use the analogy of a traffic intersection. Just like cars at an intersection need to follow a specific order to avoid collisions, transactions in a database need to follow a specific order to avoid conflicts and ensure consistency.