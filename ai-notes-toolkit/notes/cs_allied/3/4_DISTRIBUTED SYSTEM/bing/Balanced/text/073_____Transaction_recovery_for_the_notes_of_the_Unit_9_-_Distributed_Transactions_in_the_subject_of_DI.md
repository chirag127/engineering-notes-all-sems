### Transaction recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring a distributed database system to a consistent state after a failure of one or more components, such as sites, networks, or transactions.
- Transaction recovery is essential for maintaining the ACID properties of transactions, especially atomicity and durability.
- Transaction recovery involves two main steps: failure detection and failure recovery.
- Failure detection is the process of identifying and reporting the occurrence of a failure in the system. Failure detection can be done by various methods, such as timeouts, acknowledgments, heartbeats, or voting.
- Failure recovery is the process of restoring the system to a consistent state after a failure. Failure recovery can be done by various methods, such as undoing, redoing, or compensating the effects of failed transactions, or using backup copies or shadow versions of the data.
- Transaction recovery can be classified into two types: local recovery and global recovery.
- Local recovery is the process of recovering a single site or transaction after a failure. Local recovery can be done by using techniques such as write-ahead logging, checkpoints, or shadow paging.
- Global recovery is the process of recovering the entire system or a distributed transaction after a failure. Global recovery can be done by using techniques such as two-phase commit, three-phase commit, or presumed abort/commit protocols.