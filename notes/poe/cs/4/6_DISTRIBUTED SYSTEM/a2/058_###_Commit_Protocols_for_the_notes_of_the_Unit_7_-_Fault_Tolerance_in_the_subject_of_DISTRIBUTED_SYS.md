 Here is the content in markdown format:

### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- **Two-phase commit protocol:** It is a distributed algorithm that coordinates all the processes that are participating in a distributed transaction on whether to commit or abort (roll back) the transaction. It ensures the atomicity of the transaction. It has two phases:

1. Commit-request phase: The coordinator (one of the participating processes) asks all the participants to prepare to commit. Each participant checks if it is ready to commit and votes either yes or no.

2. Commit phase: If all the participants voted yes in the first phase, the coordinator asks all to commit. Otherwise, it asks all to abort.

- **Three-phase commit protocol:** It is an extension of two-phase commit protocol that adds an extra phase to handle failures. After the commit-request phase, there is a pre-commit phase where the coordinator commits locally and waits for the participants' acknowledgement. If all acknowledge, it proceeds to the commit phase, otherwise it rolls back. This handles the coordinator failure.

- **Paxos algorithm:** It is a consensus algorithm that involves multiple rounds of communication between the processes to agree upon a value. In each round, a process proposes a value and the others vote to accept or reject it. A value is chosen only if a majority of the processes accept it. It ensures that at most one value is chosen. It is complex but can tolerate process failures.

- **Zab protocol:** It is a distributed consensus algorithm that is suited for replicated databases. It uses a "primary-backup" approach where one replica (primary) handles all write operations and the backups passively copy the data. The primary is elected using a consensus protocol and may change in case of failures. It ensures strong consistency and high availability.

[Include diagrams and examples if required.]

The pros and cons, applications, etc. can be included if helpful for learning. The content can be modified as needed. Let me know if you would like me to revise or add anything.