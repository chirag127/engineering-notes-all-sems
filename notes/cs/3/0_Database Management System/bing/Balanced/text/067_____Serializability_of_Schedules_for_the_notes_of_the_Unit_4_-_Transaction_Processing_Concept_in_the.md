### Serializability of Schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- Serializability is a desirable property of a schedule because it ensures that concurrent transactions do not interfere with each other and preserve the consistency and correctness of the database.
- There are two main types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stronger notion of serializability that requires that the order of conflicting operations (read-write, write-read, or write-write) in a schedule is the same as in a serial schedule. Two schedules are conflict equivalent if they have the same order of conflicting operations.
- View serializability is a weaker notion of serializability that requires that the read and write operations of each transaction in a schedule have the same effect as in a serial schedule. Two schedules are view equivalent if they have the same initial read, final write, and read-from relations.
- Conflict serializability can be checked by constructing a precedence graph of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- View serializability can be checked by comparing the read and write operations of each transaction in a schedule with those in a serial schedule. A schedule is view serializable if and only if it is view equivalent to some serial schedule.