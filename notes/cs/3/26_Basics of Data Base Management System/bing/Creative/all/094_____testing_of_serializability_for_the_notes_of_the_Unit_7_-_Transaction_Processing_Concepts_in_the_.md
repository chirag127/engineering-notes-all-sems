# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of a database.
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after the other without any overlap.
- Serializability can be tested using two techniques: serialization graph and precedence graph.
- A serialization graph is a directed graph where the nodes represent transactions and the edges represent conflicts between transactions. A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- A schedule is serializable if and only if its serialization graph is acyclic, meaning that it has no cycles. A cycle in the graph indicates that there is a circular dependency between transactions, which violates serial order.
- A precedence graph is a special case of a serialization graph, where the edges are labeled with the type of conflict: read-write (RW), write-read (WR), or write-write (WW). A schedule is serializable if and only if its precedence graph is acyclic.
- To construct a precedence graph for a given schedule, we follow these steps:
  - Create a node for each transaction in the schedule.
  - Scan the schedule from left to right and identify the conflicts between transactions.
  - For each conflict, draw an edge from the transaction that executed earlier to the transaction that executed later, and label it with the type of conflict.
  - Check if the graph has any cycles. If yes, the schedule is not serializable. If no, the schedule is serializable.