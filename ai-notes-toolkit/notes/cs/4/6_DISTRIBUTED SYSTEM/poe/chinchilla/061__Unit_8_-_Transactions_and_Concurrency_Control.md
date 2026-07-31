## Unit 8 - Transactions and Concurrency Control

In this unit, we will learn about transactions and concurrency control in database management systems. Here are some key points to keep in mind:

### Transactions

- A transaction is a logical unit of work that consists of one or more database operations.
- Transactions have four properties, commonly known as ACID:
  - Atomicity: all or nothing property that ensures that if any part of the transaction fails, the entire transaction fails.
  - Consistency: ensures that a transaction brings the database from one consistent state to another.
  - Isolation: ensures that concurrent transactions do not interfere with each other.
  - Durability: ensures that once a transaction is committed, its changes are permanent and survive system failures.
- Transactions can be started with a BEGIN TRANSACTION statement and ended with either a COMMIT or a ROLLBACK statement.
- A COMMIT statement saves the changes made by a transaction and a ROLLBACK statement undoes them.

### Concurrency Control

- Concurrency control is the process of managing simultaneous access to a shared resource, such as a database, to ensure data consistency and integrity.
- In database management systems, concurrency control is necessary to prevent conflicts between transactions that access the same data.
- Two main approaches are used for concurrency control: locking and timestamping.
- Locking involves acquiring locks on data items before accessing them, and releasing them after the transaction is completed.
- Timestamping involves assigning a unique timestamp to each transaction and using these timestamps to determine the order in which transactions should be executed.
- The most commonly used concurrency control algorithm is the two-phase locking protocol, which ensures serializability of transactions.
- Other concurrency control techniques include optimistic concurrency control and multi-version concurrency control.

### Conclusion

Transactions and concurrency control are essential features of database management systems that ensure data consistency, integrity, and reliability. Understanding these concepts is crucial for building robust and scalable database applications.