### Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent and correct state after a failure .
- Failure in distributed database systems can be classified into two types: soft failures and hard failures.
  - Soft failures are temporary and do not cause physical damage to the database, such as network failures, transaction aborts, or deadlocks.
  - Hard failures are permanent and cause physical damage to the database, such as disk crashes, power outages, or site failures.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that either all or none of the subtransactions at different sites are committed, and the committed changes are permanent .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site, and the system may not have a global view of the transaction status.
- Recovery in distributed database systems can be divided into two phases: local recovery and global recovery.
  - Local recovery is the process of restoring a site to a consistent state after a failure, using techniques such as undo, redo, or compensation.
  - Global recovery is the process of coordinating the commit or abort of distributed transactions across multiple sites, using protocols such as two-phase commit, three-phase commit, or majority consensus.
- Recovery in distributed database systems faces several challenges, such as concurrency control, partial operability, network partitioning, and global rollback.
  - Concurrency control is the mechanism to ensure serializability and isolation of distributed transactions, which may conflict with the recovery protocols.
  - Partial operability is the ability of the system to continue processing transactions at some sites even if other sites are down, which may lead to inconsistency or deadlock.
  - Network partitioning is the situation where the system is divided into two or more disjoint subsets of sites that cannot communicate with each other, which may cause ambiguity or deadlock in the commit or abort decision.
  - Global rollback is the situation where the system has to undo all the committed subtransactions of a distributed transaction, which may be costly or impossible.