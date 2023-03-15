# Recoverability

Recoverability is a property of transaction schedules that ensures that the database state is consistent even if some transactions fail and are rolled back. A schedule is recoverable if no transaction commits before all the transactions whose changes it has read commit. In other words, a transaction can only depend on the results of committed transactions, not uncommitted ones. This prevents the problem of cascading aborts, where a single transaction failure causes many other transactions to abort as well.

## Types of Recoverability

There are different types of recoverability, depending on the order of commit and abort operations in a schedule. They are:

- **Strict schedules**: These are the schedules where a transaction cannot read or write a data item until the last transaction that wrote it commits or aborts. This ensures that no transaction ever reads a dirty (uncommitted) data item, and that the order of transactions is the same as the order of their commit operations. Strict schedules are always recoverable and also serializable, meaning that they are equivalent to some serial execution of the transactions.

- **Cascading rollback schedules**: These are the schedules where a transaction can read a data item written by an uncommitted transaction, but it cannot commit until that transaction commits. This means that if the transaction that wrote the data item aborts, then all the transactions that read it must also abort and roll back their changes. This can cause a cascade of aborts, which can be costly and inefficient. Cascading rollback schedules are recoverable, but not strict or serializable.

- **Irrecoverable schedules**: These are the schedules where a transaction can read a data item written by an uncommitted transaction, and it can also commit before that transaction commits or aborts. This means that if the transaction that wrote the data item aborts, then the database state becomes inconsistent, as the committed transaction has read a wrong value. Irrecoverable schedules are not recoverable, strict, or serializable, and should be avoided.

## Examples of Recoverability

Consider the following schedule of two transactions T1 and T2, where R(x) denotes reading data item x, W(x) denotes writing data item x, C denotes commit, and A denotes abort:

| T1 | T2 |
|----|----|
| R(A) | |
| | R(A) |
| W(A) | |
| | W(B) |
| C | |
| | C |

This schedule is **irrecoverable**, because T2 commits after reading A, which is written by T1, but before T1 commits. If T1 aborts after T2 commits, then the database state becomes inconsistent.

Consider another schedule of the same transactions:

| T1 | T2 |
|----|----|
| R(A) | |
| | R(A) |
| W(A) | |
| | W(B) |
| | C |
| C | |

This schedule is **recoverable**, but not **strict**, because T2 commits after reading A, which is written by T1, but before T1 commits. However, if T1 aborts after T2 commits, then T2 does not have to abort, because it has not read any dirty data from T1.

Consider a third schedule of the same transactions:

| T1 | T2 |
|----|----|
| R(A) | |
| | R(A) |
| W(A) | |
| | W(B) |
| C | |
| | A |

This schedule is **recoverable** and **strict**, because T2 does not commit before T1 commits, and T2 does not read or write any data item after T1 writes it. This schedule is also **serializable**, because it is equivalent to the serial execution of T1 followed by T2.