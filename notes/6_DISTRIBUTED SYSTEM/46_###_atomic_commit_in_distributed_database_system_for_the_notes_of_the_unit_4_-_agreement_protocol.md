### Atomic Commit in Distributed Database system for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM
Atomic Commit in Distributed Database System is a protocol that ensures that all transactions in a distributed database system are either fully committed or fully rolled back. The main goal of atomic commit is to maintain consistency and ensure that data is not lost or corrupted. 

The process of atomic commit involves several steps: 
1. Transaction initiation: The transaction is started by the client.
2. Pre-commit: The coordinator sends a pre-commit message to all participants to ensure that they are ready to commit.
3. Commit: If all participants respond positively to the pre-commit message, the coordinator sends a commit message to all participants.
4. Post-commit: Participants execute the transaction and send a post-commit message to the coordinator.
5. End of transaction: The coordinator sends an end-of-transaction message to all participants to indicate that the transaction is complete.

Atomic commit protocols can be further classified into two types:
1. Two-phase commit (2PC): A coordinator-based protocol where the coordinator makes the final decision to commit or abort the transaction.
2. Three-phase commit (3PC): An extension of 2PC that adds an extra phase to handle failures in the coordinator.
