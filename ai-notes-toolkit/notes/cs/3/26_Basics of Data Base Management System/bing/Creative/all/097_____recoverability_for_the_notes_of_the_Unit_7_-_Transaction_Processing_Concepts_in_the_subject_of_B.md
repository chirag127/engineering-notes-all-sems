# Recoverability in Transaction Processing

- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash.
- A schedule is recoverable if it does not contain any dirty read, which is when a transaction reads a data item that is updated by another uncommitted transaction.
- A schedule is irrecoverable if it contains a dirty read and the transaction that performs the dirty read commits before the transaction that updates the data item.
- Irrecoverable schedules can lead to inconsistent database states if the transaction that updates the data item aborts after the other transaction commits.
- Example of an irrecoverable schedule:

| T1 | T2 |
|----|----|
| W(A) |    |
|     | R(A) |
|     | C |
| A | |

- In this schedule, T2 reads the value of A that is written by T1, but T1 aborts later. T2 has already committed, so it cannot undo its changes. The database state is inconsistent because it reflects the changes of an aborted transaction.
- A schedule is cascadingly recoverable if it is recoverable and the transactions that read the data items updated by an aborted transaction also abort.
- Cascadingly recoverable schedules can avoid inconsistent database states, but they can cause a lot of wasted work and delays due to cascading aborts.
- Example of a cascadingly recoverable schedule:

| T1 | T2 | T3 |
|----|----|----|
| W(A) |    |    |
|     | R(A) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(C) |
| A |    |    |
|     | A |    |
|     |    | A |

- In this schedule, T1 aborts and causes T2 to abort, which in turn causes T3 to abort. All the transactions that read the data items updated by T1 have to abort and undo their changes. The database state is consistent, but a lot of work is lost and the transactions have to restart.
- A schedule is strictly recoverable if it is recoverable and the transactions that update the data items commit only after all the transactions that read those data items commit.
- Strictly recoverable schedules can avoid inconsistent database states and cascading aborts, but they can reduce the concurrency and performance of the system.
- Example of a strictly recoverable schedule:

| T1 | T2 | T3 |
|----|----|----|
| W(A) |    |    |
|     | R(A) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(C) |
|     |    | C |
|     | C |    |
| C |    |    |

- In this schedule, T1 commits only after T2 and T3 commit, and T2 commits only after T3 commits. All the transactions that update the data items commit after all the transactions that read those data items commit. The database state is consistent and no cascading aborts occur. However, the transactions have to wait for each other to commit, which can reduce the concurrency and performance of the system.