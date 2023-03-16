### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to cope with failures, such as network partitions, message losses, node crashes, or malicious attacks.
- There are many ways in which processes in a distributed system can reach a consensus, but there is usually a trade-off between security and performance.
- The more we want our algorithm to be secure against ways in which failure can happen, the less performant it tends to become.
- Some of the common consensus algorithms in distributed systems are:
  - Two-phase commit (2PC): A simple and widely used protocol that involves a coordinator and a set of participants.
  - Three-phase commit (3PC): An extension of 2PC that adds a pre-commit phase to avoid blocking in case of coordinator failure.
  - Paxos: A family of protocols that use a leader election and a majority voting mechanism to achieve consensus in the presence of failures.
  - Raft: A simplified version of Paxos that is easier to understand and implement, and that also provides strong consistency and fault tolerance.
  - Byzantine fault tolerance (BFT): A class of protocols that can tolerate arbitrary failures, including malicious or faulty nodes, by requiring a supermajority of nodes to agree.
- The consensus problem is proven to be impossible to solve in a fully asynchronous distributed system with even one faulty process.
- This is known as the FLP impossibility result, named after the authors Fischer, Lynch and Paterson.
- However, the consensus problem can be solved in a partially synchronous or a synchronous distributed system, or by making some assumptions about the failure model or the network behavior.