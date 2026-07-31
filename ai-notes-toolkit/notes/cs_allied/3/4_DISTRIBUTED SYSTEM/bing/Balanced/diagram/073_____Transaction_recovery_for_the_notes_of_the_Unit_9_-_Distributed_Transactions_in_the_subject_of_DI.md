### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction .
- A failure in a distributed system can be caused by various reasons, such as network partition, site crash, communication link failure, disk failure, or software error.
- A transaction in a distributed system may involve multiple sites, each executing a subtransaction on a local database. If any of the subtransactions fails or aborts, the whole transaction must be rolled back to ensure atomicity.
- Transaction recovery in a distributed system involves two main tasks: failure detection and failure handling.
  - Failure detection is the process of identifying the sites or subtransactions that have failed or aborted, and notifying the other sites or subtransactions involved in the same transaction.
  - Failure handling is the process of taking appropriate actions to recover from the failure, such as aborting, committing, or restarting the subtransactions, depending on the state of the transaction and the type of the failure.
- There are different techniques for transaction recovery in a distributed system, such as logging, shadow versions, two-phase commit protocol, three-phase commit protocol, and presumed abort/commit protocols   .
  - Logging is a technique that records the changes made by a subtransaction in a log file, which can be used to undo or redo the changes in case of a failure .
  - Shadow versions is a technique that creates a copy of the data before modifying it, and updates a pointer to the latest version after committing the subtransaction. If a subtransaction aborts, the pointer is restored to the previous version.
  - Two-phase commit protocol is a protocol that coordinates the commit or abort decision of a transaction among all the sites involved, using a coordinator site and two phases: prepare and commit  .
  - Three-phase commit protocol is a protocol that extends the two-phase commit protocol by adding a pre-commit phase, which reduces the possibility of blocking in case of a failure .
  - Presumed abort/commit protocols are protocols that optimize the two-phase commit protocol by reducing the amount of logging or communication required, based on the assumption that most transactions abort or commit .