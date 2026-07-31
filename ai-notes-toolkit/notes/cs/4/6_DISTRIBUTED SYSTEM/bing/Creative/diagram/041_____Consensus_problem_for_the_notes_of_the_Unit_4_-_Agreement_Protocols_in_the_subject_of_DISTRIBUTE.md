### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate the actions of different nodes, such as committing transactions, electing leaders, replicating data, etc.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, etc.
- Consensus algorithms are protocols that enable nodes to reach consensus in a distributed system despite failures.
- Consensus algorithms have to satisfy some properties, such as:
  - Termination: every correct node eventually decides on a value.
  - Agreement: every correct node that decides, decides on the same value.
  - Validity: if a correct node decides on a value, then that value was proposed by some node.
- Some examples of consensus algorithms are:
  - Two-phase commit: a simple protocol that involves a coordinator node and a set of participant nodes. The coordinator proposes a value and asks the participants to vote. If all participants agree, the coordinator commits the value and notifies the participants. Otherwise, the coordinator aborts the value and notifies the participants.
  - Paxos: a more complex protocol that involves a set of proposer nodes, a set of acceptor nodes, and a set of learner nodes. The proposers propose values and the acceptors vote on them. The learners learn the decided value from the acceptors. The protocol ensures that at most one value is decided and that value is chosen by a majority of acceptors.
  - Raft: a simpler protocol that involves a set of server nodes and a set of client nodes. The servers elect a leader among themselves and the leader proposes values to the followers. The followers append the values to their logs and acknowledge the leader. The leader commits the values when a majority of followers have appended them. The clients interact with the leader to propose values or query the system state.