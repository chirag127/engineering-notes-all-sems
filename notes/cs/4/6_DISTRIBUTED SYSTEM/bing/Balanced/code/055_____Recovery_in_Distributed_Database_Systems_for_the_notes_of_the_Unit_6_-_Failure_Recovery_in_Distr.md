### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.
- Recovery in distributed database systems can be classified into two types: transaction recovery and system recovery.
- Transaction recovery is done to eliminate the adverse effects of faulty transactions rather than to recover from a failure. Faulty transactions include all transactions that have changed the database into an undesired state and the transactions that have used values written by the faulty transactions.
- Transaction recovery can be achieved by using undo or redo operations, depending on the state of the transaction at the time of failure. Undo operations restore the database to its state before the transaction started, while redo operations restore the database to its state after the transaction committed.
- Transaction recovery can be implemented by using different protocols, such as two-phase commit protocol, three-phase commit protocol, or majority protocol, which coordinate the commit or abort decisions of the subtransactions at different sites .
- System recovery is done to restore the database to a consistent state after a failure that causes extensive damage to the database, such as disk crash or power outage.
- System recovery can be achieved by using backup copies of the database, which are periodically created and stored on archival media, such as tapes or disks.
- System recovery can be implemented by using different techniques, such as shadow paging, checkpointing, or logging, which record the changes made to the database or the state of the database at certain points in time .
- System recovery can be performed by using different strategies, such as deferred update, immediate update, or fuzzy update, which determine when the changes made by the transactions are written to the database or the backup copy .