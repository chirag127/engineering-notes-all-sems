 Here is the content in markdown format for Unit 8 - Transactions and Concurrency Control:

## Unit 8 - Transactions and Concurrency Control

### Transactions
- A transaction is a logical unit of work that contains one or more SQL statements.
- A transaction begins with the first executable statement and ends with a COMMIT or ROLLBACK statement.
- The ACID properties of a transaction:
	- Atomicity - Either all statements are executed successfully or none.
	- Consistency - Data is consistent before and after the transaction.
	- Isolation - Transactions are isolated from each other.
	- Durability - Changes are permanent after a commit.
- Example transaction:
	START TRANSACTION;
	UPDATE accounts SET balance = balance - 100 WHERE account_number = 123;
	UPDATE accounts SET balance = balance + 100 WHERE account_number = 456;
	COMMIT;

### Concurrency Control
- When multiple transactions access the same data at the same time, concurrency control is required to maintain data consistency.
- Locks are used to prevent undesirable side-effects:
	- Shared lock (S) - Prevents other transactions from acquiring exclusive locks.
	- Exclusive lock (X) - Prevents other transactions from acquiring any kind of lock.
- Two phase locking is a common concurrency control protocol:
	1. Growing phase - Transactions acquire all locks needed.
	2. Shrinking phase - Transactions release all locks.
- Advantages: Prevents deadlocks and ensures serializability.
- Disadvantages: May reduce concurrency.
- Other techniques: Timestamp ordering, optimistic concurrency control.

[Detailed diagrams, examples, etc. can be included here if helpful for learning]