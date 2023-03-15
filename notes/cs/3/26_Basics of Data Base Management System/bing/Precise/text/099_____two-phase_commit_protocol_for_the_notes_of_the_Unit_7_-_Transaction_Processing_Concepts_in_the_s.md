### Two-Phase Commit Protocol

The two-phase commit protocol (2PC) is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. It is a specialized type of consensus protocol.

The protocol achieves its goal even in many cases of temporary system failure (involving either process, network node, communication, etc. failures), and is thus widely used. However, it is not resilient to all possible failure configurations, and in rare cases, user (e.g., a system's administrator) intervention is needed to remedy an outcome. To accommodate recovery from failure (automatic in most cases) the protocol's participants use logging of the protocol's states. Log records, which are typically slow to generate but survive failures, are used by the protocol's recovery procedures. Many protocol variants exist that primarily differ in the number of states logged and the number of messages exchanged.

#### Phase 1: Voting

1. The coordinator sends a query to commit message to all participants and waits until it has received a reply from all participants.
2. The participants execute the transaction up to the point where they will be asked to commit. They each write an entry to their undo log and an entry to their redo log.
3. Each participant replies with an agreement message (participant votes Yes to commit), if the participant's actions succeeded, or an abort message (participant votes No, not to commit), if the participant experiences a failure that will make it impossible to commit.

#### Phase 2: Commit or Abort

1. If the coordinator received an agreement message from all participants during phase 1, it sends a commit message to all the participants.
2. If any participant votes No during phase 1, the coordinator sends a rollback message to all the participants.
3. Each participant undoes the transaction using the undo log, and sends an acknowledgement to the coordinator.
4. The coordinator undoes the transaction using the undo log, and releases all the locks and resources held during the transaction.
5. On the other hand, if the coordinator had sent a commit message to all the participants, each participant completes the operation, and releases all the locks and resources held during the transaction. Each participant sends an acknowledgement to the coordinator.
6. The coordinator completes the transaction when all acknowledgements have been received.