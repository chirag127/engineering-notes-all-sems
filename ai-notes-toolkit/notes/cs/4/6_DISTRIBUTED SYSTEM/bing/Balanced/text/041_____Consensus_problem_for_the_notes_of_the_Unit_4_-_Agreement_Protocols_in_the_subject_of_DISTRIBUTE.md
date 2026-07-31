### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- Consensus is hard to achieve in a distributed system due to the possibility of node failures, network partitions, message delays, and malicious attacks .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator node to initiate and finalize the consensus among all participants.
  - Three-phase commit: An extension of two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum of nodes to propose and accept values, and tolerate up to half of the nodes to fail.
  - Raft: A simplified version of Paxos that uses a leader node to propose values and replicate them to follower nodes, and handles leader election and log consistency.
  - Byzantine fault tolerance: A class of protocols that can tolerate arbitrary failures or malicious behaviors of up to one-third of the nodes, and use cryptographic techniques to ensure agreement.