# Serializability of Schedules

- A schedule is a sequence of operations performed by one or more transactions on a database.
- A schedule is serial if it executes one transaction at a time, without any interleaving of operations from different transactions.
- A schedule is non-serial if it allows concurrent execution of two or more transactions, with some interleaving of operations from different transactions.
- A schedule is serializable if it is equivalent to some serial schedule with the same transactions.
- Serializability is a desirable property of a schedule, as it ensures the consistency and isolation of transactions.
- There are two main methods to check the serializability of a schedule: conflict serializability and view serializability.

## Conflict Serializability

- Two operations in a schedule are said to conflict if they belong to different transactions, access the same data item, and at least one of them is a write operation.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Conflict serializability can be tested by constructing a precedence graph (or serializability graph) for the given schedule.
- A precedence graph is a directed graph where the nodes represent the transactions and the edges represent the conflicts between them.
- An edge from Ti to Tj means that Ti must precede Tj in any serial schedule equivalent to the given schedule.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

## View Serializability

- A schedule is view serializable if it is view equivalent to some serial schedule with the same transactions.
- Two schedules are view equivalent if they satisfy the following conditions:
  - For each data item, the same transaction reads its initial value in both schedules.
  - For each data item, the same transaction writes its final value in both schedules.
  - For each data item, the set of transactions that read the value written by a transaction is the same in both schedules.
- View serializability is a more general notion than conflict serializability, as it allows some schedules that are not conflict serializable.
- View serializability can be tested by constructing a polygraph (or view graph) for the given schedule.
- A polygraph is a directed graph where the nodes represent the transactions and the edges represent the view dependencies between them.
- An edge from Ti to Tj means that Ti must precede Tj in any serial schedule view equivalent to the given schedule.
- A schedule is view serializable if and only if its polygraph is acyclic.