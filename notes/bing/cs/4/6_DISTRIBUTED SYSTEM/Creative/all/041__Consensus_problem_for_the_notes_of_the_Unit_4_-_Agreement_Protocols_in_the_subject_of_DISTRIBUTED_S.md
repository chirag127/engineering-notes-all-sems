### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is a fundamental problem in a distributed system, where multiple processes need to agree on a common value or state to achieve overall system reliability on top of unreliable system components .
- Consensus is a property that may be achieved by protocols that exchange messages among processes to propose and decide on a final value.
- Consensus is usually required for tasks such as leader election, distributed transactions, replication, fault tolerance, and distributed commit .
- Consensus is hard to achieve in a distributed system, especially in the presence of failures, such as process crashes, network partitions, message losses, or malicious attacks  .
- Consensus algorithms are designed to cope with different types of failures and provide different levels of guarantees, such as safety (the correctness of the decision), liveness (the termination of the protocol), and fault tolerance (the resilience to failures) .
- Some examples of consensus algorithms are Paxos, Raft, Zab, Two-Phase Commit, Three-Phase Commit, and Byzantine Fault Tolerance  .
- A mnemonic to remember some of the consensus algorithms is **P**lease **R**emember **Z**oo **T**wo **T**hree **B**ytes, where each letter stands for the first letter of an algorithm  .
- A learning trick to understand the consensus problem is to imagine a group of friends trying to decide where to go for dinner, and each one has a different preference. They need to communicate with each other and reach a consensus on a single restaurant that satisfies everyone, or at least the majority. They also need to deal with possible failures, such as someone not answering the phone, someone changing their mind, or someone lying about their preference.