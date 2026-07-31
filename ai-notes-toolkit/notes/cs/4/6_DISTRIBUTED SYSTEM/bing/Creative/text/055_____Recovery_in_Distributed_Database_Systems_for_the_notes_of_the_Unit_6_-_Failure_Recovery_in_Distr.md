### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure, such as a site crash, a communication link failure, or a transaction abort .
- Recovery in distributed database systems is more complicated than in centralized database systems, because failures can affect multiple sites and transactions, and the system has to coordinate the recovery actions across the network.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites are committed, and the committed changes are permanent.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery.
  - Local recovery is the recovery of a single site from a failure, such as a disk crash or a power outage. Local recovery involves restoring a backup copy of the database, and applying the undo and redo operations from the log to bring the database to a consistent state.
  - Global recovery is the recovery of the whole system from a failure, such as a network partition or a coordinator crash. Global recovery involves resolving the uncertain status of distributed transactions, and ensuring that all sites agree on the final outcome of each transaction.
- Recovery in distributed database systems can use different techniques, such as:
  - Two-phase commit protocol, which is a distributed commit protocol that ensures atomicity of distributed transactions by using a coordinator site and participant sites, and two phases of voting and decision .
  - Three-phase commit protocol, which is an extension of the two-phase commit protocol that ensures atomicity and avoids blocking in case of a coordinator failure, by using a third phase of pre-commit and a timeout mechanism .
  - Shadow paging, which is a technique that maintains two copies of the database pages, one as the current version and one as the shadow version, and updates only the current version until the transaction commits, and then switches the roles of the two versions .
  - Checkpointing, which is a technique that periodically records the state of the system, such as the committed transactions, the active transactions, and the log records, to a stable storage, and reduces the amount of work needed for recovery .
  - Logging, which is a technique that records the changes made by the transactions to the database, such as the before and after values of the updated data items, the transaction identifiers, and the commit and abort records, to a log file, and uses them for undo and redo operations during recovery .
  - Replication, which is a technique that maintains multiple copies of the database at different sites, and increases the availability and reliability of the system, but also introduces the challenges of maintaining consistency and concurrency among the replicas .

: https://www.tutorialspoint.com/distributed_dbms/distributed_dbms_database_recovery.htm
: https://www.oreilly.com/library/view/database-systems-concepts/9788177585674/9788177585674_ch18lev1sec7.html
: https://link.springer.com/referenceworkentry/10.1007/978-0-387-39940-9_712