# Atomic Commit Protocols

Atomic Commit Protocols are used in Distributed Systems to ensure that a transaction is either committed on all sites or aborted on all sites. This is important to maintain the consistency of data across all sites in a distributed system.

There are two main types of Atomic Commit Protocols:

1. Two-Phase Commit Protocol (2PC)
2. Three-Phase Commit Protocol (3PC)

## Two-Phase Commit Protocol (2PC)

The Two-Phase Commit Protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. The protocol is initiated by the coordinator after the last step of the transaction has been reached.

The 2PC protocol consists of two phases:

1. **Voting Phase:** In this phase, the coordinator sends a `VOTE-REQUEST` message to all participants and waits for their response. Each participant replies with either a `VOTE-COMMIT` if it is ready to commit the transaction or a `VOTE-ABORT` if it is not ready to commit the transaction.

2. **Decision Phase:** In this phase, the coordinator makes the final decision on whether to commit or abort the transaction based on the votes received from the participants. If all participants voted to commit, the coordinator sends a `GLOBAL-COMMIT` message to all participants. If any participant voted to abort, the coordinator sends a `GLOBAL-ABORT` message to all participants.

## Three-Phase Commit Protocol (3PC)

The Three-Phase Commit Protocol (3PC) is an extension of the 2PC protocol that adds an additional phase to avoid blocking in case of a coordinator failure. The 3PC protocol consists of three phases:

1. **Voting Phase:** This phase is the same as the voting phase in the 2PC protocol.

2. **Pre-Commit Phase:** In this phase, the coordinator sends a `PRE-COMMIT` message to all participants if all participants voted to commit. Each participant acknowledges the receipt of the `PRE-COMMIT` message by sending an `ACK` message to the coordinator.

3. **Commit Phase:** In this phase, the coordinator makes the final decision on whether to commit or abort the transaction based on the acknowledgements received from the participants. If all participants sent an `ACK` message, the coordinator sends a `GLOBAL-COMMIT` message to all participants. If any participant did not send an `ACK` message, the coordinator sends a `GLOBAL-ABORT` message to all participants.
