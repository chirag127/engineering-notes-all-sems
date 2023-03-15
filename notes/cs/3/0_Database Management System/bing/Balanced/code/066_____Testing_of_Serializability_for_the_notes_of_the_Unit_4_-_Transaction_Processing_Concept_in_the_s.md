### Testing of Serializability

Serializability is a property of a schedule that ensures the correctness and consistency of a database when multiple transactions are executed concurrently. A schedule is a sequence of operations performed by different transactions on the same data items. A schedule is serializable if it produces the same result as a serial schedule, which is a schedule where transactions are executed one after another without any overlap.

There are two types of serializability: conflict serializability and view serializability.

- Conflict serializability: A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. Two operations are conflicting if they belong to different transactions, operate on the same data item, and at least one of them is a write operation. For example, the schedule S1 below is conflict serializable, as it can be transformed into the serial schedule T1 -> T2 by swapping the non-conflicting operations R2(B) and W1(B).

| S1 | T1 | T2 |
| --- | --- | --- |
| R1(A) | R1(A) | |
| R2(B) | W1(B) | |
| W1(B) | | R2(B) |
| R2(C) | | R2(C) |
| W2(C) | | W2(C) |

- View serializability: A schedule is view serializable if it is view equivalent to a serial schedule. Two schedules are view equivalent if they satisfy the following conditions:

  - The initial read operations on each data item are performed by the same transaction in both schedules.
  - The final write operations on each data item are performed by the same transaction in both schedules.
  - The read operations on each data item see the same value written by the same transaction in both schedules.

  For example, the schedule S2 below is view serializable, as it is view equivalent to the serial schedule T2 -> T1.

| S2 | T1 | T2 |
| --- | --- | --- |
| R1(A) | | R1(A) |
| R2(B) | | R2(B) |
| W2(B) | | W2(B) |
| R1(B) | R1(B) | |
| W1(B) | W1(B) | |
| R2(C) | | R2(C) |
| W2(C) | | W2(C) |

Testing of serializability is an important step in ensuring that concurrent transactions executing in the database do not produce inconsistent or incorrect results. There are two methods widely used to test serializability: conflict graph and precedence graph .

- Conflict graph: A conflict graph is a directed graph that represents the conflicts between the transactions in a schedule. The nodes of the graph are the transactions, and the edges are the conflicts. An edge from Ti to Tj means that Ti has a conflicting operation with Tj and Ti precedes Tj in the schedule. A schedule is conflict serializable if and only if its conflict graph is acyclic. For example, the conflict graph for the schedule S1 above is shown below. It is acyclic, so S1 is conflict serializable.

![Conflict graph for S1](https://www.w3schools.blog/wp-content/uploads/2021/10/Testing-of-Serializability-DBMS-1.png)

- Precedence graph: A precedence graph is a directed graph that represents the dependencies between the transactions in a schedule. The nodes of the graph are the transactions, and the edges are the dependencies. An edge from Ti to Tj means that Ti must precede Tj in any serial schedule that is view equivalent to the given schedule. A schedule is view serializable if and only if its precedence graph is acyclic. For example, the precedence graph for the schedule S2 above is shown below. It is acyclic, so S2 is view serializable.

![Precedence graph for S2](https://www.geeksforgeeks.org/wp-content/uploads/View-Serializability-1.png)

Serializability is a desirable property for a database management system, as it ensures the correctness and consistency of the data. However, testing for serializability can be computationally expensive and may reduce the concurrency and performance of the system. Therefore, some database systems use other techniques, such as locking, timestamping, or multiversion concurrency control, to achieve serializability or a weaker form of consistency.