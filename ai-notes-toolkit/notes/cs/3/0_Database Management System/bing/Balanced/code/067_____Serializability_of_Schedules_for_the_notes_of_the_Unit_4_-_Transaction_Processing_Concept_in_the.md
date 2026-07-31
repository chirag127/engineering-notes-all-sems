### Serializability of Schedules

- A schedule is a sequence of database actions (read and write operations) performed by one or more transactions on a shared database.
- Serializability is a property of schedules that ensures consistency and correctness of the database state after the execution of concurrent transactions.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one at a time without any interleaving of actions.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stronger notion of serializability that requires that two schedules have the same order of conflicting actions, where a conflict is a pair of actions from different transactions that access the same data item and at least one of them is a write operation.
- View serializability is a weaker notion of serializability that requires that two schedules have the same view of the database, where a view is defined by three rules:
  - The same transaction reads the initial value of each data item in both schedules.
  - The same transaction writes the final value of each data item in both schedules.
  - The same transaction reads the value of each data item written by another transaction in both schedules.
- Conflict serializability implies view serializability, but not vice versa.
- Serializability can be checked by using various methods, such as precedence graphs, testing for cycles, or using locking protocols.