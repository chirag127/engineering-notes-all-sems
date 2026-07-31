# Serializability of schedules

- A schedule is a sequence of operations performed by concurrent transactions on a shared database.
- A schedule is serializable if it is equivalent to a serial schedule, which is a schedule where transactions are executed one after another without any overlap in time.
- Serializability is a desirable property of schedules because it ensures the consistency and correctness of the database state after the execution of concurrent transactions.
- There are two types of serializability: conflict serializability and view serializability.

## Conflict serializability

- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations, which are operations that access different data items or are both read operations.
- Conflict serializability can be checked by constructing a precedence graph, which is a directed graph where the nodes are transactions and the edges are conflicts between operations. A conflict is a pair of operations from different transactions that access the same data item and at least one of them is a write operation.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

## View serializability

- A schedule is view serializable if it is equivalent to a serial schedule in terms of the following three conditions:
  - The initial read operations of each data item are the same in both schedules.
  - The final write operations of each data item are the same in both schedules.
  - The read operations of each data item see the same value written by the same transaction in both schedules.
- View serializability is a more general concept than conflict serializability, as it allows some schedules that are not conflict serializable to be view serializable.
- View serializability can be checked by constructing a polygraph, which is a directed graph where the nodes are operations and the edges are dependencies between operations. A dependency is a relation between two operations that access the same data item and at least one of them is a write operation.
- A schedule is view serializable if and only if its polygraph is acyclic.