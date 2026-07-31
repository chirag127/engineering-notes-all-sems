# Commit Protocols

## Introduction

- A commit protocol is a method for ensuring that a distributed transaction either commits or aborts atomically across all the participating sites.
- A commit protocol is necessary to achieve atomicity and durability in the presence of failures, such as site crashes, network partitions, or message losses.
- A commit protocol typically involves a coordinator site and one or more participant sites that exchange messages to reach a consensus on the outcome of the transaction.
- A commit protocol can be classified into two-phase commit (2PC), three-phase commit (3PC), or other variants based on the number and type of messages exchanged.

## Two-Phase Commit (2PC)

- 2PC is the most widely used commit protocol in distributed systems.
- 2PC consists of two phases: a prepare phase and a commit phase.
- In the prepare phase, the coordinator sends a PREPARE message to all the participants, asking them to vote on whether they are ready to commit or abort the transaction.
- Each participant replies with a YES vote if it has successfully executed its part of the transaction and is ready to commit, or a NO vote if it has encountered any failure or inconsistency and wants to abort the transaction.
- In the commit phase, the coordinator collects the votes from all the participants and decides the final outcome of the transaction based on the following rules:
  - If all the participants vote YES, the coordinator decides to commit the transaction and sends a COMMIT message to all the participants, instructing them to make their changes permanent and release any locks or resources held by the transaction.
  - If any participant votes NO, or if the coordinator does not receive a vote from any participant within a timeout period, the coordinator decides to abort the transaction and sends an ABORT message to all the participants, instructing them to undo their changes and release any locks or resources held by the transaction.
- Each participant follows the coordinator's decision and sends an ACK message to the coordinator, confirming that it has completed the commit or abort operation.
- The coordinator waits for the ACK messages from all the participants and then terminates the transaction.

## Three-Phase Commit (3PC)

- 3PC is a commit protocol that aims to avoid blocking in the presence of network partitions or coordinator failures.
- 3PC consists of three phases: a prepare phase, a pre-commit phase, and a commit phase.
- In the prepare phase, the coordinator sends a PREPARE message to all the participants, asking them to vote on whether they are ready to commit or abort the transaction.
- Each participant replies with a YES vote if it has successfully executed its part of the transaction and is ready to commit, or a NO vote if it has encountered any failure or inconsistency and wants to abort the transaction.
- In the pre-commit phase, the coordinator collects the votes from all the participants and decides the final outcome of the transaction based on the following rules:
  - If all the participants vote YES, the coordinator decides to commit the transaction and sends a PRE-COMMIT message to all the participants, instructing them to prepare to commit the transaction and wait for the final confirmation.
  - If any participant votes NO, or if the coordinator does not receive a vote from any participant within a timeout period, the coordinator decides to abort the transaction and sends an ABORT message to all the participants, instructing them to undo their changes and release any locks or resources held by the transaction.
- Each participant follows the coordinator's decision and sends an ACK message to the coordinator, confirming that it has received the PRE-COMMIT or ABORT message.
- In the commit phase, the coordinator waits for the ACK messages from all the participants and then sends a COMMIT message to all the participants, instructing them to make their changes permanent and release any locks or resources held by the transaction.
- Each participant follows the coordinator's decision and sends an ACK message to the coordinator, confirming that it has completed the commit or abort operation.
- The coordinator waits for the ACK messages from all the participants and then terminates the transaction.