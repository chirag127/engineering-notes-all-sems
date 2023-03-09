 Here is the content in markdown format for the topic - Transaction System for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System:

### Transaction System

- A transaction is a logical unit of work that is atomic, consistent, isolated, and durable (ACID).
- Atomic: Either all operations in a transaction are performed or none. If one fails, the entire transaction fails.
- Consistent: A transaction never leaves the database in a half-finished state. If a transaction succeeds, the database moves from one valid state to another. If it fails, the database state is unchanged.
- Isolated: Transactions execute independently and do not interact with each other. The results of an ongoing transaction cannot be affected by others until it is committed.
- Durable: After a transaction commits, its changes persist in the database even if there is a system failure.

- ACID properties are guaranteed by the transaction system which ensures that all database operations are properly synchronized and executed.
- The transaction system tracks all ongoing transactions and coordinates their execution, preventing conflicts and guaranteeing ACID properties. It consists of the following components:
	- Transaction manager: Manages the execution of individual transactions. It coordinates the commit and abort of transactions.
	- Log manager: Maintains a log of all database changes for durability. The log is used to undo transactions in case of aborts and to redo transactions in case of system failures.
	- Lock manager: Manages locks to prevent conflicts between concurrent transactions. It grants locks to transactions and releases locks when transactions end.

- Examples of transactional systems:
	- Database systems
	- File systems
	- Version control systems

- Advantages: Guarantees data consistency and integrity. enables concurrent access and recovery from failures.
- Disadvantages: Additional overhead due to logging and concurrency control, which can impact performance.

[Include diagrams/images/codes/tables etc. if any to explain the concepts]