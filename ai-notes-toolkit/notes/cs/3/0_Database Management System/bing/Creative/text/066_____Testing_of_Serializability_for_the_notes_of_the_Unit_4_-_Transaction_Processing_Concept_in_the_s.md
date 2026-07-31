### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stronger notion of serializability that requires that any two conflicting operations (read or write on the same data item) of two transactions in a schedule must have the same order as in some serial schedule.
- View serializability is a weaker notion of serializability that requires that any two transactions in a schedule must have the same read and write operations on the same data items as in some serial schedule, but not necessarily the same order of conflicting operations.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph or a precedence graph is a directed graph of the transactions in a schedule, where an edge from transaction Ti to transaction Tj indicates that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its serialization graph is acyclic, meaning that it does not contain any cycles of edges.
- A schedule is view serializable if and only if it is conflict serializable or it can be transformed into a conflict serializable schedule by swapping non-conflicting operations.
- To construct a serialization graph for a given schedule, we follow these steps:
  - Create a node for each transaction in the schedule.
  - For each pair of conflicting operations (read or write on the same data item) of two transactions Ti and Tj in the schedule, draw an edge from Ti to Tj if Ti appears before Tj in the schedule.
  - Check if the graph is acyclic. If yes, then the schedule is conflict serializable and the serial order of transactions is given by the topological sorting of the graph. If no, then the schedule is not conflict serializable and may or may not be view serializable.
- To check if a schedule is view serializable, we can use the following algorithm:
  - Construct the serialization graph for the schedule as described above.
  - If the graph is acyclic, then the schedule is view serializable and the serial order of transactions is given by the topological sorting of the graph.
  - If the graph is cyclic, then check if the cycle can be broken by swapping non-conflicting operations of adjacent transactions in the cycle. If yes, then the schedule is view serializable and the serial order of transactions is given by the topological sorting of the modified graph. If no, then the schedule is not view serializable.
- Example: Consider the following schedule of three transactions T1, T2 and T3:

| T1 | T2 | T3 |
|----|----|----|
| R(A) |    |    |
| W(A) |    |    |
|     | R(B) |    |
|     | W(B) |    |
|     |    | R(A) |
|     |    | W(A) |
|     |    | R(B) |
|     |    | W(B) |

- To test the serializability of this schedule, we construct the serialization graph as follows:

![serialization graph](https://i.imgur.com/2QyQ0x4.png)

- The graph is cyclic, so the schedule is not conflict serializable. However, we can swap the non-conflicting operations R(A) and W(A) of T1 and T3 in the cycle to break the cycle and obtain the following modified schedule:

| T1 | T2 | T3 |
|----|----|----|
|     |    | R(A) |
|     |    | W(A) |
| R(A) |    |    |
| W(A) |    |    |
|     | R(B) |    |
|     | W(B) |    |
|     |    | R(B) |
|     |    | W(B) |

- The serialization graph for the modified schedule is as follows:

![modified serialization graph](https://i.imgur.com/6wZ6q3v.png)

- The graph is ac