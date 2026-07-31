### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is essential for ensuring reliability, consistency, fault-tolerance, and availability in distributed systems .
- Consensus is challenging to achieve in distributed systems because of the possibility of failures, such as network partitions, message losses, node crashes, or malicious attacks  .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- Some of the common consensus protocols are:
  - Two-phase commit: A simple and centralized protocol that requires a coordinator node to initiate and finalize the decision based on the votes of the other nodes.
  - Three-phase commit: An extension of the two-phase commit that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of decentralized protocols that use a quorum of nodes to propose and accept values, and ensure that only one value is chosen.
  - Raft: A simplified version of Paxos that divides the consensus problem into leader election, log replication, and safety.
  - Byzantine fault tolerance: A class of protocols that can tolerate arbitrary failures, including malicious behavior, by requiring a supermajority of nodes to agree.