### Conflict & View Serializable Schedule for the Notes of the Unit 7 - Transaction Processing Concepts in the Subject of Basics of Database Management System

In the world of transaction processing, managing concurrent transactions is of utmost importance. A conflict serializable schedule is a schedule that ensures the same end result as a serial schedule, where transactions are executed one after the other. A view serializable schedule, on the other hand, ensures the same view of the database as a serial schedule. Let's dive deeper into these concepts:

#### Conflict Serializable Schedule

A schedule is considered conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. Two operations are said to conflict if they access the same data item and at least one of them is a write operation. Here are some of the properties of conflict serializable schedules:

- A schedule is conflict serializable if and only if its precedence graph is acyclic.
- Precedence graph is a directed graph where each transaction is a node, and there is an edge from Ti to Tj if an operation in Ti precedes an operation in Tj.
- To test whether a schedule is conflict serializable or not, we construct its precedence graph and check if it is acyclic.

#### View Serializable Schedule

A schedule is considered view serializable if it produces the same result as a serial schedule in terms of the final values seen by the transactions. Here are some of the properties of view serializable schedules:

- A schedule is view serializable if and only if its view serializability graph is acyclic.
- View serializability graph is a directed graph where each transaction is a node, and there is an edge from Ti to Tj if Ti reads a data item that Tj has written.
- To test whether a schedule is view serializable or not, we construct its view serializability graph and check if it is acyclic.

In conclusion, conflict and view serializable schedules are essential concepts in transaction processing. They ensure that concurrent transactions do not interfere with each other and produce the same result as a serial schedule. Understanding these concepts is crucial for designing efficient and reliable database systems.