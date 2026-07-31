
### Conflict & View Serializability

* Conflict serializability is a concept used in database management systems to ensure that concurrent transactions are processed without conflicting with each other.
* A transaction is said to be conflict serializable if its execution produces the same results as if the transactions were executed serially in some order.
* The concept of conflict serializability is important in order to ensure data integrity in a multi-user database system.
* A view serializable schedule is a schedule of transactions that is conflict serializable and also maintains the view consistency of the database.
* View consistency means that the results of a query on the database are the same regardless of the order in which the transactions are executed.
* In order to achieve view serializability, transactions must be ordered according to some criteria such as timestamp ordering or lock ordering.
* A schedule is considered to be view serializable if it is conflict serializable and also maintains the view consistency of the database.