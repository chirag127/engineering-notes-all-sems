# Serializability of Schedules

- A schedule is a sequence of operations performed by one or more transactions on a database.
- A serial schedule is a schedule in which transactions are executed one after another, without any overlap in time.
- A non-serial schedule is a schedule in which transactions are executed concurrently, with some overlap in time.
- Serializability is a property of a schedule that ensures the consistency and correctness of a database.
- Serializability means that a non-serial schedule is equivalent to a serial schedule with the same transactions, in terms of the final state of the database and the data values.
- There are two methods to check the serializability of a schedule: conflict serializability and view serializability.

## Conflict Serializability

- Conflict serializability is based on the concept of conflict operations.
- Two operations are said to conflict if they belong to different transactions, access the same data item, and at least one of them is a write operation.
- A conflict operation can affect the outcome of a schedule, and hence the order of conflict operations must be preserved in any equivalent schedule.
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Conflict serializability can be tested by using a precedence graph, which is a directed graph that represents the order of conflicting operations in a schedule.
- A schedule is conflict serializable if and only if its precedence graph is acyclic.

## View Serializability

- View serializability is based on the concept of view equivalence.
- Two schedules are said to be view equivalent if they have the same view of the database, which means:
  - They read the same initial value for each data item.
  - They write the same final value for each data item.
  - They read the same value for each data item that is written by some transaction.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- View serializability is a more general notion than conflict serializability, and it allows some schedules that are not conflict serializable.
- View serializability can be tested by using a polygraph, which is a directed graph that represents the read-write dependencies among transactions in a schedule.
- A schedule is view serializable if and only if its polygraph is acyclic and has no blind writes.