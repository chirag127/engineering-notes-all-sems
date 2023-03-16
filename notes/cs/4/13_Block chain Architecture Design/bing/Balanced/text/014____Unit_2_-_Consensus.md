## Unit 2 - Consensus

- Consensus is the process of reaching agreement among a group of participants on a common state of a system or a value of a variable.
- Consensus is essential for distributed systems that need to coordinate their actions or maintain a consistent view of the system state, such as databases, blockchains, or peer-to-peer networks.
- Consensus is challenging to achieve in the presence of faults, such as network delays, message losses, or node failures.
- Consensus algorithms are designed to ensure that the group of participants can eventually agree on a value, even if some of them are faulty or malicious.
- Consensus algorithms have different properties and trade-offs, such as:
  - Safety: the property that the participants will not agree on conflicting values.
  - Liveness: the property that the participants will eventually agree on a value.
  - Fault tolerance: the ability to withstand a certain number of faulty or malicious participants.
  - Performance: the efficiency and scalability of the algorithm in terms of communication, computation, and latency.
- Some examples of consensus algorithms are:
  - Paxos: a family of algorithms that ensure safety and liveness in asynchronous networks with up to half of the participants being faulty.
  - Raft: a simplified version of Paxos that is easier to understand and implement, and that uses a leader-based approach to achieve consensus.
  - Byzantine fault tolerance (BFT): a class of algorithms that ensure safety and liveness in asynchronous networks with up to one-third of the participants being malicious or arbitrary.
  - Proof-of-work (PoW): a probabilistic consensus algorithm that relies on cryptographic puzzles to elect a leader and validate transactions, such as in Bitcoin.
  - Proof-of-stake (PoS): a consensus algorithm that relies on the stake or wealth of the participants to elect a leader and validate transactions, such as in Ethereum 2.0.