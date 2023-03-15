# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the same outcome as if the transactions were executed one by one in some order.
- Serializability is important for maintaining the consistency and correctness of a database in a concurrent environment.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read-write, write-read, or write-write) on the same data item by different transactions must be executed in the same order in the schedule as in the serial order.
- View serializability is a weaker form of serializability that requires that any transaction must read the same value and write the final value of any data item as in the serial order, but allows the order of non-conflicting operations to be different.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions. A schedule is conflict serializable if and only if its serialization graph is acyclic.
- A precedence graph is a directed graph of the conflicting operations of a schedule, where each node represents an operation and each edge represents a precedence relationship between two operations. A schedule is conflict serializable if and only if its precedence graph is acyclic.
- A schedule is view serializable if and only if it is view equivalent to some serial schedule, meaning that it preserves the same read and write values as the serial schedule. Testing for view serializability is more complex than testing for conflict serializability and usually involves finding a legal serialization order for the transactions.