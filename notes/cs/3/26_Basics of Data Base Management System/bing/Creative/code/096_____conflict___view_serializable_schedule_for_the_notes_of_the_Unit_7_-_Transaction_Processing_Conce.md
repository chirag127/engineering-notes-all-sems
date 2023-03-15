### Conflict and View Serializable Schedule

A schedule is a sequence of operations performed by concurrent transactions on a shared database. A schedule is said to be serializable if it is equivalent to a serial schedule, which means that the transactions are executed one after another without any interleaving. Serial schedules are desirable because they preserve the consistency and isolation of transactions.

There are two types of serializability: conflict serializability and view serializability.

- Conflict serializability: A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. Two operations are said to be conflicting if they belong to different transactions, they operate on the same data item, and at least one of them is a write operation. For example, R1(A) and W2(A) are conflicting, but R1(A) and R2(A) are not. A schedule is conflict serializable if it has the same precedence graph as a serial schedule, where a precedence graph is a directed graph that shows the order of conflicting operations among transactions. A schedule is conflict serializable if and only if its precedence graph is acyclic .

- View serializability: A schedule is view serializable if it is view equivalent to a serial schedule, which means that it preserves the same read and write operations on each data item as a serial schedule. A schedule is view equivalent to another schedule if they satisfy the following conditions  :

  - The initial read operations on each data item are performed by the same transaction in both schedules.
  - The final write operations on each data item are performed by the same transaction in both schedules.
  - The value read by any read operation on a data item is the value written by the same transaction in both schedules.

  For example, the schedule R1(A) W2(A) R2(B) W1(B) is view equivalent to the serial schedule R1(A) W1(B) R2(A) W2(B), but not to the serial schedule R2(A) W2(B) R1(A) W1(B).

  A schedule is view serializable if it is view equivalent to a serial schedule, but not necessarily conflict equivalent. For example, the schedule R1(A) W2(A) R2(A) W1(A) is view serializable, but not conflict serializable, because it has a cycle in its precedence graph. A schedule that is conflict serializable is also view serializable, but not vice versa.

  A schedule that is not serializable is called non-serializable, and it may lead to inconsistency and anomalies in the database. Therefore, serializability is an important property to ensure the correctness and reliability of concurrent transactions.