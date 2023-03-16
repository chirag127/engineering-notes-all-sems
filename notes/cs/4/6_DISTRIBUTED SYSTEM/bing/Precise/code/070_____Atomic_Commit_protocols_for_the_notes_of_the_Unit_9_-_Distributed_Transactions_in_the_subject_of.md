### Atomic Commit protocols

Atomic Commit protocols are used in distributed systems to ensure that a transaction is either committed or aborted on all participating nodes. This is important to maintain the consistency of the distributed database. There are two main types of atomic commit protocols: Two-phase commit (2PC) and Three-phase commit (3PC).

1. **Two-phase commit (2PC)**: This protocol involves two phases - the voting phase and the decision phase. In the voting phase, the coordinator sends a prepare message to all participants, asking them to vote on whether to commit or abort the transaction. If all participants vote to commit, the coordinator sends a commit message to all participants in the decision phase. If any participant votes to abort, the coordinator sends an abort message to all participants.

2. **Three-phase commit (3PC)**: This protocol is an extension of the 2PC protocol and involves an additional phase called the pre-commit phase. In the pre-commit phase, the coordinator sends a pre-commit message to all participants after receiving a vote to commit from all participants in the voting phase. The participants then send an acknowledgement to the coordinator, after which the coordinator sends a commit message to all participants in the decision phase.

Both 2PC and 3PC protocols ensure that all participants reach a consensus on whether to commit or abort a transaction. However, 3PC has an advantage over 2PC in that it can recover from certain failures, such as a coordinator failure, without blocking.
