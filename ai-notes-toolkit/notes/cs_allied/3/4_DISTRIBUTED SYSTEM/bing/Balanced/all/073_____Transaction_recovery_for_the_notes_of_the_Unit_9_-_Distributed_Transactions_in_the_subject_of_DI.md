# Transaction Recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring a distributed database system to a consistent state after a failure of a site, a communication network, or a transaction .
- Transaction recovery is essential to ensure the ACID properties of transactions, especially atomicity and durability.
- Transaction recovery involves two main steps: failure detection and failure recovery.
- Failure detection is the process of identifying the sites, transactions, or messages that are affected by a failure.
- Failure recovery is the process of applying appropriate actions to restore the consistency of the database and complete the transactions.
- There are different types of failures that can occur in a distributed system, such as site failures, network failures, transaction failures, and media failures.
- There are different techniques for transaction recovery, such as logging, shadow versions, checkpoints, and two-phase commit   .
- Logging is a technique that records the changes made by transactions in a log file, which can be used to undo or redo the operations in case of a failure   .
- Shadow versions is a technique that maintains multiple versions of the database objects, and updates them only when a transaction commits successfully .
- Checkpoints is a technique that periodically saves the state of the database and the transactions, which can be used to reduce the recovery time and the amount of logging  .
- Two-phase commit is a protocol that coordinates the commit or abort decision of a distributed transaction among all the participating sites  .