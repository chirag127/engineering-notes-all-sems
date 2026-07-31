### Serializability of Schedules

- Serializability is a property of a schedule that ensures the consistency of a database.
- A schedule is a sequence of operations from one or more transactions.
- A schedule is serializable if it is equivalent to a serial schedule, where transactions are executed one after the other.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is when two schedules are conflict equivalent, meaning they have the same order of conflicting operations.
- View serializability is when two schedules are view equivalent, meaning they have the same set of read and write operations on the same data items.
- Checking for serializability can be done using a precedence graph or a conflict graph.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A schedule is view serializable if and only if its conflict graph is acyclic.
- Serializability is important to ensure the consistency and correctness of a database.
