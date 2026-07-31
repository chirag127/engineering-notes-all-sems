### System models for the notes of the Unit 4 - Agreement Protocols in the subject of DISTRIBUTED SYSTEM

A system model is a description of the properties and assumptions of a distributed system that are relevant for its design and analysis. System models can help us understand the behavior, limitations, and challenges of distributed systems, as well as compare and evaluate different solutions.

There are different types of system models, depending on the aspects of the system that we want to focus on. Some of the most common system models are:

- **Architectural models**: These models capture the hardware composition of a system in terms of computers and other devices and their interconnecting network. They also describe the responsibilities and placement of system components, such as clients, servers, peers, brokers, etc. Architectural models can help us design the structure and communication patterns of a distributed system.

- **Interaction models**: These models capture the communication and coordination mechanisms of a system, such as message passing, remote procedure calls, publish-subscribe, shared memory, etc. They also describe the properties and guarantees of these mechanisms, such as reliability, ordering, atomicity, consistency, etc. Interaction models can help us design the protocols and algorithms of a distributed system.

- **Fault models**: These models capture the possible failures and errors that can occur in a system, such as node crashes, network partitions, message losses, corrupted data, etc. They also describe the assumptions and expectations of the system in the presence of faults, such as fault detection, fault tolerance, fault recovery, etc. Fault models can help us design the resilience and reliability of a distributed system.

- **Timing models**: These models capture the temporal aspects of a system, such as clock synchronization, time bounds, latency, throughput, etc. They also describe the assumptions and expectations of the system in terms of timing, such as synchrony, asynchrony, partial synchrony, etc. Timing models can help us design the performance and scalability of a distributed system.

- **Consensus models**: These models capture the problem of achieving agreement among a set of nodes in a system, such as electing a leader, committing a transaction, ordering events, etc. They also describe the assumptions and expectations of the system in terms of consensus, such as safety, liveness, termination, etc. Consensus models can help us design the correctness and consistency of a distributed system.

Some examples of system models for distributed systems are:

- **Client-server model**: This is an architectural model where the system consists of two types of components: clients and servers. Clients request services from servers, and servers provide services to clients. Servers can be centralized or distributed, and clients can be thin or thick. This model is widely used for web applications, databases, file systems, etc.

- **Peer-to-peer model**: This is an architectural model where the system consists of a set of peers that are equal and autonomous. Peers can act as both clients and servers, and can communicate and cooperate with each other. Peers can form structured or unstructured overlays, and can join or leave the system dynamically. This model is widely used for file sharing, streaming, distributed hash tables, etc.

- **Message passing model**: This is an interaction model where the system uses messages as the basic unit of communication. Messages can be sent and received by nodes using various protocols, such as TCP, UDP, HTTP, etc. Messages can have different properties and guarantees, such as reliability, ordering, delivery, etc. This model is widely used for distributed algorithms, middleware, distributed objects, etc.

- **Publish-subscribe model**: This is an interaction model where the system uses events as the basic unit of communication. Events can be published by nodes to topics, and can be subscribed by nodes that are interested in those topics. Events can have different properties and guarantees, such as reliability, ordering, filtering, etc. This model is widely used for event-driven systems, notification systems, data streams, etc.

- **Crash-recovery model**: This is a fault model where the system assumes that nodes can fail by crashing, but can recover after some time. Nodes can have persistent or volatile state, and can use checkpoints or logs to recover their state. Nodes can detect failures by using timeouts or heartbeats, and can tolerate failures by using replication or redundancy. This model is widely used for distributed databases, distributed file systems, distributed transactions, etc.

- **Byzantine model**: This is a fault model where the system assumes that nodes can fail in arbitrary ways, such as sending incorrect or malicious messages, deviating from the protocol, colluding with other nodes, etc. Nodes can have different trust levels,