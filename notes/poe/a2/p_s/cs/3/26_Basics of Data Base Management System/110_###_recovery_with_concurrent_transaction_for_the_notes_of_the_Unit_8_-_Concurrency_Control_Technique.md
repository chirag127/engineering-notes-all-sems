 Here is the content in markdown format for the topic ### recovery with concurrent transaction for the notes of the Unit 8 - Concurrency Control Techniques in the subject of Basics of Data Base Management System:

### Recovery with Concurrent Transactions

- When multiple transactions are executing concurrently, it is possible that a system failure may occur leaving the database in an inconsistent state.
- To recover from such failures and bring the database to a consistent state, a recovery procedure is followed.
- The recovery manager uses the log records to undo incomplete transactions and redo committed transactions that were not reflected in the database.
- The issue is more complicated when there are concurrent transactions - the effects of committed transactions may depend on the order in which they are redone. Hence, a careful ordering of redone transactions may be required for serializability.
- Two phase locking is a concurrency control technique that ensures that the scheduling of transactions for concurrency will not affect serializability. So, if all transactions are executed with two-phase locking, then a simple redo of committed transactions in any order will produce a serializable result.
- However, other concurrency control techniques like timestamp ordering do not have this property. For them, a more sophisticated recovery procedure is required that analyzes the transaction read and write sets to determine a recovery schedule that will result in a serializable outcome.

Advantages:
- Ensures database consistency after failures.
- Supports concurrent transactions while maintaining serializability.

Disadvantages:
- Increased complexity of recovery procedures especially for non-two phase locking concurrency control techniques.
- Additional overhead for maintaining logs and carrying out recovery.

[Diagrams and examples can be added here to illustrate the concepts]

Applications: Database management systems implement recovery with concurrency control to provide fault tolerance and data consistency.