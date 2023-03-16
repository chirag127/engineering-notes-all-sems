# Atomic Commit Protocols

Atomic Commit Protocols are used in Distributed Systems to ensure that a transaction is either completed successfully or aborted completely. This is important in a distributed system where multiple nodes are involved in a transaction and a failure at any node can result in an inconsistent state.

There are two main types of Atomic Commit Protocols:

1. Two-Phase Commit Protocol (2PC)
2. Three-Phase Commit Protocol (3PC)

## Two-Phase Commit Protocol (2PC)

The Two-Phase Commit Protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. It is a blocking protocol, meaning that if the coordinator fails permanently, some participants will be blocked, unable to decide on the outcome of the transaction.

The 2PC protocol consists of two phases:

1. **Voting Phase**: The coordinator sends a query to commit message to all participants and waits for their response. Each participant replies with either a yes or no vote.
2. **Decision Phase**: If all participants voted yes, the coordinator sends a global commit message to all participants. If any participant voted no, the coordinator sends a global abort message to all participants.

## Three-Phase Commit Protocol (3PC)

The Three-Phase Commit Protocol (3PC) is an extension of the 2PC protocol that aims to solve the blocking problem of the 2PC protocol. It introduces an additional phase, the pre-commit phase, to ensure that no participant is blocked in case of a coordinator failure.

The 3PC protocol consists of three phases:

1. **Voting Phase**: Same as the voting phase of the 2PC protocol.
2. **Pre-Commit Phase**: If all participants voted yes, the coordinator sends a pre-commit message to all participants and waits for their acknowledgement.
3. **Commit Phase**: After receiving acknowledgement from all participants, the coordinator sends a global commit message to all participants. If any participant voted no or if the coordinator did not receive acknowledgement from all participants, the coordinator sends a global abort message to all participants.

These are the basics of Atomic Commit Protocols in Distributed Systems. They play a crucial role in ensuring the consistency and reliability of transactions in a distributed environment.