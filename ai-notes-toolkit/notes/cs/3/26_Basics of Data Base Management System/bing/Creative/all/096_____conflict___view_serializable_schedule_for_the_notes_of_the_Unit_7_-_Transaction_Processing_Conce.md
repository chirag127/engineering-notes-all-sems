# Conflict and View Serializable Schedule

## Introduction

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

## Conflict Serializability

- Conflict serializability is a property of a schedule that ensures the same order of conflicting operations as a serial schedule.
- Two operations are said to be conflicting if they satisfy all the following conditions:
  - They belong to different transactions.
  - They operate on the same data item.
  - At least one of them is a write operation.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- A schedule is conflict equivalent to another schedule if they have the same order of conflicting operations.
- Conflict serializability can be checked by constructing a precedence graph of the transactions in the schedule and checking if it is acyclic.

## View Serializability

- View serializability is a property of a schedule that ensures the same effect on the database as a serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item.
  - They have the same final write operations on each data item.
  - They have the same update operations on each data item.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- A schedule is view equivalent to another schedule if they have the same view on the database.
- View serializability can be checked by comparing the initial read, final write and update operations of the schedules.