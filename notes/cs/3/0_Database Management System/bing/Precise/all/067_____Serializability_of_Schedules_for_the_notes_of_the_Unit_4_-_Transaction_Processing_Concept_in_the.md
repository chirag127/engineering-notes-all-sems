# Serializability of Schedules

Serializability is a concept in transaction processing that refers to the ability to execute multiple transactions concurrently while maintaining the consistency of the database. In other words, the result of executing multiple transactions concurrently should be the same as if they were executed one after the other in some order.

There are two types of serializability: conflict serializability and view serializability.

- **Conflict serializability** is achieved when the order of conflicting operations in two transactions is the same as if the transactions were executed serially. Conflicting operations are those that access the same data item and at least one of them is a write operation.

- **View serializability** is achieved when the transactions have the same effect on the database as if they were executed serially. This means that the transactions read the same data items and write the same data items in the same order as if they were executed serially.

To determine if a schedule is serializable, a precedence graph can be constructed. In this graph, the nodes represent the transactions and the edges represent the order in which the transactions must be executed. If the graph contains no cycles, then the schedule is serializable.

In summary, serializability is an important concept in transaction processing that ensures the consistency of the database when multiple transactions are executed concurrently. There are two types of serializability: conflict serializability and view serializability, and a precedence graph can be used to determine if a schedule is serializable.