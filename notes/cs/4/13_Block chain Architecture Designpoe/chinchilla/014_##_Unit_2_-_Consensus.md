## Unit 2 - Consensus

Consensus is an important concept in distributed systems, where multiple nodes need to agree on a decision or a value. It is a fundamental problem in computer science and has many applications, such as in blockchain, distributed databases, and distributed storage systems. In this unit, we will learn about different algorithms and techniques that are used to achieve consensus in distributed systems.

### Paxos Algorithm

Paxos is a widely used algorithm for achieving consensus in distributed systems. It was developed by Leslie Lamport in 1990 and is known for its simplicity and fault-tolerance. The algorithm works by electing a leader, who proposes a value to the other nodes. The nodes then vote on the value, and if a quorum (a majority of the nodes) agrees, the value is accepted.

### Raft Algorithm

The Raft algorithm is another consensus algorithm that is designed to be more understandable than Paxos. It was developed by Diego Ongaro and John Ousterhout in 2013 and is based on the concept of a replicated state machine. The algorithm works by electing a leader, who is responsible for coordinating the state changes. If the leader fails, a new leader is elected.

### Byzantine Fault Tolerance

Byzantine Fault Tolerance (BFT) is a concept in distributed systems that refers to the ability of a system to tolerate failures, including malicious attacks. It is named after the Byzantine Generals' Problem, which is a thought experiment that explores the difficulties of achieving consensus in the presence of faulty nodes. BFT algorithms are designed to be resilient to attacks and can tolerate up to a certain number of faulty nodes.

### Practical Byzantine Fault Tolerance

Practical Byzantine Fault Tolerance (PBFT) is a BFT algorithm that was developed by Miguel Castro and Barbara Liskov in 1999. It is designed to be practical for use in real-world applications and can tolerate up to a third of the nodes being faulty. PBFT works by electing a primary node, which proposes a value to the other nodes. The other nodes then vote on the value, and if a quorum agrees, the value is accepted.

## Mnemonics and Learning Tricks

- To remember the difference between Paxos and Raft, think of Paxos as a more complex algorithm that is better suited for large-scale distributed systems, while Raft is simpler and easier to understand, making it more suitable for smaller-scale systems.

- To remember the concept of Byzantine Fault Tolerance, think of the Byzantine Generals' Problem, which is a thought experiment that explores the difficulties of achieving consensus in the presence of faulty nodes.

- To remember the difference between PBFT and other BFT algorithms, think of PBFT as being more practical and suitable for real-world applications, while other BFT algorithms may be more theoretical and less practical.