### Testing of Serializability

- Serializability is a property of a schedule of transactions that ensures the consistency and correctness of the database state after the execution of the transactions.
- A schedule is serializable if it is equivalent to some serial schedule, where the transactions are executed one after the other without any interleaving of operations.
- There are two types of serializability: conflict serializability and view serializability.
- Conflict serializability is a stricter form of serializability that requires that any two conflicting operations (read-write, write-read, or write-write) on the same data item in a schedule must be ordered in the same way as in a serial schedule.
- View serializability is a weaker form of serializability that requires that any two schedules have the same initial and final state of the database, and that any read operation on a data item in a schedule must read the same value as in a serial schedule.
- Testing of serializability involves verifying that a given schedule of transactions is serializable, meaning that the effects of running the transactions concurrently are equivalent to running them serially, one after the other.
- We can use below two techniques to test serializability in DBMS: serialization graph and precedence graph.
- A serialization graph or a precedence graph is a directed graph of the transactions in a schedule, where an edge from Ti to Tj indicates that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its serialization graph is acyclic, meaning that it does not contain any cycles or loops.
- A schedule is view serializable if and only if it is conflict serializable or it can be transformed into a conflict serializable schedule by swapping non-conflicting operations.
- Testing of serializability using serialization graph or precedence graph is a polynomial-time algorithm, meaning that it can be done in a reasonable amount of time for a given schedule.