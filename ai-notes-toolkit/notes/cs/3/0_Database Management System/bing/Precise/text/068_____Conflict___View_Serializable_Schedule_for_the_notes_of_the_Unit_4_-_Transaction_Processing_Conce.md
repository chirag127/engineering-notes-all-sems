### Conflict & View Serializable Schedule

#### Conflict Serializable Schedule
- A schedule is conflict serializable if it can be transformed into a serial schedule by swapping non-conflicting operations.
- Two operations are said to be conflicting if they satisfy the following conditions:
    1. They belong to different transactions.
    2. They access the same data item.
    3. At least one of the operations is a write operation.
- If two operations are not conflicting, they can be swapped without affecting the final outcome of the schedule.

#### View Serializable Schedule
- A schedule is view serializable if it is view equivalent to a serial schedule.
- Two schedules are view equivalent if the following conditions are satisfied:
    1. The same set of transactions participates in both schedules.
    2. For any data item, if a transaction reads the initial value of the data item in one schedule, the same transaction must read the initial value of the data item in the other schedule.
    3. For any data item, if a transaction writes the final value of the data item in one schedule, the same transaction must write the final value of the data item in the other schedule.
    4. For any data item, if a transaction T reads the value of the data item written by transaction S in one schedule, the same transaction T must read the value of the data item written by the same transaction S in the other schedule.
- A view serializable schedule may not be conflict serializable.
