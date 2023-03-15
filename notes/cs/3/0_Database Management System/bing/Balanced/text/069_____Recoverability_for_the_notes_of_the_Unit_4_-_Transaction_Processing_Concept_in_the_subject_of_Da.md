### Recoverability for the notes of the Unit 4 - Transaction Processing Concept in the subject of Database Management System

- Recoverability is the property of a schedule that ensures that the database can be restored to a consistent state after a transaction failure or system crash .
- A schedule is a sequence of operations performed by one or more transactions on the database.
- A transaction is a logical unit of work that accesses and possibly modifies the contents of a database.
- A transaction has four properties: atomicity, consistency, isolation, and durability (ACID).
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that the transaction preserves the internal consistency of the database.
- Isolation means that the execution of a transaction does not interfere with the execution of other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive any system failure.
- A transaction can be in one of the following states: active, partially committed, committed, failed, or aborted.
- Active is the initial state of a transaction, where it is executing its operations.
- Partially committed is the state of a transaction after it has executed its final operation, but before it has committed.
- Committed is the state of a transaction after it has successfully completed and its effects are recorded in the database.
- Failed is the state of a transaction after it has encountered an error that prevents it from continuing its execution.
- Aborted is the state of a transaction after it has been rolled back and its effects are undone from the database.
- A transaction can be aborted either by the system (due to a hardware failure, system crash, or deadlock) or by the user (due to a logical error or cancellation).
- A schedule is recoverable if it ensures that no transaction commits before all the transactions whose changes it has read commit.
- A schedule is irrecoverable if it allows a transaction to commit before some transaction whose changes it has read commits or aborts.
- An irrecoverable schedule can lead to a cascading rollback, where the abort of one transaction causes the abort of other transactions that have read its changes.
- A schedule is cascadeless if it ensures that no transaction reads a data item until the last transaction that has written it commits.
- A cascadeless schedule avoids the problem of cascading rollback and reduces the amount of undo work.
- A schedule is strict if it ensures that no transaction reads or writes a data item until the last transaction that has written it commits.
- A strict schedule is also cascadeless, but it is more restrictive than a cascadeless schedule.
- A strict schedule is desirable for recovery purposes, as it simplifies the undo and redo operations.
- A schedule can be classified into one of the following types, based on its recoverability property:
  - Irrecoverable: A schedule that is not recoverable.
  - Recoverable: A schedule that is recoverable but not cascadeless.
  - Cascadeless: A schedule that is cascadeless but not strict.
  - Strict: A schedule that is strict.
- Example: Consider the following schedule of two transactions T1 and T2, where R(x) denotes reading data item x, W(x) denotes writing data item x, and C denotes commit:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|    | R(A) |
|    | W(A) |
| C  |    |
|    | C  |

- This schedule is irrecoverable, as T2 commits after reading the uncommitted change of T1. If T1 aborts after T2 commits, the database will be inconsistent.
- To make this schedule recoverable, T2 should not commit before T1 commits. For example, the following schedule is recoverable:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|    | R(A) |
|    | W(A) |
|    | C  |
| C  |    |

- To make this schedule cascadeless, T2 should not read A until T1 commits. For example, the following schedule is cascadeless: