### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple nodes in a distributed system, such as multiple databases or microservices.
- A distributed transaction must satisfy the ACID properties: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations in a transaction are executed or none of them are.
- Consistency means that the transaction preserves the integrity constraints of the database.
- Isolation means that the transaction does not interfere with other concurrent transactions.
- Durability means that the effects of the transaction are permanent and survive failures.
- Transaction recovery is the process of restoring the database to a consistent state after a failure, such as a system crash, a network partition, or a transaction abort.
- Transaction recovery is based on two techniques: logging and checkpointing.
- Logging is the process of recording the changes made by a transaction to the database in a persistent log file.
- Checkpointing is the process of periodically writing the modified pages of the database to the disk, and recording the checkpoint location in the log file.
- There are two types of logging: undo logging and redo logging.
- Undo logging records the old values of the data items before they are modified by a transaction. Undo logging allows to rollback a transaction by restoring the old values from the log.
- Redo logging records the new values of the data items after they are modified by a transaction. Redo logging allows to reapply the changes of a committed transaction from the log in case of a failure.
- There are two types of recovery algorithms: undo/redo recovery and shadow versioning.
- Undo/redo recovery is based on both undo and redo logging. It uses the log file and the checkpoint to determine which transactions need to be undone or redone after a failure.
- Shadow versioning is based on creating a copy of the database before modifying it by a transaction. It uses the copy as a backup in case of a failure, and switches to the modified version only after the transaction commits.