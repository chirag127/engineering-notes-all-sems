### Conflict & View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions, which may lead to inconsistency or anomalies in the database.
- Serializability is the property of a schedule that ensures the same outcome as a serial schedule, i.e., the same final state of the database and the same values returned by read operations.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- Conflict serializability is a type of serializability that checks if a non-serial schedule is conflict equivalent to a serial schedule, i.e., if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if they satisfy all the following conditions:
  - They belong to different transactions.
  - They operate on the same data item.
  - At least one of them is a write operation.
- For example, R1(X) and W2(X) are conflicting operations, but R1(X) and R2(X) are not.
- A schedule is conflict serializable if it preserves the order of all conflicting operations in the serial schedule.
- For example, the schedule R1(X) W1(X) R2(X) W2(X) is conflict serializable, as it is conflict equivalent to the serial schedule T1 T2.
- Conflict serializability can be checked by using a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts. A schedule is conflict serializable if and only if its precedence graph is acyclic.

#### View Serializability

- View serializability is a type of serializability that checks if a non-serial schedule is view equivalent to a serial schedule, i.e., if it produces the same view of the database as a serial schedule.
- Two schedules are said to be view equivalent if they satisfy all the following conditions:
  - They have the same initial read operations on each data item, i.e., the same transaction reads the initial value of each data item in both schedules.
  - They have the same final write operations on each data item, i.e., the same transaction writes the final value of each data item in both schedules.
  - They have the same update operations on each data item, i.e., the same transaction reads the value written by the same transaction in both schedules.
- For example, the schedule R1(X) W1(X) R2(X) W2(X) is view serializable, as it is view equivalent to the serial schedule T1 T2.
- View serializability is a more general notion than conflict serializability, as every conflict serializable schedule is also view serializable, but not vice versa.
- View serializability can be checked by using a polygraph, which is a directed graph where the nodes are operations and the edges are dependencies. A schedule is view serializable if and only if its polygraph is acyclic.