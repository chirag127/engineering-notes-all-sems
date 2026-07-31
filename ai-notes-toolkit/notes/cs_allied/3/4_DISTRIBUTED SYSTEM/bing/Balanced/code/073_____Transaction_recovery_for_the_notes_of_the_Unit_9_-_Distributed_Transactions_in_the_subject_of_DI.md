### Transaction Recovery for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Transaction recovery is the process of restoring the consistency and integrity of a distributed database after a failure or an abort of a transaction.
- Transaction recovery is essential for ensuring the ACID properties of transactions in a distributed system, where failures and concurrency issues are more likely to occur.
- Transaction recovery involves two main steps: detection and resolution.
- Detection is the process of identifying the transactions that are affected by a failure or an abort, and their status (committed, aborted, or in-doubt).
- Resolution is the process of applying the appropriate actions to the affected transactions, such as undoing, redoing, or committing them, based on their status and the recovery protocol used.
- There are different types of failures that can affect transactions in a distributed system, such as site failures, network failures, media failures, or system failures.
- There are different types of recovery protocols that can be used to handle failures in a distributed system, such as two-phase commit (2PC), three-phase commit (3PC), presumed abort (PA), presumed commit (PC), or shadow versions.
- Each recovery protocol has its own advantages and disadvantages in terms of performance, reliability, and complexity.
- The choice of a recovery protocol depends on the characteristics of the distributed system, such as the degree of replication, the frequency of failures, the availability of backup copies, and the communication cost.