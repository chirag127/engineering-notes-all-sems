 Here is the content in markdown format for the topic -

### Conflict & View Serializable Schedule

A schedule is said to be view serializable if the order of execution of transactions in the schedule preserves the consistency of all views that each transaction may have of the database. This is a weaker condition than serializability.

- A view for a transaction consists of all updates performed by that transaction and all updates that were committed before that transaction began.
- A view serializable schedule ensures that transactions see a consistent database state, but it does not ensure that the final database state is consistent with some serial execution of the transactions.
- Conflicts may exist between transactions in a view serializable schedule. A conflict occurs if two transactions access and modify the same data item, and at least one of the accesses is a write.
- View serializable is a weaker correctness criterion than serializability. All serializable schedules are view serializable, but the converse is not true.
- Example: Consider two transactions T1 and T2. T1: Read(X); Write(X). T2: Read(X); Write(X). This schedule is view serializable but not serializable as it contains a conflict between T1 and T2.

Advantages:
- Throughput can be higher than serial schedules as less restrictions are placed on transaction execution.
Disadvantages:
- The final database state may not correspond to some serial execution of the transactions, so database consistency cannot be guaranteed.

Applications:
View serializability is used in databases and transaction processing systems where high performance is critical and some lack of consistency can be tolerated. It can be a good approach when conflicts are unlikely or when conflicts can be resolved manually if they do occur.