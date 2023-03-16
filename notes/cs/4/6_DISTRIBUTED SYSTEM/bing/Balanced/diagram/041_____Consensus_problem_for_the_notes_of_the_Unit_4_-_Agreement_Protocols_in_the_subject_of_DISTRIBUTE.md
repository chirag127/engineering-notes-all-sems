### Consensus problem for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

- The consensus problem is the problem of getting a set of nodes in a distributed system to agree on something - it might be a value, a course of action or a decision.
- Achieving consensus allows a distributed system to act as a single entity, with every individual node aware of and in agreement with the actions of the whole of the network.
- Consensus is a general agreement on a decision made by the majority of those involved.
- Consensus is needed in a distributed system to ensure overall system reliability on top of unreliable system components.
- Consensus is also needed to coordinate the actions of different nodes, such as committing transactions, electing leaders, replicating data, etc.
- Consensus is hard to achieve in a distributed system due to the possibility of failures, such as node crashes, network partitions, message losses, etc.
- Consensus algorithms are protocols that enable nodes to reach consensus in a distributed system despite failures.
- Consensus algorithms can vary in terms of security and performance, depending on the assumptions and guarantees they make.
- Some examples of consensus algorithms are Two-Phase Commit, Three-Phase Commit, Paxos, Raft, etc.
- Consensus algorithms can be classified into two categories: crash-fault tolerant (CFT) and Byzantine-fault tolerant (BFT).
- CFT algorithms assume that nodes can only fail by crashing, and they can tolerate up to half of the nodes failing.
- BFT algorithms assume that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, and they can tolerate up to one-third of the nodes failing.
- BFT algorithms are more secure but less performant than CFT algorithms.