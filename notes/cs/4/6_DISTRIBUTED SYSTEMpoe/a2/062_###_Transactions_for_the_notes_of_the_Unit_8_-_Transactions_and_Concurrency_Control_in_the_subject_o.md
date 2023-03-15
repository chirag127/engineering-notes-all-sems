 Here is the content in markdown format for the topic ### Transactions for the notes of the Unit 8 - Transactions and Concurrency Control in the subject of DISTRIBUTED SYSTEM:

### Transactions

- A transaction is a unit of work that is atomic, consistent, isolated, and durable (ACID).
- Atomic: Either all operations in a transaction succeed or all fail. There is no partial completion of a transaction.
- Consistent: A transaction moves data from one valid state to another. If a transaction fails, the system state is unchanged.
- Isolated: Transactions execute independently and concurrently without interference.
- Durable: Once a transaction completes successfully, its effects persist even if there is a system failure.

#### Types of Transactions

- Flat transaction: Contains only one execution thread.
- Nested transaction: A transaction that is nested inside another transaction. If the outer transaction commits, then the nested transaction is also committed; if the outer transaction rolls back, then the nested transaction is also rolled back.
- Distributed transaction: A transaction that updates data on two or more networked computers. Ensuring ACID properties for distributed transactions is challenging.

#### commits and rollbacks

- Commit: To finalize a transaction, making its changes permanent.
- Rollback: To undo a transaction, discarding its changes.

A transaction can be rolled back for various reasons:

- Deadlock: Two transactions are waiting for each other to release locks, causing both to halt.
- Concurrency conflicts: The serial execution of concurrent transactions can lead to incorrect results.
- System failures: If the system fails in the middle of a transaction, the partial work must be rolled back.
- User request: A user can explicitly request rollback of a transaction.

#### Mnemonics and learning tricks

- Think of a transaction as an "all or nothing" unit of work. It either fully completes or fully undoes. (Atomicity)
- Data is kept in a valid state as a transaction proceeds. (Consistency)
- Imagine transactions as isolated rooms that don't interact. (Isolation)
- Imagine transactions as permanent sticky notes on a wall. Once posted, they persist. (Durability)