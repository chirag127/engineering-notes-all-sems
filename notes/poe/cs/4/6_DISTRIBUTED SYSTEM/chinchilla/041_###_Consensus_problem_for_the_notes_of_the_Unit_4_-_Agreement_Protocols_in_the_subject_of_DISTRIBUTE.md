### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

Consensus is a fundamental problem in distributed systems that requires a group of processes to agree on a common value, despite the presence of failures and potential delays in communication. The Consensus problem is a central problem in the design of distributed systems, and it is crucial for achieving fault tolerance, scalability, and consistency in distributed systems.

#### What is the Consensus problem?

The Consensus problem can be formally defined as follows: Given a set of processes in a distributed system that communicate by sending messages to each other, each process must decide on a common value, such that the following conditions hold:

- Agreement: All correct processes must agree on the same value.
- Validity: The value agreed upon must be proposed by a correct process.
- Termination: All correct processes must eventually decide on a value.

The Consensus problem is challenging because it is impossible to solve under certain failure models. For example, if a process can crash-stop, it is impossible to solve the Consensus problem with fewer than three processes. Similarly, if a process can experience Byzantine failures, where it can behave arbitrarily, it is impossible to solve the Consensus problem with fewer than three processes.

#### Learning Tricks and Mnemonics

- Remember the three conditions of Consensus with the mnemonic "AVT":
  - Agreement: All correct processes agree on the same value.
  - Validity: The value agreed upon must be proposed by a correct process.
  - Termination: All correct processes must eventually decide on a value.

#### Examples of Consensus Algorithms

- Paxos: Paxos is a widely-used Consensus algorithm that was first introduced by Leslie Lamport in 1989. Paxos uses a three-phase protocol to reach Consensus and is widely used in distributed systems like Google's Chubby lock service.
- Raft: Raft is another popular Consensus algorithm that was introduced by Diego Ongaro and John Ousterhout in 2014. Raft is designed to be more understandable than Paxos and is used in systems like etcd and CockroachDB.
- Byzantine fault-tolerant (BFT) Consensus algorithms: BFT Consensus algorithms, like Practical Byzantine Fault Tolerance (PBFT), are designed to tolerate Byzantine failures and are used in systems like Hyperledger Fabric.

#### Advantages and Disadvantages of Consensus Algorithms

- Advantages:
  - Consensus algorithms provide fault tolerance by ensuring that all correct processes agree on the same value, even in the presence of failures.
  - Consensus algorithms provide consistency by ensuring that all correct processes see the same state of the system.
  - Consensus algorithms enable scalable and distributed systems by allowing multiple processes to work together towards a common goal.
- Disadvantages:
  - Consensus algorithms can be complex and difficult to implement correctly.
  - Consensus algorithms can incur high communication overhead, especially in large-scale systems.
  - Consensus algorithms may suffer from performance degradation and reduced fault tolerance under certain failure models.