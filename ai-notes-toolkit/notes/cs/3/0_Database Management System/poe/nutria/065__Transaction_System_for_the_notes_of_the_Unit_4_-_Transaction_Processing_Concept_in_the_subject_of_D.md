
### Transaction System

* A transaction is a unit of work that is performed against a database.
* The ACID (Atomicity, Consistency, Isolation, Durability) properties are used to guarantee the integrity of the database.
* Atomicity ensures that all operations within a transaction are completed successfully or none of them are.
* Consistency ensures that the database remains in a consistent state.
* Isolation ensures that the results of concurrent transactions are not visible to each other until the transactions are committed.
* Durability ensures that the results of a committed transaction are not lost in case of a system failure.
* A two-phase commit protocol is used to guarantee the atomicity of distributed transactions.
* A distributed transaction is a transaction that involves multiple databases.
* A transaction log is used to store information about the changes made to the database during a transaction.
* A transaction manager is responsible for managing the transaction lifecycle.
* A deadlock is a situation where two or more transactions are waiting for each other to complete before they can proceed.
* A checkpoint is a point in time where the database is in a consistent state.