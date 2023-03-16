# Recovery in Distributed Database Systems

- Recovery in distributed database systems is the process of restoring the database to a consistent state after a failure or an error .
- Recovery in distributed database systems is more complicated than in centralized database systems because failures can occur at the communication links or a remote site.
- Recovery in distributed database systems aims to maintain the atomicity and durability of distributed transactions, which means that all statements in a transaction, distributed or non-distributed, either commit or roll back as a unit.
- Recovery in distributed database systems can be classified into two types: local recovery and global recovery .
  - Local recovery is the recovery of a single site or a single transaction that has failed or aborted. Local recovery can be done by using undo or redo operations based on the transaction log.
  - Global recovery is the recovery of a distributed transaction that involves multiple sites or multiple transactions that have failed or aborted. Global recovery can be done by using distributed commit protocols, such as two-phase commit (2PC) or three-phase commit (3PC), that coordinate the commit or abort decisions of all the participating sites .
- Recovery in distributed database systems can also be affected by the replication of data across multiple sites. Replication can improve the availability and performance of the database, but it also introduces the problem of maintaining the consistency of the replicas.
  - Recovery in replicated database systems can be done by using replication protocols, such as eager replication or lazy replication, that synchronize the updates of the replicas.
  - Eager replication ensures that all the replicas are updated before a transaction commits, which avoids the problem of conflicting updates, but it also increases the communication and synchronization overhead.
  - Lazy replication allows the replicas to be updated after a transaction commits, which reduces the communication and synchronization overhead, but it also introduces the problem of conflicting updates, which have to be resolved by using conflict resolution policies.