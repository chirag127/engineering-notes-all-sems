### Atomic Commit protocols for the notes of the Unit 9 - Distributed Transactions in the subject of DISTRIBUTED SYSTEM

- Atomic Commit protocols are used in distributed systems to ensure that a transaction is either committed on all sites or aborted on all sites.
- The goal of these protocols is to achieve atomicity, which means that either all changes made by a transaction are committed or none are.
- There are two main types of atomic commit protocols: Two-Phase Commit (2PC) and Three-Phase Commit (3PC).
- In 2PC, the coordinator sends a prepare message to all participants, asking them to vote on whether to commit or abort the transaction. If all participants vote to commit, the coordinator sends a commit message to all participants. If any participant votes to abort, the coordinator sends an abort message to all participants.
- In 3PC, there is an additional phase called the pre-commit phase. In this phase, the coordinator sends a pre-commit message to all participants, asking them to prepare to commit. If all participants respond with a yes, the coordinator sends a do-commit message to all participants. If any participant responds with a no, the coordinator sends an abort message to all participants.
- Both 2PC and 3PC have their advantages and disadvantages. 2PC is simpler but can result in blocking if the coordinator fails. 3PC is more complex but can avoid blocking in some failure scenarios.
- Atomic Commit protocols are an essential part of distributed transactions and help ensure data consistency in distributed systems.