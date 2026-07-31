### Conflict & View Serializable Schedule

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serial if it executes one transaction at a time, without interleaving operations from different transactions.
- A schedule is non-serial if it interleaves operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule in terms of the final state of the database.
- There are two types of serializability: conflict serializability and view serializability.

#### Conflict Serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if all conditions satisfy:
  - They belong to different transactions
  - They operate on the same data item
  - At least one of them is a write operation
- For example, consider the following schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- This schedule is conflict serializable because it can be transformed into a serial schedule by swapping the non-conflicting operations R(B) and W(B) of T1 with R(B) and W(B) of T2. The resulting serial schedule is:

| T2 | T1 |
|----|----|
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | W(A) |
|     | R(B) |
|     | W(B) |

- A schedule can be tested for conflict serializability using a precedence graph, which is a directed graph where the nodes are the transactions and the edges are the conflicts between them.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

#### View Serializability

- A schedule is view serializable if it is view equivalent to some serial schedule, where two schedules are view equivalent if they satisfy the following conditions:
  - They have the same initial read operations on each data item
  - They have the same final write operations on each data item
  - They have the same set of read operations on each data item that read the same value
- For example, consider the following schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
|     | R(A) |
| W(A) |    |
|     | R(B) |
|     | W(B) |
| R(B) |    |
| W(B) |    |

- This schedule is view serializable because it is view equivalent to the serial schedule:

| T1 | T2 |
|----|----|
| R(A) |    |
| W(A) |    |
| R(B) |    |
| W(B) |    |
|     | R(A) |
|     | R(B) |
|     | W(B) |

- Both schedules have the same initial read operations on A and B, the same final write operations on A and B, and the same set of read operations on A and B that read the same value.
- A schedule can be tested for view serializability using a polygraph, which is a directed graph where the nodes are the operations and the edges are the dependencies between them.
- A schedule is view serializable if and only if its polygraph is acyclic and has a serial subgraph that contains all the nodes.