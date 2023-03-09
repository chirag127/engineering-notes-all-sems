### Conflict & View Serializable Schedule

In transaction processing, the concept of serializability is very important. A schedule is considered serializable if it produces the same result as a serial schedule. In this context, we will discuss two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

A schedule is conflict serializable if it does not create any conflicts between transactions. A conflict occurs when two transactions try to access and modify the same data item, and at least one of them tries to write the data. There are two types of conflicts: read-write and write-write conflicts.

- **Read-Write Conflicts**: If a transaction tries to read a data item that another transaction is writing to, then a read-write conflict occurs. In this case, the transaction that is reading has to wait until the transaction that is writing finishes.

- **Write-Write Conflicts**: If two transactions try to write to the same data item, then a write-write conflict occurs. In this case, one of the transactions has to wait until the other transaction finishes.

To check if a schedule is conflict serializable, we can use the concept of precedence graph. A precedence graph is a directed graph that shows the order of execution of transactions. If the graph is acyclic, then the schedule is conflict serializable.

#### View Serializability

A schedule is view serializable if it produces the same result as a serial schedule, when viewed from each transaction's point of view. In other words, the order of execution of transactions does not affect the final result.

To check if a schedule is view serializable, we can use the concept of view equivalence. Two schedules are view equivalent if they produce the same result, when viewed from each transaction's point of view. If two schedules are view equivalent, then they are also conflict serializable.

In conclusion, conflict and view serializability are important concepts in transaction processing. They ensure that the order of execution of transactions does not affect the final result, and that there are no conflicts between transactions. The use of precedence graphs and view equivalence can help us determine whether a schedule is conflict or view serializable.