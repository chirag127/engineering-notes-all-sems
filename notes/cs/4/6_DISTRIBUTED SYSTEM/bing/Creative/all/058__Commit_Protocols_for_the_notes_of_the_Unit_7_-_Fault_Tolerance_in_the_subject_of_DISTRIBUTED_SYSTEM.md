### Commit Protocols for the notes of the Unit 7 - Fault Tolerance in the subject of DISTRIBUTED SYSTEM

- Commit protocols are used to ensure the atomicity property of a distributed transaction, which means that either all the operations of the transaction are executed successfully, or none of them are executed at all.
- Commit protocols involve a coordinator process that communicates with the participating processes (or servers) and decides whether to commit or abort the transaction based on their votes.
- There are different types of commit protocols, such as one-phase commit, two-phase commit, and three-phase commit, which differ in the number of phases and messages exchanged, as well as the blocking and failure recovery behavior  .

#### One-phase commit
- One-phase commit is the simplest commit protocol, which involves only one phase of communication between the coordinator and the participants.
- In this protocol, the coordinator sends a commit request to each participant, and the participant executes the transaction and commits it locally, without waiting for the coordinator's decision.
- The advantage of this protocol is that it is fast and simple, as it requires only one round of message exchange.
- The disadvantage of this protocol is that it does not guarantee atomicity, as some participants may commit the transaction while others may abort it due to failures or conflicts.
- This protocol is suitable for transactions that involve only one participant, or transactions that do not need atomicity.

#### Two-phase commit
- Two-phase commit is the most widely used commit protocol, which involves two phases of communication between the coordinator and the participants  .
- In the first phase, called the voting phase, the coordinator sends a prepare request to each participant, and the participant executes the transaction and writes the undo and redo logs to stable storage, and then votes either yes (ready to commit) or no (abort) to the coordinator .
- In the second phase, called the commit phase, the coordinator collects the votes from all the participants, and decides whether to commit or abort the transaction based on the majority rule . If all the participants vote yes, the coordinator commits the transaction and sends a commit message to each participant. If any participant votes no, or if the coordinator does not receive a vote from a participant within a timeout, the coordinator aborts the transaction and sends an abort message to each participant .
- The advantage of this protocol is that it guarantees atomicity, as all the participants follow the coordinator's decision, and the undo and redo logs can be used to recover from failures .
- The disadvantage of this protocol is that it is blocking, as the participants have to wait for the coordinator's decision after voting, and the coordinator has to wait for all the votes before deciding . If the coordinator or a participant fails during the second phase, the protocol may be stuck in an uncertain state, and manual intervention may be needed to resolve the outcome .
- This protocol is suitable for transactions that involve multiple participants, and transactions that need atomicity.

#### Three-phase commit
- Three-phase commit is an extension of the two-phase commit protocol, which involves three phases of communication between the coordinator and the participants .
- In the first phase, called the can-commit phase, the coordinator sends a can-commit request to each participant, and the participant executes the transaction and writes the undo and redo logs to stable storage, and then replies either yes (can commit) or no (abort) to the coordinator .
- In the second phase, called the pre-commit phase, the coordinator collects the replies from all the participants, and decides whether to pre-commit or abort the transaction based on the majority rule . If all the participants reply yes, the coordinator pre-commits the transaction and sends a pre-commit message to each participant. If any participant replies no, or if the coordinator does not receive a reply from a participant within a timeout, the coordinator aborts the transaction and sends an abort message to each participant .
- In the third phase, called the do-commit phase, the coordinator waits for an acknowledgement from each participant after sending the pre-commit message, and then commits the transaction and sends a do-commit