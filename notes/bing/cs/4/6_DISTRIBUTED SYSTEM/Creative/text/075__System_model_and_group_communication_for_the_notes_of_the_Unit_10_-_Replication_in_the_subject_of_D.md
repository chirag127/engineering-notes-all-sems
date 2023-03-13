### System model and group communication for replication in distributed system

- A system model is a set of assumptions and properties that describe the behavior and characteristics of a distributed system, such as the communication network, the failure modes, the timing constraints, and the consistency guarantees.
- A group communication is a mechanism that allows one or more processes to send messages to a group of processes, and to receive messages from the group, in a reliable and ordered way.
- Replication is a technique that creates and maintains multiple copies of the same data or service on different nodes in a distributed system, for the purposes of fault tolerance, availability, and performance  .
- Some of the challenges and trade-offs of replication are:
  - How to ensure consistency among replicas, especially in the presence of concurrent updates and network partitions .
  - How to balance the load among replicas, and how to handle dynamic changes in the system, such as failures, recoveries, and migrations .
  - How to minimize the communication and storage overhead of replication, and how to optimize the performance and latency of read and write operations .
- Some of the models and methods for replication are:
  - Primary-backup replication: A single replica is designated as the primary, and the others are backups. The primary receives all the update requests, and propagates them to the backups. The backups only serve read requests, and take over the primary role in case of failure .
  - Quorum-based replication: Each replica has a vote, and a quorum is a subset of replicas that has enough votes to perform an operation. A read quorum and a write quorum are defined, such that any two quorums of the same type or different types have a non-empty intersection. A read or write operation can proceed only if a quorum of the corresponding type is available .
  - State machine replication: Each replica executes the same deterministic state machine, and the state machine transitions are triggered by the same sequence of commands. A consensus protocol is used to ensure that all replicas agree on the order of commands. A state machine replica can serve both read and write requests .
  - Peer-to-peer replication: Each replica is equal, and can receive both read and write requests. A conflict resolution mechanism is used to handle concurrent or divergent updates. A gossip protocol is used to disseminate updates among replicas in a probabilistic way .
- Some of the protocols and standards for group communication and replication are:
  - IP multicast: A network layer protocol that allows a process to send a message to a group of processes, identified by a multicast address, using a single network transmission.
  - Virtual synchrony: A group communication model that ensures that all processes in a group see the same sequence of messages, and that the membership changes of the group are synchronized with the message delivery.
  - Paxos: A consensus protocol that allows a set of processes to agree on a single value, despite the possibility of failures and asynchrony.
  - Raft: A consensus protocol that is similar to Paxos, but simpler and more understandable. It uses a leader election mechanism and a log replication algorithm to ensure consistency among replicas.
  - CRDT: A data structure that can be replicated across multiple nodes, and can be updated without coordination. It guarantees that all replicas will eventually converge to the same state, even if they receive updates in different orders or concurrently.