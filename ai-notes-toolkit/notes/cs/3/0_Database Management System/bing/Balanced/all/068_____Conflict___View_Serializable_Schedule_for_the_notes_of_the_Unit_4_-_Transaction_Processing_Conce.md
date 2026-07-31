# Conflict & View Serializable Schedule

## Conflict Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is called **serial** if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is called **serializable** if it produces the same final state of the database as some serial schedule.
- A schedule is called **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be **conflicting** if all conditions satisfy:
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

- The schedule S is **not serial**, because it interleaves operations from T1 and T2.
- The schedule S is **conflict serializable**, because it can be transformed into a serial schedule S' by swapping non-conflicting operations:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(B) |
|     | W(B) |

- The schedule S' is **serial**, because it executes T1 first and then T2.
- The schedule S' is **equivalent** to S, because it produces the same final state of the database as S.

## View Serializable Schedule

- A schedule is called **view serializable** if it is view equal to a serial schedule.
- Two schedules are said to be **view equal** if the order of initial read, final write and update operations is the same in both the schedules.
- An **initial read** operation is the first read of a data item by any transaction in the schedule.
- A **final write** operation is the last write of a data item by any transaction in the schedule.
- An **update** operation is a read followed by a write of the same data item by the same transaction in the schedule.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- The schedule S is **not serial**, because it interleaves operations from T1 and T2.
- The schedule S is **view serializable**, because it is view equal to a serial schedule S'':

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(A) |
|     | W(A) |

- The schedule S'' is **serial**, because it executes T2 first and then T1.
- The schedule S'' is **view equal** to S, because the order of initial read, final write and update operations is the same in both the schedules:
  - The initial read of A is done by T1 in both S and S''.
  - The final write of A is done by T1 in both S and S''.
  - The update of A is done by T1 in both S and S''.
  - The initial read of B is done by T2 in both S and S''.
  - The final write of B is done by T2 in both S and S''.
  - The update of B is done by T2 in both S and S''.

## Difference between Conflict and View Serializability

- Conflict serializability is a stricter condition than view serializability, because every conflict serializable schedule is also view serializable, but not vice versa.
- Conflict serializability can be checked by using a **precedence graph**, which is a directed graph that represents the order of conflicting operations in a schedule.
- View serializability can be checked by using a **polygraph**, which is a directed graph that represents the order of initial read, final write and update operations in a schedule.
- Conflict serializability is easier to implement and enforce than view serializability, because it