### Recoverability in Transaction Processing
- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash .
- A schedule is recoverable if no transaction commits before all the transactions whose changes it has read commit .
- A schedule is irrecoverable if some transaction commits after reading the changes made by another transaction that has not committed yet .
- Irrecoverable schedules can lead to inconsistency in the database state if the transaction that has not committed yet aborts or fails .
- Example of a recoverable schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(A) |
| W(A) |    |
|    | W(A) |
| C |    |
|    | C |

- Example of an irrecoverable schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
|    | R(A) |
|    | W(A) |
|    | C |
| W(A) |    |
| A |    |

- There are different types of recoverable schedules, such as cascadeless schedules and strict schedules.
- A cascadeless schedule is a recoverable schedule in which no transaction reads a data item unless the transaction that last wrote it has committed.
- A strict schedule is a recoverable schedule in which no transaction reads or writes a data item unless the transaction that last wrote it has committed.
- Cascadeless and strict schedules prevent cascading aborts, which are a chain of aborts caused by the failure of one transaction.
- Example of a cascadeless schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| C |    |
|    | R(A) |
|    | W(A) |
|    | C |

- Example of a strict schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|    | R(A) |
|    | W(A) |
| C |    |
|    | C |

- Recoverability is an important concept in transaction processing systems, as it ensures the consistency and durability of the database state .
- Recoverability can be achieved by using various techniques, such as logging, checkpoints, shadow paging, and locking .