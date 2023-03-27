### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

In distributed transactions, atomicity is a vital property that ensures the consistency of the system. Atomic commit protocols ensure that either all the transactions are committed or none of them are. This is a crucial step in maintaining data integrity in a distributed system. Here are some of the atomic commit protocols:

1. Two-Phase Commit (2PC)
   - It is the most widely used atomic commit protocol.
   - It consists of two phases: the prepare phase and the commit phase.
   - In the prepare phase, the coordinator sends a prepare message to all the participants, and they respond with a yes or no. If all agree, the coordinator sends a commit message in the commit phase, and if any participant disagrees, the coordinator sends an abort message.
   - 2PC is a blocking protocol, which means that it waits for all participants to respond before proceeding.

2. Three-Phase Commit (3PC)
   - It is an extension of 2PC that adds another phase to the protocol.
   - The additional phase is the pre-commit phase, where the participants inform the coordinator that they are ready to commit.
   - If all the participants are ready to commit in the pre-commit phase, the coordinator sends a commit message in the commit phase, and if any participant disagrees, the coordinator sends an abort message.
   - Unlike 2PC, 3PC is a non-blocking protocol, which means that it does not wait for all participants to respond before proceeding.

3. Paxos Commit Protocol
   - It is a consensus-based atomic commit protocol.
   - It uses a voting mechanism to ensure that all the participants agree on the commit decision.
   - It consists of two phases: the prepare phase and the accept phase.
   - In the prepare phase, the coordinator proposes a value to all the participants, and they respond with a yes or no. If a participant agrees, it sends an accept message in the accept phase.
   - Paxos can handle failures and recover from them.

In conclusion, atomic commit protocols ensure that data integrity is maintained in a distributed system. Two-Phase Commit, Three-Phase Commit, and Paxos Commit Protocol are some of the well-known atomic commit protocols that ensure the atomicity of transactions.