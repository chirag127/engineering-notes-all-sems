### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are used to ensure the atomicity of distributed transactions, which means that either all the operations of a transaction are executed or none of them are.
- Commit protocols involve a coordinator (or controlling site) and one or more participants (or slave sites) that execute the operations of a transaction.
- The coordinator is responsible for initiating the commit process and collecting the votes from the participants. The participants are responsible for executing the operations and sending their votes to the coordinator.
- There are three main types of commit protocols: one-phase commit, two-phase commit, and three-phase commit.

#### One-phase commit
- One-phase commit is the simplest commit protocol, but it is not fault-tolerant.
- In one-phase commit, the coordinator sends a commit request to all the participants and waits for their acknowledgments. If all the participants acknowledge, the coordinator commits the transaction and informs the participants. If any participant fails to acknowledge, the coordinator aborts the transaction and informs the participants.
- The advantage of one-phase commit is that it is fast and simple, as it requires only one round of communication between the coordinator and the participants.
- The disadvantage of one-phase commit is that it is not resilient to failures. If the coordinator fails after sending the commit request, the participants do not know whether to commit or abort the transaction. If a participant fails after receiving the commit request, the coordinator does not know whether the participant has committed or aborted the transaction.

#### Two-phase commit
- Two-phase commit is the most widely used commit protocol, as it is fault-tolerant and ensures atomicity.
- In two-phase commit, the coordinator initiates the commit process by sending a prepare request to all the participants and waits for their votes. The participants execute the operations and send their votes (commit or abort) to the coordinator. This is the first phase of the protocol, called the voting phase.
- In the second phase, called the decision phase, the coordinator decides whether to commit or abort the transaction based on the votes. If all the participants vote commit, the coordinator commits the transaction and sends a commit message to all the participants. If any participant votes abort, the coordinator aborts the transaction and sends an abort message to all the participants. The participants then follow the decision of the coordinator and send an acknowledgment to the coordinator.
- The advantage of two-phase commit is that it ensures atomicity and consistency, as all the participants agree on the outcome of the transaction.
- The disadvantage of two-phase commit is that it is blocking, which means that if the coordinator fails after receiving the votes, the participants are blocked in the prepared state and cannot proceed with other transactions until the coordinator recovers. Similarly, if a participant fails after sending its vote, the coordinator is blocked in the waiting state and cannot decide the outcome of the transaction until the participant recovers.

#### Three-phase commit
- Three-phase commit is an extension of two-phase commit that aims to overcome the blocking problem by introducing an extra phase, called the pre-commit phase.
- In three-phase commit, the coordinator initiates the commit process by sending a prepare request to all the participants and waits for their votes. The participants execute the operations and send their votes (commit or abort) to the coordinator. This is the first phase of the protocol, called the voting phase.
- In the second phase, called the pre-commit phase, the coordinator decides whether to commit or abort the transaction based on the votes. If all the participants vote commit, the coordinator sends a pre-commit message to all the participants and waits for their acknowledgments. If any participant votes abort, the coordinator aborts the transaction and sends an abort message to all the participants. The participants then follow the decision of the coordinator and send an acknowledgment to the coordinator.
- In the third phase, called the commit phase, the coordinator sends a commit message to all the participants and waits for their acknowledgments. The participants then commit the transaction and send an acknowledgment to the coordinator.
- The advantage of three-phase commit is that it is non-blocking, which means that if the coordinator fails after sending the pre-commit message, the participants can decide to commit the transaction without waiting for the coordinator. Similarly, if a participant fails after sending its acknowledgment, the coordinator can decide to commit the transaction without waiting for the participant.
- The disadvantage of three-phase commit is that it requires more messages and rounds of communication than two-phase commit, which increases the latency and overhead of the protocol.

#### Mnemonics and learning tricks
- One way to remember the difference between the three commit protocols is