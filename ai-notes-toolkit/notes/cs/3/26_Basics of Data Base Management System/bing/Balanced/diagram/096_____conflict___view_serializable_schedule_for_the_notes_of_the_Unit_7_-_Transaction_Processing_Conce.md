### Conflict and View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- Serializability is the property of a schedule that ensures the same outcome as a serial schedule, regardless of the order of operations.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if all conditions satisfy:
  - They belong to different transactions
  - They operate on the same data item
  - At least one of them is a write operation
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- S is conflict serializable because it can be transformed into a serial schedule S' by swapping non-conflicting operations:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- S' is equivalent to the serial schedule T1 -> T2.

#### View Serializability

- A schedule is view serializable if it is view equivalent to a serial schedule, meaning that it preserves the same read-write dependencies as a serial schedule.
- Two schedules are said to be view equivalent if all conditions satisfy:
  - They have the same initial read operations on each data item
  - They have the same final write operations on each data item
  - They have the same update operations on each data item
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

- S is view serializable because it is view equivalent to a serial schedule S' by preserving the same read-write dependencies:

| T1 | T2 |
|----|----|
| R(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | W(A) |
|     | R(B) |
|     | W(B) |

- S' is equivalent to the serial schedule T1 -> T2.