
### Commit Protocols for the Notes of the Unit 7 - Fault Tolerance in the Subject of DISTRIBUTED SYSTEM

Commit protocols are used in distributed systems to ensure that data is consistent across all nodes in the system. They are used to ensure that all nodes in the system agree on the same state of the data and to prevent conflicting updates from different nodes.

There are two main types of commit protocols: two-phase commit (2PC) and three-phase commit (3PC).

**Two-Phase Commit (2PC)**

The two-phase commit protocol is the most basic commit protocol. It consists of two phases: the prepare phase and the commit phase.

In the prepare phase, the coordinator node sends a message to all other nodes in the system, asking them to prepare to commit. If all the nodes acknowledge the request, the coordinator sends a commit message. If any of the nodes fail to acknowledge the request, the coordinator sends an abort message.

In the commit phase, the coordinator sends a commit message to all the nodes. This message tells the nodes to commit their changes. If all the nodes acknowledge the request, the changes are committed and the protocol is complete. If any of the nodes fail to acknowledge the request, the coordinator sends an abort message and the changes are not committed.

**Three-Phase Commit (3PC)**

The three-phase commit protocol is more complex than the two-phase commit protocol. It consists of three phases: the prepare phase, the voting phase, and the commit phase.

In the prepare phase, the coordinator node sends a message to all other nodes in the system, asking them to prepare to commit. If all the nodes acknowledge the request, the coordinator sends a vote message. If any of the nodes fail to acknowledge the request, the coordinator sends an abort message.

In the voting phase, the coordinator sends a vote message to all the nodes. This message tells the nodes to vote on whether or not to commit the changes. If all the nodes vote to commit, the coordinator sends a commit message. If any of the nodes vote to abort, the coordinator sends an abort message.

In the commit phase, the coordinator sends a commit message to all the nodes. This message tells the nodes to commit their changes. If all the nodes acknowledge the request, the changes are committed and the protocol is complete. If any of the nodes fail to acknowledge the request, the coordinator sends an abort message and the changes are not committed.

Mnemonics and Learning Tricks: 
- Two-Phase Commit (2PC): "Prepare, Commit, or Abort"
- Three-Phase Commit (3PC): "Prepare, Vote, Commit, or Abort"