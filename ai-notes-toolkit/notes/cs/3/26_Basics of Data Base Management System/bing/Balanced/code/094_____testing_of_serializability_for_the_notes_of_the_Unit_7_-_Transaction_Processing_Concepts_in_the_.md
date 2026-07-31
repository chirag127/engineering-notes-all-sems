### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the same outcome as if the transactions were executed serially, one after the other.
- Serializability is important for maintaining the consistency and correctness of a database in a concurrent environment.
- There are two main techniques for testing the serializability of a schedule: serialization graph and precedence graph.
- A serialization graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between the transactions. A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- A schedule is serializable if and only if its serialization graph is acyclic, meaning that there is no cycle in the graph. A cycle in the graph implies that there is a circular dependency among the transactions, which violates the serial order.
- A precedence graph is a special case of a serialization graph where the edges are drawn only from the earlier transaction to the later transaction in the schedule. A precedence graph preserves the order of conflicting operations in the schedule.
- A schedule is serializable if and only if its precedence graph is acyclic, meaning that there is no cycle in the graph. A cycle in the graph implies that there is a contradiction in the order of conflicting operations, which violates the serial order.
- An example of a schedule and its precedence graph is shown below:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
|    | R(A) |    |
| W(A) |    |    |
|    |    | R(A) |
|    | W(A) |    |
|    |    | W(A) |

![Precedence graph](https://www.w3schools.blog/wp-content/uploads/2020/12/Precedence-Graph-1.png)

- The schedule is not serializable because its precedence graph has a cycle: T1 -> T2 -> T3 -> T1. This means that there is no serial order that is equivalent to the concurrent execution of the transactions.