### Conflict & View Serializable Schedule

#### Unit 4 - Transaction Processing Concept in the subject of Database Management System

- A **conflict serializable schedule** is a schedule whose effect on any consistent database state is guaranteed to be the same as that of some serial schedule of the same transactions.
- A **view serializable schedule** is a schedule that is view equivalent to a serial schedule.
- **View equivalence** between two schedules means that the same set of transactions reads and writes the same set of data items in both schedules.
- A schedule is **view serializable** if it is view equivalent to a serial schedule.
- A schedule is **conflict serializable** if the precedence graph is acyclic.
- A **precedence graph** is a directed graph where the nodes represent committed transactions and the edges represent conflicts between transactions.
- A **conflict** between two transactions occurs when one transaction reads or writes a data item that was previously written by another transaction.
- A **serial schedule** is a schedule in which transactions are executed one after the other, without any overlap in time.
- A **schedule** is an ordering of the operations of a set of transactions.
- **Transaction processing** is the process of managing transactions in a database management system.
