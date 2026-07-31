Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on testing of serializability for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System.

### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any overlap.
- There are two main techniques to test the serializability of a schedule: serialization graph and precedence graph.
- A serialization graph is a directed graph that represents the conflicts between the transactions in a schedule. A conflict occurs when two transactions access the same data item and at least one of them performs a write operation.
- A node in the serialization graph corresponds to a transaction, and an edge from Ti to Tj indicates that Ti has to finish before Tj can start, due to some conflict.
- A schedule is serializable if and only if its serialization graph is acyclic, meaning that it does not contain any directed cycles.
- A precedence graph is a special case of a serialization graph, where the edges are drawn only for the first conflict between any pair of transactions. The precedence graph captures the essential ordering constraints among the transactions in a schedule.
- A schedule is serializable if and only if its precedence graph is acyclic, meaning that it does not contain any directed cycles.
- To construct a precedence graph for a given schedule, we follow these steps:
  - Create a node for each transaction in the schedule.
  - Scan the schedule from left to right, and for each pair of conflicting operations, draw an edge from the transaction that performed the earlier operation to the transaction that performed the later operation.
  - Check if the graph contains any cycles. If yes, the schedule is not serializable. If no, the schedule is serializable, and a possible serial order of the transactions can be obtained by a topological sorting of the graph.

Here is an example of a schedule and its precedence graph:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
| W(A) |    |    |
|     | R(B) |    |
|     | W(B) |    |
|     |    | R(A) |
|     |    | W(A) |
| R(B) |    |    |
| W(B) |    |    |
| C   | C  | C  |

The precedence graph for this schedule is:

```
T1 --> T2 --> T3
 ^           /
  \_________/
```

The graph contains a cycle, so the schedule is not serializable.