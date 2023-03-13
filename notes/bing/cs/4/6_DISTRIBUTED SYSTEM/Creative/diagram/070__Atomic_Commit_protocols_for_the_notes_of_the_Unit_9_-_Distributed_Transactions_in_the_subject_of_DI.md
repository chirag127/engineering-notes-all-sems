An atomic commit protocol is a distributed algorithm that coordinates all the processes that participate in a distributed atomic transaction on whether to commit or abort the transaction. There are different types of atomic commit protocols, such as two-phase commit protocol and three-phase commit protocol. 

The two-phase commit protocol consists of two phases: prepare phase and commit phase. In the prepare phase, the coordinator sends a prepare message to all the participants and waits for their votes. The participants execute the transaction and send either a yes or a no vote to the coordinator. In the commit phase, the coordinator decides whether to commit or abort the transaction based on the votes. If all the votes are yes, the coordinator sends a commit message to all the participants and commits the transaction. If any vote is no, the coordinator sends an abort message to all the participants and aborts the transaction. The participants follow the coordinator's decision and either commit or abort the transaction.

The three-phase commit protocol seeks to remove the main problem with the two-phase commit protocol, which occurs if a coordinator and another node fail at the same time during the commit phase neither can tell what action should occur. To solve this problem a third phase is added to the protocol. The three-phase commit protocol consists of three phases: can commit phase, pre-commit phase and do commit phase. In the can commit phase, the coordinator sends a can commit message to all the participants and waits for their votes. The participants execute the transaction and send either a yes or a no vote to the coordinator. In the pre-commit phase, the coordinator decides whether to commit or abort the transaction based on the votes. If all the votes are yes, the coordinator sends a pre-commit message to all the participants and waits for their acknowledgments. If any vote is no, the coordinator sends an abort message to all the participants and aborts the transaction. The participants acknowledge the pre-commit message and enter a prepared state. In the do commit phase, the coordinator sends a do commit message to all the participants and commits the transaction. The participants follow the coordinator's decision and either commit or abort the transaction.

The following diagram illustrates the basic architecture of a two-phase commit protocol in markdown:

```
+-------------+     +-------------+     +-------------+
| Coordinator |     | Participant |     | Participant |
+-------------+     +-------------+     +-------------+
      |                   |                   |
      |-----Prepare-----> |                   |
      |                   |-----Prepare-----> |
      |                   |                   |
      |<----Yes/No------- |                   |
      |                   |<----Yes/No------- |
      |                   |                   |
      |-----Commit/Abort->|                   |
      |                   |-----Commit/Abort->|
      |                   |                   |
      |<----Ack---------- |                   |
      |                   |<----Ack---------- |
      |                   |                   |
```

The following diagram illustrates the basic architecture of a three-phase commit protocol in markdown:

```
+-------------+     +-------------+     +-------------+
| Coordinator |     | Participant |     | Participant |
+-------------+     +-------------+     +-------------+
      |                   |                   |
      |---Can Commit----> |                   |
      |                   |---Can Commit----> |
      |                   |                   |
      |<----Yes/No------- |                   |
      |                   |<----Yes/No------- |
      |                   |                   |
      |---Pre-Commit/Abort>|                   |
      |                   |---Pre-Commit/Abort>|
      |                   |                   |
      |<----Ack---------- |                   |
      |                   |<----Ack---------- |
      |                   |                   |
      |---Do Commit------>|                   |
      |                   |---Do Commit------>|
      |                   |                   |
      |<----Ack---------- |                   |
      |                   |<----Ack---------- |
      |                   |                   |
```