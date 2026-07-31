### Atomic Commit protocols

Atomic Commit protocols are used in distributed systems to ensure that a transaction is either committed on all sites or aborted on all sites. This is important to maintain the consistency of data across all sites in a distributed system.

There are two main types of atomic commit protocols:

1. Two-phase commit (2PC)
2. Three-phase commit (3PC)

#### Two-phase commit (2PC)

The two-phase commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. The protocol is initiated by the coordinator after the last step of the transaction has been reached.

The first phase of the protocol is the voting phase. In this phase, the coordinator sends a query to commit message to all participants and waits for their response. Each participant replies with either a yes or no vote, depending on whether it is ready to commit the transaction.

In the second phase, the decision phase, the coordinator makes a decision based on the votes received from the participants. If all participants voted yes, the coordinator sends a global commit message to all participants. If any participant voted no, the coordinator sends a global abort message to all participants.

#### Three-phase commit (3PC)

The three-phase commit protocol is an extension of the two-phase commit protocol that introduces an additional phase to make the protocol more resilient to failures. The additional phase is called the pre-commit phase.

In the pre-commit phase, the coordinator sends a pre-commit message to all participants after receiving all yes votes in the voting phase. The participants acknowledge the receipt of the pre-commit message by sending an acknowledgement to the coordinator.

In the commit phase, the coordinator sends a do-commit message to all participants after receiving all acknowledgements. The participants then commit the transaction and send an acknowledgement to the coordinator.

In the abort phase, the coordinator sends an abort message to all participants if it does not receive all acknowledgements in the pre-commit phase or if any participant voted no in the voting phase. The participants then abort the transaction.

These are the basics of Atomic Commit protocols in distributed systems. They are an important part of ensuring the consistency of data across all sites in a distributed system.