### Serializability of schedules

- A schedule is a sequence of operations performed by one or more transactions on a database.
- A schedule is serializable if it produces the same result as a serial schedule, which is a schedule where transactions are executed one after the other without any overlap.
- Serializability is a desirable property of schedules because it ensures consistency and isolation of transactions, which are two of the ACID properties of database systems.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read or write on the same data item) in a schedule must have the same order as in a serial schedule.
- View serializability is a weaker form of serializability that requires that any read operation in a schedule must see the same value as in a serial schedule, and any write operation in a schedule must update the same final value as in a serial schedule.
- Conflict serializability can be checked by using a precedence graph, which is a directed graph where nodes are transactions and edges are conflicts. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- View serializability can be checked by using a polygraph, which is a directed graph where nodes are operations and edges are dependencies. A schedule is view serializable if and only if its polygraph is acyclic.