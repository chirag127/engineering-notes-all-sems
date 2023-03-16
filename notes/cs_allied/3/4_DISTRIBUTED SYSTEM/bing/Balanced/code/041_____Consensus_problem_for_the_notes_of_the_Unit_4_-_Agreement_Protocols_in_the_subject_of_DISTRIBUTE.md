### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate distributed transactions, replicate data, elect leaders, and implement fault tolerance mechanisms.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, and malicious attacks .
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): A simple and efficient protocol that requires a coordinator node to initiate a commit request to all other nodes, and then decide to commit or abort based on their responses.
  - Three-phase commit (3PC): An extension of 2PC that adds a pre-commit phase to avoid blocking in case of a coordinator failure.
  - Paxos: A family of protocols that use a quorum-based approach to elect a leader and propose values to be agreed upon by the majority of nodes.
  - Raft: A simplified version of Paxos that divides the consensus problem into three subproblems: leader election, log replication, and safety.
  - Byzantine fault tolerance (BFT): A class of protocols that can tolerate arbitrary failures, including malicious or faulty nodes, by requiring a supermajority of nodes (usually 2/3 or more) to agree on a value.