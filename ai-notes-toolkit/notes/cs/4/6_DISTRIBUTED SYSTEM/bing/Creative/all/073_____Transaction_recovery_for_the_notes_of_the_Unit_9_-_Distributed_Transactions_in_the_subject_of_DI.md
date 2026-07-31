# Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction system must ensure the ACID properties of transactions: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.

- Transaction recovery is the process of restoring the database to a consistent state after a failure or an abort.
- Transaction recovery is essential for maintaining the atomicity and durability properties of transactions.
- Transaction recovery in a distributed system is more complex than in a centralized system because of the following challenges:
  - Communication failures: A site may not be able to communicate with other sites due to network problems or partitioning.
  - Site failures: A site may crash or become unavailable due to hardware or software faults.
  - Distributed commit: A distributed transaction must ensure that all the sites involved agree on the outcome of the transaction (commit or abort).
  - Distributed concurrency control: A distributed transaction must coordinate with other transactions to ensure the isolation property.

- Transaction recovery in a distributed system relies on the following techniques:
  - Logging: A log is a record of the operations performed by a transaction and their effects on the database. A log is used to undo or redo the operations of a transaction in case of a failure or an abort. A log can be stored locally at each site or globally at a coordinator site.
  - Checkpointing: A checkpoint is a point in time when the database is consistent and all the log records have been written to stable storage. A checkpoint reduces the amount of work needed for recovery by limiting the number of transactions that need to be examined or redone.
  - Two-phase commit protocol: A two-phase commit protocol is a protocol that ensures that all the sites involved in a distributed transaction agree on the outcome of the transaction. The protocol consists of two phases: a prepare phase and a commit phase. In the prepare phase, the coordinator site asks all the participant sites to vote on whether they are ready to commit or abort the transaction. In the commit phase, the coordinator site decides on the final outcome based on the votes and informs all the participant sites to commit or abort accordingly.
  - Shadow versions: A shadow version is a copy of a data item that is created by a transaction before modifying it. A shadow version is used to restore the original value of the data item in case of an abort. A shadow version can be stored locally at each site or globally at a coordinator site.