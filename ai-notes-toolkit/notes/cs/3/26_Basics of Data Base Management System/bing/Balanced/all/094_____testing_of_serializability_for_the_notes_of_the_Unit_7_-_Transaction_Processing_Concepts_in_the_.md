# Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of a database.
- A schedule is serializable if it is equivalent to some serial schedule, where transactions are executed one after the other without any overlap.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read-write, write-read, or write-write) on the same data item in a schedule must be ordered in the same way as in a serial schedule.
- View serializability is a weaker form of serializability that requires that any two schedules have the same initial and final state of the database, and that any read operation on a data item in a schedule must read the same value as in a serial schedule.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph is a directed graph of the entire transactions of a schedule, where each node represents a transaction and each edge represents a conflict between two transactions.
- A precedence graph is a subset of a serialization graph that only contains the edges that indicate the order of conflicting operations on the same data item.
- A schedule is conflict serializable if and only if its serialization graph or precedence graph is acyclic, meaning that it does not contain any cycles.
- A schedule is view serializable if and only if it is view equivalent to some serial schedule, where two schedules are view equivalent if they have the same initial and final state of the database, and the same read operations on the same data items.
- Testing for view serializability is more complex than testing for conflict serializability, and it involves checking for potential cycles between transactions' precedence relationships.
- A precedence relationship exists when one transaction must precede another transaction for the schedule to be valid. For example, if transaction T1 reads a data item X that was written by transaction T2, then T2 must precede T1 in any serial schedule.
- A schedule is view serializable if and only if it has a legal serialization order, meaning that there is a way to order the transactions in a serial schedule such that no precedence relationship is violated.
- A legal serialization order can be found by using a topological sorting algorithm on the precedence graph, which produces an order of nodes such that no node appears before its predecessors. If the precedence graph is cyclic, then there is no legal serialization order and the schedule is not view serializable.