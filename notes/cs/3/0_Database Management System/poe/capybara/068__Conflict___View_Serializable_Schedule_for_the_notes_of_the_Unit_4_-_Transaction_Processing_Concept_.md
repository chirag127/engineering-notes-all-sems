### Conflict & View Serializable Schedule

In database management system, a transaction is a set of operations that are executed as a single unit of work. The transaction processing concept is essential for maintaining the consistency, integrity, and reliability of data in a database. 

Two important concepts related to transaction processing are conflict and view serializable schedule. Let's understand them in detail:

#### Conflict Serializable Schedule:

A schedule is conflict serializable if it is equivalent to a serial schedule that could be obtained by interleaving the operations of the given schedule. A schedule is said to have a conflict if two transactions T1 and T2 access the same data item, and at least one of them modifies that data item. 

A schedule can be tested for conflict serializability by constructing a precedence graph. In the precedence graph, each transaction is represented by a node, and an edge is drawn from T1 to T2 if T1 precedes T2 in the schedule and they conflict with each other. If the graph is acyclic, then the schedule is conflict serializable. 

#### View Serializable Schedule:

A schedule is view serializable if it is equivalent to a serial schedule that could be obtained by interleaving the operations of the given schedule, without changing the final result of the transactions. A schedule can be tested for view serializability by constructing a view serializability graph. 

In the view serializability graph, each transaction is represented by a node, and an edge is drawn from T1 to T2 if T2 reads a data item written by T1. If the graph is acyclic, then the schedule is view serializable. 

To summarize, conflict serializability ensures that the database remains consistent, while view serializability guarantees that the final result of the transactions is the same as if they were executed in a serial order. It is important for a database system to ensure both conflict and view serializability to provide a reliable and consistent system for transaction processing.