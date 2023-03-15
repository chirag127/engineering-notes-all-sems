# Conflict & View Serializable Schedule

## Introduction

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if each transaction in it is executed one after another without any interleaving of operations.
- A schedule is non-serial if the operations of different transactions are interleaved.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

## Conflict Serializability

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

- The schedule S is not serial, but it is conflict serializable because it can be transformed into a serial schedule S' by swapping the non-conflicting operations R(B) and W(B) of T1 with R(B) and W(B) of T2:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
|     | R(B) |
|     | W(B) |

- The schedule S' is serial and equivalent to S in terms of the final state of the database.

## View Serializability

- View serializability is another property of a schedule that ensures the consistency of the database.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same set of read operations on each data item that read the same value written by the same transaction.
- For example, consider the following schedule S:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(A) |
|     | W(A) |
| R(B) |    |
| W(B) |    |

- The schedule S is not serial, but it is view serializable because it is view equivalent to a serial schedule S' that executes T1 followed by T2:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | W(A) |

- The schedule S' is serial and view equivalent to S in terms of the initial reads, final writes, and read-write dependencies.

## Summary

- Conflict serializability and view serializability are two types of serializability that ensure the consistency of the database when concurrent transactions are executed.
- Conflict serializability is based on the order of conflicting operations, while view serializability is based on the effect of read and write operations on the database state.
- Every conflict serializable schedule is also view serializable, but the converse is not true.