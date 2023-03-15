### Testing of Serializability

- Serializability is the property of a schedule that ensures the consistency of a database.
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after another without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is based on the order of conflicting operations, such as read-write, write-read, or write-write, on the same data item by different transactions.
- View serializability is based on the read and write operations of each transaction on each data item, regardless of the order of conflicting operations.
- To test for conflict serializability, we can use a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts.
- To test for view serializability, we can use a polygraph, which is a directed graph where the nodes are operations and the edges are dependencies.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A schedule is view serializable if and only if its polygraph is acyclic and has a unique sink node for each data item.