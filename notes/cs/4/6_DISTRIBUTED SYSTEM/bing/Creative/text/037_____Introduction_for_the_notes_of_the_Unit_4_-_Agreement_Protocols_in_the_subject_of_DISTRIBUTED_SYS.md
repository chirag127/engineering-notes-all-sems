### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are algorithms that enable the processes in a distributed system to reach a common decision or consensus on some value or action, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the consistency, reliability, and availability of distributed systems, especially in applications such as fault-tolerant services, distributed transactions, distributed databases, distributed ledgers, and distributed consensus.
- Some of the challenges and issues that agreement protocols need to address are:
  - How to deal with partial failures, such as process crashes, network partitions, or message losses?
  - How to cope with malicious failures, such as Byzantine faults, where some processes may behave arbitrarily or dishonestly?
  - How to handle asynchrony, where there is no bound on the message delays or the relative speeds of the processes?
  - How to achieve efficiency, scalability, and fault-tolerance, while minimizing the communication and computation overheads?
- Some of the types and variants of agreement protocols are:
  - Atomic commit protocols, which ensure that a set of processes either all commit or all abort a transaction.
  - Consensus protocols, which ensure that a set of processes agree on a single value proposed by one or more of them.
  - Byzantine agreement protocols, which are consensus protocols that can tolerate Byzantine faults.
  - Paxos and Raft protocols, which are consensus protocols that are widely used in practical distributed systems.
  - Multi-Paxos and Viewstamped Replication protocols, which are extensions of Paxos and Raft that enable state machine replication.
  - Leader election protocols, which ensure that a set of processes elect a unique leader among them.
  - Mutual exclusion protocols, which ensure that a set of processes can access a shared resource in a mutually exclusive manner.