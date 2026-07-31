### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- A transaction is a logical unit of work that accesses and possibly modifies the data in a database.
- A distributed transaction is a transaction that spans multiple sites or nodes in a distributed system.
- A distributed transaction system must ensure the ACID properties of transactions: atomicity, consistency, isolation, and durability.
- Atomicity means that either all the operations of a transaction are executed or none of them are.
- Consistency means that a transaction preserves the integrity constraints of the database.
- Isolation means that a transaction does not interfere with other concurrent transactions.
- Durability means that the effects of a committed transaction are permanent and survive failures.
- Transaction recovery is the process of restoring the database to a consistent state after a failure or an abort of a transaction.
- Transaction recovery is essential for maintaining the ACID properties of transactions in a distributed system.
- Transaction recovery in a distributed system is more complex than in a centralized system because of the following challenges:
  - Communication failures: A site may not be able to communicate with other sites due to network problems or partitioning.
  - Site failures: A site may crash or become unavailable due to hardware or software faults.
  - Distributed concurrency control: A site may have to coordinate with other sites to ensure the isolation of transactions.
  - Distributed commit protocol: A site may have to participate in a protocol to ensure the atomicity of transactions.
- Transaction recovery in a distributed system can be based on different techniques, such as:
  - Logging and checkpointing: A site records the operations of transactions in a log file and periodically saves the state of the database in a checkpoint. In case of a failure, a site can use the log and the checkpoint to undo or redo the operations of transactions.
  - Shadow versions: A site maintains multiple versions of the database and updates only the latest version. In case of a failure, a site can switch to a previous version of the database that is consistent.
  - Compensation: A site executes compensating transactions to undo the effects of aborted transactions. A compensating transaction is a transaction that reverses the actions of another transaction without violating the consistency of the database.