### Consensus problem

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for ensuring the reliability, consistency and fault-tolerance of a distributed system.
- Consensus is challenging to achieve in a distributed system because of the possibility of failures, delays, asynchrony and malicious behavior of the nodes  .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator node to initiate and finalize the consensus among the participant nodes.
  - Three-phase commit: An extension of the two-phase commit protocol that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum-based approach to tolerate failures and asynchrony among the nodes.
  - Raft: A simplified version of Paxos that uses a leader election mechanism and a replicated state machine to achieve consensus.