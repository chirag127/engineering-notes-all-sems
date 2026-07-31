### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

In distributed systems, transactions that involve multiple resources can be challenging to manage. Atomic commit protocols are used to ensure that all operations within a transaction are either all committed or all rolled back in case of a failure. These protocols are essential for maintaining data consistency in distributed systems. In this unit, we will discuss the different types of atomic commit protocols.

#### Two-Phase Commit (2PC)
- Two-phase commit is a widely used atomic commit protocol in distributed systems.
- It involves two phases: **Prepare** and **Commit**.
- In the Prepare phase, the coordinator sends a message to all participants asking them to vote on whether to commit or abort the transaction.
- In the Commit phase, the coordinator sends a message to all participants to commit the transaction if all participants voted to commit; otherwise, it sends a message to all participants to abort the transaction.
- 2PC ensures that all participants agree on the final outcome of the transaction.

#### Three-Phase Commit (3PC)
- Three-phase commit is an improvement over the two-phase commit protocol.
- It involves three phases: **CanCommit**, **PreCommit**, and **DoCommit**.
- In the CanCommit phase, the coordinator sends a message to all participants asking if they can commit the transaction.
- In the PreCommit phase, the coordinator sends a message to all participants to prepare for committing the transaction.
- In the DoCommit phase, the coordinator sends a message to all participants to commit the transaction.
- 3PC reduces the amount of time that locks are held on resources compared to 2PC.

#### Optimistic Commit
- Optimistic commit is another type of atomic commit protocol.
- It assumes that conflicts between participants are rare and that it is possible to resolve them after the fact.
- In the optimistic commit protocol, each participant commits the transaction locally without coordinating with other participants.
- If a conflict is detected later, the participants can roll back and retry the transaction.
- Optimistic commit is useful when the number of participants is large, and the probability of conflicts is low.

#### Conclusion
Atomic commit protocols are essential for ensuring data consistency in distributed systems. Two-phase commit, three-phase commit, and optimistic commit are three types of atomic commit protocols that are commonly used. Each protocol has its advantages and disadvantages, and the choice of protocol depends on the specific requirements of the system.