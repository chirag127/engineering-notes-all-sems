# Serializability of schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- Serializability is a property of a schedule that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it produces the same effect on the database as some serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read and write operations on the same data item) in a schedule must be ordered in the same way as in some serial schedule.
- View serializability is a weaker form of serializability that requires that any two transactions in a schedule must have the same view of the database as in some serial schedule. A view of a transaction consists of three components: the initial read set, the final write set, and the read-from relation.
- To check whether a schedule is conflict serializable, we can use a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- To check whether a schedule is view serializable, we can use a polygraph, which is a directed graph where the nodes are operations and the edges are view dependencies. A schedule is view serializable if and only if its polygraph is acyclic and has a unique sink node for each data item.
- Serializability is important for concurrency control, which is the mechanism to ensure the isolation and atomicity of transactions in a database system. Concurrency control techniques, such as locking, timestamping, and validation, can enforce serializability by preventing or resolving conflicts among transactions.