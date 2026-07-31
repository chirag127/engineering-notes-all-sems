### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the same outcome as if the transactions were executed serially, one after the other.
- Serializability is important for maintaining the consistency and correctness of a database in a concurrent environment.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that preserves the order of conflicting operations (read-write, write-read, write-write) between transactions.
- View serializability is a weaker form of serializability that preserves the final state of the database and the read-write dependencies between transactions.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- There are two techniques to test serializability: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions.
- A precedence graph is a subset of the serialization graph that only contains the edges that indicate the order of conflicting operations between transactions.
- A schedule is conflict serializable if and only if its serialization graph or precedence graph is acyclic, meaning that it does not contain any cycles.
- A schedule is view serializable if and only if it is view equivalent to a serial schedule, meaning that it produces the same final state of the database and the same read-write dependencies as a serial schedule.
- View serializability can be tested by checking the following three conditions for each transaction in the schedule:
  - Initial read condition: the transaction reads the initial value of a data item if and only if no other transaction writes to that data item before it in the serial schedule.
  - Final write condition: the transaction writes the final value of a data item if and only if no other transaction writes to that data item after it in the serial schedule.
  - Read-write dependency condition: the transaction reads the value of a data item written by another transaction if and only if the other transaction precedes it in the serial schedule.
- If all three conditions are satisfied for all transactions in the schedule, then the schedule is view serializable. Otherwise, it is not view serializable.