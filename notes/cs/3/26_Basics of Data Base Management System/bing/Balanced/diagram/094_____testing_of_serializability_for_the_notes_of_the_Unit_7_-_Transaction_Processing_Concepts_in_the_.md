### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any interleaving of operations.
- There are two main techniques to test the serializability of a schedule: serialization graph and precedence graph.
- A serialization graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between the transactions. A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- A schedule is serializable if and only if its serialization graph is acyclic, meaning that there is no cycle in the graph. If there is a cycle, then the schedule is not serializable and may lead to inconsistency or anomaly in the database state.
- A precedence graph is a special case of a serialization graph where the edges are drawn only between the conflicting operations, not the transactions. A schedule is serializable if and only if its precedence graph is acyclic, meaning that there is no cycle in the graph. If there is a cycle, then the schedule is not serializable and may lead to inconsistency or anomaly in the database state.
- The advantage of using a precedence graph over a serialization graph is that it is more compact and easier to construct and analyze. However, both techniques are equivalent in terms of testing the serializability of a schedule.
- An example of a schedule and its serialization graph and precedence graph is shown below:

| T1 | T2 | T3 |
|----|----|----|
| R(A) | | |
| | R(B) | |
| W(A) | | |
| | W(B) | |
| | | R(A) |
| | | W(A) |

![Serialization graph](https://i.imgur.com/9yYfYyN.png)

![Precedence graph](https://i.imgur.com/6m7lZbX.png)

- The schedule is not serializable because both graphs have a cycle involving T1, T2, and T3. This means that the schedule may produce a different result than any serial schedule, and may violate the consistency and correctness of the database state.