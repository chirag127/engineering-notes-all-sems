### Recovery in Distributed Database Systems

Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure. There are two types of failures that can occur in a distributed database system: soft failures and hard failures.

1. **Soft Failures**: In case of soft failures that result in inconsistency of the database, the recovery strategy includes transaction undo or rollback. However, sometimes, transaction redo may also be adopted to recover to a consistent state of the transaction.

2. **Hard Failures**: In case of hard failures resulting in extensive damage to the database, recovery strategies encompass restoring a past copy of the database from archival backup.

As with local recovery, distributed database recovery aims to maintain the atomicity and durability of distributed transactions. A database must guarantee that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.

Distributed recovery is more complicated than centralized database recovery because failures can occur at the communication links or a remote site. Ideally, a recovery system should be simple, incur tolerable overhead, maintain system consistency, provide partial operability and avoid global rollback.

Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions.