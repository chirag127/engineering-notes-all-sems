### Conflict and View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if they satisfy all the following conditions:
  - They belong to different transactions.
  - They operate on the same data item.
  - At least one of them is a write operation.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- The schedule S is not serial, as it interleaves operations from T1 and T2.
- The schedule S is conflict serializable, as it can be transformed into a serial schedule S' by swapping non-conflicting operations:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial and equivalent to S in terms of the final state of the database.
- A conflict serializable schedule preserves the order of conflicting operations in the serial schedule.

#### View Serializability

- A schedule is view serializable if it is view equivalent to some serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same update operations on each data item by the same transaction.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S is not serial, as it interleaves operations from T1 and T2.
- The schedule S is view serializable, as it is view equivalent to a serial schedule S' as follows:

| T1 | T2 |
|----|----|
| R(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | W(A) |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial and equivalent to S in terms of the initial and final views of the database.
- A view serializable schedule may not preserve the order of conflicting operations in the serial schedule.

#### Difference between Conflict and View Serializability

- Conflict serializability is a stricter criterion than view serializability, as every conflict serializable schedule is also view serializable, but not vice versa.
- Conflict serializability can be checked by constructing a precedence graph of the transactions and testing for cycles, whereas view serializability requires testing for view equivalence with all possible serial schedules, which is computationally expensive.
- Conflict serializability ensures that the concurrent execution of transactions is equivalent to some serial order of the transactions, whereas view serializability ensures that the concurrent execution of transactions produces the same view of the database as some serial order of the transactions.