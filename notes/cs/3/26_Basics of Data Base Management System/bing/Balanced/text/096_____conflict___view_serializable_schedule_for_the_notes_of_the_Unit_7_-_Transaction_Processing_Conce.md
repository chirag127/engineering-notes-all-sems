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

- The schedule S is conflict serializable because it can be transformed into a serial schedule S' by swapping the non-conflicting operations R(B) and W(B) of T1 with R(B) and W(B) of T2:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(B) |
|     | W(B) |

- The schedule S' is equivalent to the serial schedule T1 -> T2.

#### View Serializability

- A schedule is view serializable if it is view equivalent to a serial schedule, meaning that it preserves the following conditions:
  - The same transaction reads the initial value of each data item
  - The same transaction writes the final value of each data item
  - The same transaction reads the value of each data item that has been written by another transaction
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |

- The schedule S is view serializable because it is view equivalent to the serial schedule T2 -> T1, which satisfies the following conditions:
  - T1 reads the initial value of B
  - T2 reads the initial value of A
  - T2 writes the final value of A
  - T1 writes the final value of B
  - T2 reads the value of A written by T1
- Note that the schedule S is not conflict serializable because it cannot be transformed into a serial schedule by swapping non-conflicting operations, as all the operations are conflicting.