### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

In distributed systems, commit protocols are used to ensure that a transaction is either executed completely or not at all. This is important for maintaining data consistency and avoiding conflicts between transactions. Here are some of the commonly used commit protocols:

1. Two-Phase Commit (2PC) Protocol
- This protocol involves two phases: the prepare phase and the commit phase.
- In the prepare phase, the coordinator sends a prepare request to all participants and waits for their responses.
- If all participants agree to commit, the coordinator sends a commit request to all participants. Otherwise, it sends an abort request.
- In the commit phase, all participants execute the transaction and send an acknowledgement to the coordinator.

2. Three-Phase Commit (3PC) Protocol
- This protocol adds an extra phase to the 2PC protocol, known as the pre-commit phase.
- In the pre-commit phase, the coordinator sends a pre-commit request to all participants and waits for their responses.
- If all participants agree to commit, the coordinator sends a commit request in the commit phase. Otherwise, it sends an abort request in the abort phase.
- The pre-commit phase ensures that all participants are ready to commit before the actual commit phase.

3. Optimistic Replication Protocol
- This protocol assumes that conflicts between transactions are rare and allows each participant to execute transactions independently.
- Each participant keeps a local copy of the data and updates it without consulting other participants.
- Conflicts are resolved during the commit phase, where the participant that committed last wins and updates the other participants' copies.

4. Quorum-Based Protocol
- This protocol involves dividing the participants into groups or quorums.
- Each quorum has a majority of participants, and a transaction is committed only if a majority of the participants in each quorum agree to commit.
- This protocol provides fault tolerance since a minority of faulty participants cannot commit a transaction.

In conclusion, commit protocols are essential for maintaining data consistency in distributed systems. The choice of protocol depends on the requirements of the system, such as fault tolerance, consistency, and performance. Understanding these protocols is crucial for designing fault-tolerant distributed systems.