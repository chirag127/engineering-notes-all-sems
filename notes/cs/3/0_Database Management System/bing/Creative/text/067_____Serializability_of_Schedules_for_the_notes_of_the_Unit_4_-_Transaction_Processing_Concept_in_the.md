### Serializability of Schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- Serializability is a desirable property of a schedule because it ensures that concurrent transactions do not interfere with each other and preserve the consistency and concurrency of the database .
- There are two main methods to check the serializability of a schedule: conflict serializability and view serializability.
- Conflict serializability: A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations, which are operations that access different data items or are both read operations .
- View serializability: A schedule is view serializable if it is view equivalent to a serial schedule, which means that it preserves the following three conditions :
  - The same transaction reads the initial value of each data item in both schedules.
  - The same transaction writes the final value of each data item in both schedules.
  - The same transaction reads the value of each data item written by another transaction in both schedules.
- Conflict serializability is a stricter criterion than view serializability, which means that every conflict serializable schedule is also view serializable, but not vice versa .
- Serializability can be tested by using a precedence graph, which is a directed graph where the nodes represent transactions and the edges represent conflicts between operations .
- A schedule is conflict serializable if and only if its precedence graph is acyclic .
- A schedule is view serializable if and only if it has a view equivalent serial schedule, which can be found by using a polygraph, which is a directed graph where the nodes represent data items and the edges represent read-write dependencies between transactions .