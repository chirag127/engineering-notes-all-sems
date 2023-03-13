### System model and group communication for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- A system model is an abstraction that describes the properties and behaviors of a distributed system, such as its components, communication channels, failures, and assumptions.
- A group is a collection of interconnected processes that cooperate to achieve a common goal, such as data replication, fault tolerance, or load balancing.
- Group communication is the exchange of messages between processes that belong to the same group or different groups in a distributed system.
- Group communication can be classified into two types: broadcast communication and multicast communication.
- Broadcast communication is when a source process sends a message to every other process in the system, regardless of their group membership. Broadcast communication can be used to disseminate information, synchronize clocks, or elect a leader.
- Multicast communication is when a source process sends a message to a subset of processes in the system, based on their group membership. Multicast communication can be used to replicate data, coordinate actions, or implement consensus.
- Group communication can also be characterized by the reliability and ordering guarantees it provides.
- Reliable group communication ensures that every message sent by a process is eventually delivered to every other process in the group, unless the sender or the receiver fails.
- Ordered group communication ensures that messages are delivered in a consistent order across the group, such as FIFO, causal, or total order.
- Replication is the technique of maintaining multiple copies of the same data or service across different processes or nodes in a distributed system.
- Replication can improve the availability, performance, and fault tolerance of a distributed system, but it also introduces the challenge of maintaining consistency among the replicas.
- Consistency is the property that ensures that all replicas of the same data or service have the same state or behavior at any given time, or eventually converge to the same state or behavior.
- Consistency can be classified into two types: strong consistency and weak consistency.
- Strong consistency requires that all replicas of the same data or service are always in sync, and any update or request is immediately reflected on all replicas. Strong consistency can be achieved by using protocols such as two-phase commit, Paxos, or Raft.
- Weak consistency allows some replicas of the same data or service to be temporarily out of sync, and updates or requests are eventually propagated to all replicas. Weak consistency can be achieved by using protocols such as eventual consistency, gossip, or CRDTs.
- The choice of consistency model depends on the trade-off between the consistency, availability, and partition tolerance of the system, as stated by the CAP theorem.
- The CAP theorem states that it is impossible for a distributed system to simultaneously provide all three of the following guarantees: consistency, availability, and partition tolerance.
- Consistency means that every read operation returns the most recent write or an error.
- Availability means that every request receives a response, without guaranteeing that it contains the most recent write.
- Partition tolerance means that the system continues to operate despite arbitrary message loss or failure of part of the system.
- According to the CAP theorem, a distributed system can only provide two of these guarantees at the same time, and must sacrifice the third one in the presence of network partitions.
- For example, a system that chooses consistency and availability over partition tolerance will have to stop serving requests if a network partition occurs, while a system that chooses consistency and partition tolerance over availability will have to reject some requests if a network partition occurs.
- A system that chooses availability and partition tolerance over consistency will have to return stale or inconsistent data if a network partition occurs.
- Therefore, the system model and group communication for replication in distributed systems depend on the requirements and trade-offs of the application domain, the network environment, and the failure scenarios.

: Group Communication in distributed Systems - GeeksforGeeks
: Reliable group communication - Distributed Systems
: Replication in distributed systems - George Mason University
: Understanding Replication in Databases and Distributed Systems