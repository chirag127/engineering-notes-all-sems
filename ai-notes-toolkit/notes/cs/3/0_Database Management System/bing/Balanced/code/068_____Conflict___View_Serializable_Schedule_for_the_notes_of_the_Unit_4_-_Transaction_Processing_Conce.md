### Conflict & View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- Serializability is the property of a schedule that ensures the same effect on the database as a serial schedule.
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

- The schedule S is conflict serializable because it can be transformed into a serial schedule S' by swapping non-conflicting operations:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S' is equivalent to the serial schedule <T1, T2>.
- A conflict serializable schedule preserves the order of conflicting operations in a serial schedule.

#### View Serializability

- A schedule is view serializable if it is view equivalent to a serial schedule.
- Two schedules are said to be view equivalent if the order of initial read, final write and update operations is the same in both the schedules.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- The schedule S is view serializable because it is view equivalent to the serial schedule S' = <T1, T2>.
- The schedule S and S' have the same initial read (T1 reads A), final write (T2 writes B) and update operations (T1 updates A and B, T2 updates B).
- A view serializable schedule preserves the effect of read and write operations on the database as a serial schedule.

#### Difference between Conflict and View Serializability

- Conflict serializability is a stricter criterion than view serializability, meaning that every conflict serializable schedule is also view serializable, but not vice versa.
- Conflict serializability can be checked by using a precedence graph, which is a directed graph that represents the order of conflicting operations in a schedule. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- View serializability is harder to check than conflict serializability, as it requires comparing a schedule with all possible serial schedules to find a view equivalent one. There is no efficient algorithm to test view serializability.