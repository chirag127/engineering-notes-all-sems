

### Transaction Processing Concepts

* A transaction is a logical unit of work that accesses and possibly updates various data items.
* A transaction must be atomic, meaning that all the operations within the transaction are either all completed or none are completed.
* A transaction must also be consistent, meaning that it must leave the database in a consistent state.
* A transaction must also be isolated, meaning that the effects of a transaction cannot be seen by other transactions until the transaction is committed.
* A transaction must also be durable, meaning that once a transaction is committed, its effects will persist even in the event of system failure.
* A transaction should also be serializable, meaning that the effects of transactions should be the same as if the transactions were executed one at a time in some order.
* Concurrency control techniques are used to ensure that transactions are isolated and serializable.
* Recovery techniques are used to ensure that transactions are durable.