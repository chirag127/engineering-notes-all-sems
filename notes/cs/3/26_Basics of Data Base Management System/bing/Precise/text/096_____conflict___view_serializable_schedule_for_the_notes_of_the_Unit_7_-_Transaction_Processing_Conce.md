### Conflict Serializable Schedule

A schedule is called conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations. In other words, a schedule is conflict serializable if the order of any two conflicting operations is the same as their order in a serial schedule.

- A conflict occurs when two transactions access the same data item and at least one of them is a write operation.
- Two operations are conflicting if they belong to different transactions, access the same data item, and at least one of them is a write operation.
- A schedule is conflict serializable if it is equivalent to some serial schedule.

### View Serializable Schedule

A schedule is called view serializable if it is view equivalent to a serial schedule. View equivalence between two schedules means that the following three conditions hold:

1. The same set of transactions participates in both schedules.
2. For any data item, if a transaction reads the initial value of the data item in one schedule, then the same transaction must read the initial value of the data item in the other schedule.
3. For any data item, if a transaction writes the final value of the data item in one schedule, then the same transaction must write the final value of the data item in the other schedule.

- View serializability is a more general notion than conflict serializability.
- A schedule is view serializable if it is view equivalent to some serial schedule.
- Every conflict serializable schedule is also view serializable, but the converse is not always true.
