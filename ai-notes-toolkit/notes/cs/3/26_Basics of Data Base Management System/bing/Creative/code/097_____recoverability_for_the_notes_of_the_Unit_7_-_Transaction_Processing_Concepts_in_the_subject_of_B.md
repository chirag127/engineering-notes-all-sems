### Recoverability in Transaction Processing

- Recoverability is the property of a schedule that ensures that the database state is consistent after a transaction failure or system crash .
- A schedule is recoverable if no transaction commits before all the transactions whose changes it has read commit .
- A schedule is irrecoverable if some transaction commits after reading the changes made by another transaction that has not committed yet .
- Irrecoverable schedules can lead to inconsistent database states if the transaction that has not committed yet aborts or fails .
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
| W(A) |    |
|    | W(A) |
|    | C |
| A |    |

- A schedule is cascading abort if some transaction aborts and causes other transactions that have read its changes to abort as well.
- Cascading aborts can lead to loss of work and high overhead of rolling back multiple transactions.
- A schedule is cascadeless if no transaction reads the changes made by another transaction that has not committed yet.
- Cascadeless schedules are always recoverable and avoid cascading aborts.
- Example of a cascading abort schedule:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
|    | R(A) |    |
| W(A) |    |    |
|    |    | R(A) |
|    | W(A) |    |
|    |    | W(A) |
| A |    |    |
|    | A |    |
|    |    | A |

- Example of a cascadeless schedule:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
| W(A) |    |    |
| C |    |    |
|    | R(A) |    |
|    | W(A) |    |
|    | C |    |
|    |    | R(A) |
|    |    | W(A) |
|    |    | C |

- To ensure recoverability and avoid cascading aborts, a transaction processing system can use a locking protocol that enforces strict two-phase locking (2PL) .
- Strict 2PL requires that a transaction releases all its locks only after it commits or aborts, and that no transaction can read or write a data item that is locked by another transaction .
- Strict 2PL guarantees that the commit order of transactions is the same as their lock release order, and that no transaction reads uncommitted data .
- Example of a strict 2PL schedule:

| T1 | T2 |
|----|----|
| lock(A) |    |
| R(A) |    |
| W(A) |    |
|    | lock(A) |
|    | wait |
| C |    |
| unlock(A) |    |
|    | R(A) |
|    | W(A) |
|    | C |
|    | unlock(A) |