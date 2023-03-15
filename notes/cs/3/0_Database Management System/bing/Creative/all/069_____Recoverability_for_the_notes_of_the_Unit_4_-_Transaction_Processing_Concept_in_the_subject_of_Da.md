# Recoverability

Recoverability is a concept in database management systems (DBMS) that refers to the ability of a system to restore the database to a consistent state after a transaction failure or system crash. Recoverability is important for ensuring the integrity and reliability of the data stored in the database.

A transaction is a logical unit of work that consists of a sequence of operations on the database. A transaction can either commit, which means it successfully completes all its operations and makes its changes permanent, or abort, which means it fails to complete and undoes its changes.

A schedule is a sequence of operations from one or more transactions that are executed by the DBMS. A schedule can be classified into different types based on the order of operations and the commit or abort status of the transactions involved.

## Recoverable Schedules

A schedule is recoverable if no transaction in the schedule commits before all the transactions whose changes it has read commit. In other words, a schedule is recoverable if there is no dirty read, which is a situation where a transaction reads a data item that has been modified by another transaction that has not yet committed.

Recoverable schedules ensure that if a transaction aborts, it will not affect the outcome of any other transaction that has committed. Recoverable schedules are desirable because they prevent the loss of committed data and avoid cascading aborts, which are situations where the abort of one transaction causes the abort of other transactions that have read its changes.

Example:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(B) |
| W(A) |    |
|    | W(B) |
| C |    |
|    | C |

This schedule is recoverable because T1 commits after reading A and T2 commits after reading B, and both A and B are written by committed transactions.

## Non-recoverable Schedules

A schedule is non-recoverable if there is at least one transaction in the schedule that commits before all the transactions whose changes it has read commit. In other words, a schedule is non-recoverable if there is at least one dirty read.

Non-recoverable schedules are problematic because they can lead to inconsistent states of the database if a transaction that has been read by another transaction aborts. Non-recoverable schedules can also cause cascading aborts, which can affect the performance and availability of the system.

Example:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(A) |
| W(A) |    |
|    | C |
| A |    |

This schedule is non-recoverable because T2 commits after reading A, which is written by T1, and T1 aborts. This means that T2 has committed a change that is based on an invalid value of A, and the database is in an inconsistent state. Moreover, T2 has to abort as well, causing a cascading abort.