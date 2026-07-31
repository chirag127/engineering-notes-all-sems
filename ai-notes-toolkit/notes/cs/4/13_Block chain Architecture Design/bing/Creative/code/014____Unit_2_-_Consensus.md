## Unit 2 - Consensus

Consensus is the process of reaching agreement among a group of participants on a common decision or action. Consensus is important for distributed systems, where multiple nodes need to coordinate their state and behavior in the presence of failures and network delays.

Some key concepts and challenges of consensus are:

- **Consensus problem**: The problem of designing a protocol that allows a set of nodes to agree on a single value from a set of possible values, despite the possibility of some nodes being faulty or malicious.
- **Consensus protocol**: A protocol that solves the consensus problem, such as Paxos, Raft, or Byzantine Fault Tolerance (BFT).
- **Safety**: The property that the protocol guarantees that all correct nodes will eventually agree on the same value, and that the value is valid according to some predefined criteria.
- **Liveness**: The property that the protocol guarantees that all correct nodes will eventually decide on a value, and that the protocol will make progress even in the presence of failures and delays.
- **Fault tolerance**: The ability of the protocol to tolerate different types of faults, such as crash faults, where a node stops responding, or Byzantine faults, where a node behaves arbitrarily or maliciously.
- **Quorum**: A subset of nodes that is large enough to ensure safety and liveness of the protocol. For example, in a majority quorum, at least half of the nodes plus one must agree on a value.
- **Leader**: A node that proposes a value to the other nodes and coordinates the consensus process. Some protocols use a fixed leader, while others use a dynamic leader election mechanism.
- **Round**: A phase of the protocol where nodes exchange messages and try to reach agreement on a value. Some protocols use a fixed number of rounds, while others use a variable number of rounds depending on the network conditions.