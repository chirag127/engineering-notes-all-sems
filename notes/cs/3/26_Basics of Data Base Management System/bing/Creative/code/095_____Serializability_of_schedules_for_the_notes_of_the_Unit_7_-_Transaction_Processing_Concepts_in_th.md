### Serializability of schedules

- A schedule is a sequence of operations performed by one or more transactions on a database.
- A schedule is serializable if it produces the same result as some serial schedule, which is a schedule where transactions are executed one after another without any overlap  .
- Serializability is an important property that ensures the consistency and correctness of concurrent transactions in a database management system (DBMS)    .
- There are different types of serializability, such as conflict serializability, view serializability, and cursor stability serializability, which have different criteria and methods to check and enforce them     .
- Conflict serializability is based on the notion of conflict operations, which are operations that access the same data item and at least one of them is a write operation   . A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations   .
- View serializability is based on the notion of view equivalence, which means that two schedules have the same initial and final values for each data item, and the same transactions read the final value of each data item   . A schedule is view serializable if it is view equivalent to some serial schedule   .
- Cursor stability serializability is based on the notion of cursor stability, which means that a transaction does not lose the right to read or write a data item until it moves its cursor to another data item  . A schedule is cursor stability serializable if it preserves the cursor stability property for each transaction  .
- Serializability can be checked by using different methods, such as precedence graphs, polygraphs, or testing for cycles in the dependency graph    .
- Serializability can be enforced by using different techniques, such as locking, timestamping, or optimistic concurrency control     .
- Serializability has some advantages, such as providing a high level of isolation, consistency, and correctness for concurrent transactions, and simplifying the reasoning and verification of the database behavior    .
- Serializability also has some disadvantages, such as reducing the concurrency and performance of the system, increasing the complexity and overhead of the concurrency control mechanisms, and requiring more resources and coordination among transactions    .