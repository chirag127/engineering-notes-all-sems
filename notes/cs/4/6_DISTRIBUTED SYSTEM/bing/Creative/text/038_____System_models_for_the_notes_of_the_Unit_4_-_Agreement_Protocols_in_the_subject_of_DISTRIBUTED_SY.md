### System models for distributed systems

System models are abstract descriptions of the properties and behaviors of distributed systems. They help to understand, design, and implement distributed systems by providing common concepts and terminology. System models can be classified into three types:

- **Architectural models**: describe the structure and organization of the components of a distributed system and their interactions. Architectural models can be further divided into subtypes based on the roles and responsibilities of the components, such as client-server, peer-to-peer, publish-subscribe, etc.
- **Interaction models**: describe the communication and coordination mechanisms among the components of a distributed system. Interaction models can be further divided into subtypes based on the timing, ordering, and reliability of the messages, such as synchronous, asynchronous, causal, atomic, etc.
- **Fault models**: describe the types and effects of failures that can occur in a distributed system and the assumptions and guarantees that can be made about them. Fault models can be further divided into subtypes based on the nature and severity of the failures, such as crash, omission, timing, byzantine, etc.

System models are useful for the study of agreement protocols in distributed systems, which are algorithms that allow the components to reach a consistent state or decision despite the presence of faults and uncertainties. Agreement protocols can be classified into three types:

- **Consensus protocols**: require the components to agree on a single value from a set of proposed values. Consensus protocols are essential for achieving fault tolerance and consistency in distributed systems, such as distributed databases, blockchain, and leader election.
- **Atomic broadcast protocols**: require the components to deliver the same set of messages in the same order. Atomic broadcast protocols are useful for implementing replicated state machines and distributed transactions in distributed systems, such as distributed commit, Paxos, and Raft.
- **Mutual exclusion protocols**: require the components to access a shared resource in a mutually exclusive manner. Mutual exclusion protocols are important for ensuring correctness and fairness in distributed systems, such as distributed locks, tokens, and quorums.