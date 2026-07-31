Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for Unit 8 - Transactions and Concurrency Control.

## Unit 8 - Transactions and Concurrency Control

- A **transaction** is a logical unit of work that consists of a sequence of database operations, such as queries, updates, inserts, and deletes.
- A transaction has four properties, known as **ACID**:
  - **Atomicity**: A transaction is either executed in its entirety or not at all. If any operation in the transaction fails, the whole transaction is aborted and the database is restored to its previous state.
  - **Consistency**: A transaction preserves the consistency of the database by ensuring that it satisfies all the integrity constraints and business rules. The database is in a consistent state before and after the transaction.
  - **Isolation**: A transaction is executed in isolation from other transactions, meaning that its intermediate results are not visible to other transactions and it is not affected by the concurrent operations of other transactions.
  - **Durability**: The effects of a committed transaction are permanent and persist even in the case of system failures or power outages. The database system ensures that the committed changes are written to the disk and can be recovered if needed.
- **Concurrency control** is the technique of managing the simultaneous execution of transactions in a multi-user database system, such that the ACID properties are maintained and the performance is optimized.
- Concurrency control can be implemented using two main approaches: **locking** and **timestamping**.
  - **Locking** is the mechanism of granting exclusive or shared access to a data item or a set of data items to a transaction, based on the type of operation it performs. A transaction must acquire a lock before accessing a data item and release it after finishing the operation. Locking can prevent concurrency problems such as lost updates, uncommitted data, and inconsistent reads, but it can also cause deadlock, starvation, and reduced concurrency.
  - **Timestamping** is the mechanism of assigning a unique identifier to each transaction based on the time of its arrival or start, and using it to order the conflicting operations of different transactions. A transaction can access a data item only if its timestamp is compatible with the timestamps of previous operations on that data item. Timestamping can avoid deadlock and starvation, but it can also cause aborts, cascading aborts, and reduced concurrency.