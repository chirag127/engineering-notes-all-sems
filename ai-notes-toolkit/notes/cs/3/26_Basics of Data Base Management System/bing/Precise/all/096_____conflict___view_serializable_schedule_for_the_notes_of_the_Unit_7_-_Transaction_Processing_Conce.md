# Conflict & View Serializable Schedule

## Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

- A **schedule** is a sequence of operations from a set of transactions.
- A schedule is **conflict serializable** if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be in **conflict** if they belong to different transactions, operate on the same data item, and at least one of them is a write operation.
- A schedule is **view serializable** if it is view equivalent to a serial schedule.
- Two schedules are **view equivalent** if the following conditions hold:
  1. The same set of transactions participate in both schedules.
  2. For any data item, if a transaction reads the initial value of the data item in one schedule, then the same transaction must read the initial value of the data item in the other schedule.
  3. For any data item, if a transaction writes the final value of the data item in one schedule, then the same transaction must write the final value of the data item in the other schedule.
  4. For any data item, if a transaction T reads the value of the data item written by transaction S in one schedule, then transaction T must also read the value of the data item written by transaction S in the other schedule.
- Every conflict serializable schedule is also view serializable, but the converse is not always true.
- Conflict serializability can be checked using a **precedence graph**, while view serializability can be checked using a **polygraph**.