### Recoverability

Recoverability is the property of a transaction schedule that ensures that the database state is consistent after a transaction failure or system crash. A transaction schedule is a sequence of operations performed by one or more transactions on the database.

A transaction schedule is recoverable if it does not contain any dirty read. A dirty read is a situation where a transaction reads a data item that has been modified by another transaction that has not yet committed or aborted. If the transaction that modified the data item aborts, then the transaction that read the data item will have an incorrect value.

A transaction schedule is irrecoverable if it contains a dirty read. An irrecoverable schedule can lead to inconsistency in the database state if the transaction that performed the dirty read commits before the transaction that modified the data item.

An example of an irrecoverable schedule is:

| T1 | T2 |
|----|----|
| W(A) |    |
|     | R(A) |
|     | W(B) |
|     | C |
| A |    |

In this schedule, T2 reads the value of A that has been modified by T1, but T1 has not yet committed or aborted. This is a dirty read. If T1 aborts, then the value of A will be restored to its original value, but T2 has already committed with the modified value of A. This can lead to inconsistency in the database state.

To avoid irrecoverable schedules, we can use the following rules:

- A transaction can read a data item only if it has not been modified by any uncommitted transaction.
- A transaction can commit only after all the transactions whose changes it has read have committed.

A transaction schedule that follows these rules is called a cascading rollback schedule. A cascading rollback schedule is recoverable, but it can still cause a lot of overhead if a transaction aborts. All the transactions that have read the changes of the aborted transaction will have to rollback and restart. This can affect the performance and concurrency of the system.

An example of a cascading rollback schedule is:

| T1 | T2 | T3 |
|----|----|----|
| W(A) |    |    |
|     | R(A) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(C) |
| A |    |    |
|     | R(A) |    |
|     | A |    |
|     |    | R(B) |
|     |    | A |

In this schedule, T1 aborts after modifying A. T2 and T3 have read the changes of T1, so they have to rollback and restart. This is a cascading rollback.

To avoid cascading rollback schedules, we can use the following rule:

- A transaction can read a data item only if it has been modified by a committed transaction.

A transaction schedule that follows this rule is called a strict schedule. A strict schedule is recoverable and does not cause any cascading rollback. A strict schedule ensures that a transaction can only see the changes of committed transactions.

An example of a strict schedule is:

| T1 | T2 | T3 |
|----|----|----|
| W(A) |    |    |
| C |    |    |
|     | R(A) |    |
|     | W(B) |    |
|     | C |    |
|     |    | R(B) |
|     |    | W(C) |
|     |    | C |

In this schedule, T1, T2 and T3 commit after modifying A, B and C respectively. No transaction reads the changes of an uncommitted transaction. This is a strict schedule.

Recoverability is an important concept in transaction processing systems, as it ensures the consistency and integrity of the database state. Recoverability can be achieved by following certain rules that prevent dirty reads and cascading rollbacks. Strict schedules are the most desirable type of recoverable schedules, as they do not cause any overhead or performance issues.