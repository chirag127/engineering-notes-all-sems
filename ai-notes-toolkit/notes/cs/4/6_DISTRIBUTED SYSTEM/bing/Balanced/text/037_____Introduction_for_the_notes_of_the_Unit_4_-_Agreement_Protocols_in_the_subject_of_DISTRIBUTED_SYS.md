### Introduction for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- A distributed system is a collection of independent and geographically dispersed processes that communicate and coordinate their actions by passing messages.
- Agreement protocols are a class of distributed algorithms that aim to achieve a common goal or value among a set of processes, despite the presence of failures or uncertainties.
- Agreement protocols are essential for ensuring the reliability, consistency, and fault-tolerance of distributed systems, especially in applications such as distributed databases, distributed consensus, leader election, group membership, and atomic actions  .
- Some of the challenges and requirements for designing agreement protocols in distributed systems are:
  - Dealing with partial failures, such as process crashes, network partitions, message losses, or Byzantine faults .
  - Achieving termination, validity, and agreement properties, which ensure that all correct processes eventually decide on a value, the decided value is valid according to some criterion, and all correct processes agree on the same value .
  - Balancing the trade-offs between performance, complexity, and resilience, such as minimizing the number of messages, rounds, or assumptions needed to reach agreement, while maximizing the number of faults tolerated .
  - Adapting to dynamic and heterogeneous environments, such as changing network topologies, process behaviors, or system parameters.
- Some of the examples and types of agreement protocols in distributed systems are:
  - Two-phase commit and three-phase commit protocols, which are used to coordinate the commit or abort decision of a distributed transaction among multiple data managers.
  - Paxos and Raft protocols, which are used to implement distributed consensus among a set of replicas, such that they can agree on a sequence of commands or updates.
  - Bully and ring algorithms, which are used to elect a leader among a set of processes, such that the leader has the highest priority or identifier.
  - Viewstamped replication and virtual synchrony protocols, which are used to maintain a consistent view of the group membership among a set of processes, such that they can detect and handle failures or joins.
  - Lamport's and vector clocks, which are used to synchronize the logical clocks of processes, such that they can order the events or messages in a causal or consistent manner.