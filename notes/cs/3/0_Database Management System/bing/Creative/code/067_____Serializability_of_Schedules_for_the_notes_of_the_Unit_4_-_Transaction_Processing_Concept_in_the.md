### Serializability of Schedules

- A schedule is a sequence of database actions (read and write operations) performed by one or more transactions on a shared database.
- Serializability is a property of schedules that ensures the consistency and correctness of the database state after the execution of concurrent transactions.
- A schedule is serializable if it produces the same result as a serial schedule, which is a schedule where transactions are executed one at a time without any interleaving of actions.
- There are two main types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting actions (read and write operations on the same data item) of two different transactions must be executed in the same order in both the original and the serial schedule.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting actions of different transactions.
- View serializability is a weaker form of serializability that requires that any two transactions must have the same view of the database in both the original and the serial schedule.
- A schedule is view serializable if it is view equivalent to a serial schedule, which means that:
  - The initial read operations of each data item are performed by the same transaction in both schedules.
  - The final write operations of each data item are performed by the same transaction in both schedules.
  - The read operations of each data item that are not initial read operations see the same value written by the same transaction in both schedules.
- Serializability is important for concurrency control, which is the mechanism that ensures the isolation and atomicity of transactions in a database system.
- Serializability can be checked by using various methods, such as precedence graphs, testing for cycles, or using locking protocols.