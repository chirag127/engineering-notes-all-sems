### Conflict & View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- Conflict serializability is a property of a schedule that ensures the consistency of the database.
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
- Therefore, S is conflict serializable.

#### View Serializability

- View serializability is another property of a schedule that ensures the consistency of the database.
- A schedule is view serializable if it is view equivalent to some serial schedule, meaning that it preserves the following conditions:
  - The same transaction performs the initial read of each data item in both schedules.
  - The same transaction performs the final write of each data item in both schedules.
  - The same set of values are read and written for each data item in both schedules.
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
- The schedule S is not conflict serializable, as it cannot be transformed into a serial schedule by swapping non-conflicting operations.
- However, the schedule S is view serializable, as it is view equivalent to the following serial schedule S'':

| T1 | T2 |
|----|----|
|     | R(A) |
|     | W(A) |
|     | R(B) |
|     | W(B) |
| R(A) |    |
| R(B) |    |
| W(B) |    |

- The schedule S'' is serial and preserves the view conditions of S, as follows:
  - The same transaction (T1) performs the initial read of A in both schedules.
  - The same transaction (T2) performs the final write of A in both schedules.
  - The same transaction (T1) performs the initial read of B in both schedules.
  - The same transaction (T2) performs the final write of B in both schedules.
  - The same set of values are read and written for A and B in both schedules.
- Therefore, S is view serializable.