## Unit 8 - Transactions and Concurrency Control

Transactions and concurrency control are crucial aspects of database management systems. In this unit, we will cover the following topics:

1. Definition of a transaction and its properties
2. ACID properties of a transaction
3. Types of transactions
4. Concurrency control and its importance
5. Lock-based concurrency control methods
6. Optimistic concurrency control methods
7. Timestamp-based concurrency control methods
8. Multiversion concurrency control methods

### Transaction Definition and Properties

A transaction is a sequence of operations that must be executed as a single unit of work. It is a fundamental concept in database management systems that ensures data consistency and reliability. A transaction has the following properties:

- Atomicity: A transaction is an atomic unit of work, which means that it either completes in its entirety or is rolled back to its initial state if it fails.
- Consistency: A transaction must maintain the consistency of the database by ensuring that all data modifications are valid and adhere to the database schema and integrity constraints.
- Isolation: A transaction must be isolated from other concurrent transactions to prevent interference and ensure data consistency.
- Durability: Once a transaction is committed, its changes are permanent and can survive system crashes or failures.

### ACID Properties of a Transaction

The ACID properties are a set of properties that ensure the reliability and consistency of transactions. The properties are:

- Atomicity: A transaction must be atomic, meaning it must be executed as a single unit of work.
- Consistency: A transaction must maintain the consistency of the database by ensuring that all data modifications are valid and adhere to the database schema and integrity constraints.
- Isolation: A transaction must be isolated from other concurrent transactions to prevent interference and ensure data consistency.
- Durability: Once a transaction is committed, its changes are permanent and can survive system crashes or failures.

### Types of Transactions

There are two types of transactions:

- Read-only transaction: A transaction that only reads data from the database but does not modify it.
- Read-write transaction: A transaction that reads data from the database and modifies it.

### Concurrency Control and its Importance

Concurrency control is the process of managing concurrent access to shared resources in a database management system. It is important because it ensures data consistency and reliability in the face of concurrent access. Concurrency control methods fall into three categories:

- Lock-based concurrency control methods
- Optimistic concurrency control methods
- Timestamp-based concurrency control methods

### Lock-based Concurrency Control Methods

Lock-based concurrency control methods use locks to synchronize access to shared resources, such as data items or tables. There are two types of locks:

- Shared locks: Allow multiple transactions to read the same data item simultaneously.
- Exclusive locks: Allow only one transaction to modify a data item at a time.

### Optimistic Concurrency Control Methods

Optimistic concurrency control methods assume that conflicts are rare and do not use locks to synchronize access. Instead, they use a validation phase to check for conflicts before committing a transaction. If a conflict is detected, the transaction is rolled back and restarted.

### Timestamp-based Concurrency Control Methods

Timestamp-based concurrency control methods assign a unique timestamp to each transaction and use these timestamps to determine the order in which transactions should be executed. Transactions are executed in order of their timestamps, and conflicts are resolved by rolling back the transaction with the lowest timestamp.

### Multiversion Concurrency Control Methods

Multiversion concurrency control methods maintain multiple versions of a data item to allow concurrent access. Each version is associated with a timestamp, and transactions can access the version that is consistent with their timestamp. Conflicts are resolved by rolling back transactions and restarting them with a new timestamp.