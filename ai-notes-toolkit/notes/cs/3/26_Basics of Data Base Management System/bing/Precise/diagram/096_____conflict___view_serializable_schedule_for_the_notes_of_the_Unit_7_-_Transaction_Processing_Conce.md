### Conflict & View Serializable Schedule

#### Unit 7 - Transaction Processing Concepts in the subject of Basics of Data Base Management System

1. A schedule is a sequence of operations from a set of transactions.
2. A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
3. A conflict occurs when two transactions access the same data item and at least one of the operations is a write operation.
4. A schedule is view serializable if the following conditions are met:
    - The initial read operations of each transaction in the schedule read the same values as in the serial schedule.
    - The final write operations of each transaction in the schedule write the same values as in the serial schedule.
    - All other read operations of each transaction in the schedule read the result of the same write operations as in the serial schedule.
5. Conflict serializability is a sufficient but not necessary condition for view serializability.
6. View serializability is a more general concept than conflict serializability.
7. A schedule can be view serializable but not conflict serializable.
