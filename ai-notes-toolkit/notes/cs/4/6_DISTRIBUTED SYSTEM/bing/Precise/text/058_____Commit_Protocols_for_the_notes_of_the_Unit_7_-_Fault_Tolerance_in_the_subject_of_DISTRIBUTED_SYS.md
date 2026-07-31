### Commit Protocols

Commit protocols are used in distributed systems to ensure that a transaction is either completed successfully or aborted, even in the presence of failures. These protocols are an essential part of fault tolerance in distributed systems.

1. **Two-phase commit (2PC)**: This protocol involves two phases, the prepare phase and the commit phase. In the prepare phase, the coordinator sends a prepare message to all participants, asking if they are ready to commit. If all participants respond with a yes, the coordinator sends a commit message to all participants in the commit phase. If any participant responds with a no, the coordinator sends an abort message to all participants.

2. **Three-phase commit (3PC)**: This protocol is an extension of the two-phase commit protocol and adds an additional phase, the pre-commit phase. In the pre-commit phase, the coordinator sends a pre-commit message to all participants after receiving a yes from all participants in the prepare phase. If all participants respond with an acknowledgment, the coordinator sends a commit message to all participants in the commit phase. If any participant fails to respond with an acknowledgment, the coordinator sends an abort message to all participants.

These are two common commit protocols used in distributed systems to ensure fault tolerance. They help to ensure that transactions are either completed successfully or aborted, even in the presence of failures.