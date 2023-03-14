## Unit 2 - Consensus

Consensus is a fundamental concept in distributed systems, where multiple nodes work together to achieve a common goal. In this unit, we will explore the various algorithms and protocols used to achieve consensus in distributed systems.

### Types of Consensus Algorithms

#### 1. Paxos

Paxos is a consensus algorithm used to ensure fault-tolerance and consistency in a distributed system. It is commonly used in distributed databases, where multiple nodes need to agree on a common state. The algorithm consists of two phases: the prepare phase and the accept phase.

#### 2. Raft

Raft is another consensus algorithm used in distributed systems. It is designed to be more understandable than Paxos, and is often used in practice. Raft consists of three main components: the leader, the followers, and the candidate. The leader is responsible for managing the state of the system, while the followers and candidates vote on changes to the state.

#### 3. Byzantine Fault Tolerance (BFT)

Byzantine Fault Tolerance is a more complex consensus algorithm used in distributed systems. It is designed to tolerate not only failures but also malicious attacks on the system. BFT is often used in blockchain systems, where the nodes need to agree on the state of the ledger.

### Learning Tricks and Mnemonics

- Remember the three main components of Raft: Leader, Followers, and Candidate as LFC.
- To remember the two phases of Paxos, think of them as Prepare and Accept, or PA.

### Advantages of Consensus Algorithms

- Fault-tolerance: Consensus algorithms ensure that the system can continue to operate even if some nodes fail or become unavailable.
- Consistency: Consensus algorithms ensure that all nodes in the system agree on a common state, even if there are multiple changes happening simultaneously.
- Scalability: Consensus algorithms can scale to accommodate large numbers of nodes in the system.

### Disadvantages of Consensus Algorithms

- Complexity: Consensus algorithms can be complex and difficult to understand, making them challenging to implement and maintain.
- Latency: Consensus algorithms can introduce latency into the system, as nodes need to communicate and agree on changes before they can be applied.

### Examples of Consensus Algorithms in Practice

- Bitcoin: Bitcoin uses a variation of the BFT consensus algorithm to ensure that the nodes in the network agree on the state of the ledger.
- Apache ZooKeeper: Apache ZooKeeper uses the Paxos consensus algorithm to ensure that all nodes in the distributed system agree on a common configuration.
- CockroachDB: CockroachDB uses a variation of the Raft consensus algorithm to ensure that all nodes in the distributed database agree on a common state.

### Applications of Consensus Algorithms

- Distributed databases: Consensus algorithms are commonly used in distributed databases to ensure that all nodes in the system agree on a common state.
- Blockchain systems: Consensus algorithms are used in blockchain systems to ensure that all nodes in the network agree on the state of the ledger.
- Cloud computing: Consensus algorithms can be used in cloud computing to ensure fault-tolerance and consistency in distributed systems.