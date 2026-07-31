## Unit 4 - Agreement Protocols

Agreement protocols are an essential component of any distributed system. They help ensure that nodes in a network can reach a consensus on the state of the system and make decisions in a coordinated manner. In this unit, we will cover the following topics related to agreement protocols:

- **Consensus Algorithms:** Consensus algorithms are used to ensure that all nodes in a distributed system agree on a particular value or decision. Some commonly used consensus algorithms include Paxos, Raft, and Byzantine Fault Tolerance (BFT).

- **Paxos Algorithm:** The Paxos algorithm was developed by Leslie Lamport and is used to ensure that a distributed system can reach consensus on a value even if some nodes fail or behave maliciously. The algorithm works by having nodes propose values and then vote on them, with multiple rounds of voting occurring until a value is agreed upon.

- **Raft Algorithm:** The Raft algorithm is a consensus algorithm that was designed to be more understandable than Paxos while still providing strong guarantees of safety and consistency. It works by electing a leader who is responsible for managing the state of the system and ensuring that all nodes agree on the same state.

- **Byzantine Fault Tolerance (BFT):** BFT is a class of consensus algorithms that are designed to tolerate malicious behavior by nodes in a distributed system. These algorithms typically require a higher number of nodes to agree on a decision in order to ensure that a malicious node cannot sway the decision.

- **State Machine Replication:** State machine replication is a technique used to ensure that all nodes in a distributed system execute the same sequence of commands in the same order. This is achieved by replicating the state machine across all nodes and ensuring that all commands are executed in the same order on each node.

- **Atomic Broadcast:** Atomic broadcast is a protocol used to ensure that messages are delivered to all nodes in a distributed system in the same order. This is achieved by having a designated broadcaster node that ensures all messages are delivered to all nodes in the same order.

Agreement protocols are critical to the functioning of distributed systems, and a thorough understanding of these protocols is essential for any developer working on distributed systems.