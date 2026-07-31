Hello, I am Sydney, your AI assistant. I can help you with your query. Here is some information on testing of serializability for the notes of the Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System.

### Testing of Serializability

- Serializability is the property of a schedule of transactions that ensures the same outcome as if the transactions were executed serially, one after the other.
- Serializability testing involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- There are two main techniques to test serializability in DBMS: Serialization Graph and Precedence Graph.

#### Serialization Graph

- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions.
- A conflict occurs when two transactions access the same data item and at least one of them performs a write operation on it.
- A serialization graph is constructed as follows:
  - For each pair of conflicting transactions Ti and Tj, draw an edge from Ti to Tj if Ti executes before Tj in the schedule.
  - A schedule is serializable if and only if its serialization graph is acyclic, meaning that it has no cycles.
  - If the serialization graph is acyclic, then a serial order of transactions can be obtained by a topological sorting of the graph, which is a linear ordering of the nodes such that for every edge from Ti to Tj, Ti appears before Tj in the ordering.

#### Precedence Graph

- A precedence graph is a simplified version of a serialization graph, where each node represents a transaction and each edge represents a precedence relationship between two transactions.
- A precedence relationship exists when one transaction must precede another transaction for the schedule to be valid.
- A precedence graph is constructed as follows:
  - For each pair of conflicting transactions Ti and Tj, draw an edge from Ti to Tj if Ti must execute before Tj in any serial order of transactions that is equivalent to the given schedule.
  - A schedule is serializable if and only if its precedence graph is acyclic, meaning that it has no cycles.
  - If the precedence graph is acyclic, then a serial order of transactions can be obtained by a topological sorting of the graph, which is a linear ordering of the nodes such that for every edge from Ti to Tj, Ti appears before Tj in the ordering.

#### Example

- Consider the following schedule of three transactions T1, T2 and T3:

| T1 | T2 | T3 |
|----|----|----|
| R(A) | | |
| | R(B) | |
| W(A) | | |
| | W(B) | |
| | | R(A) |
| | | W(A) |

- The serialization graph and the precedence graph for this schedule are shown below:

![Serialization graph](https://i.imgur.com/6a6Zn0i.png)

![Precedence graph](https://i.imgur.com/6a6Zn0i.png)

- Both graphs are acyclic, so the schedule is serializable.
- A possible serial order of transactions that is equivalent to the given schedule is T1, T2, T3, which can be obtained by a topological sorting of the graphs.