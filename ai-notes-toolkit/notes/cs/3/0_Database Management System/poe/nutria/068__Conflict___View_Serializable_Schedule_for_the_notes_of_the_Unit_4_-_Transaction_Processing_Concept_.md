
### Conflict & View Serializable Schedule

* Conflict serializability is a concept used in database management systems (DBMS) to ensure that concurrent transactions do not conflict with each other. 
* A transaction is said to be conflict-serializable if its execution results in a state which is equivalent to some serial execution of the same transactions.
* Conflict serializability is a necessary condition for transaction serializability.
* A view serializable schedule is a schedule which is equivalent to some serial schedule of the same transactions.
* View serializable schedules are conflict-serializable schedules that also satisfy certain additional conditions.
* A view serializable schedule is conflict-serializable if it is equivalent to some serial schedule of the same transactions.
* In order to ensure that a schedule is view serializable, it is necessary to ensure that certain conditions are met:
  * All transactions must be conflict-serializable.
  * All transactions must be read-only.
  * All transactions must have the same read and write sets.
  * All transactions must have the same read and write locks.
  * All transactions must have the same write locks.
  * All transactions must have the same commit order.
  * All transactions must have the same commit times.
  * All transactions must have the same commit points.