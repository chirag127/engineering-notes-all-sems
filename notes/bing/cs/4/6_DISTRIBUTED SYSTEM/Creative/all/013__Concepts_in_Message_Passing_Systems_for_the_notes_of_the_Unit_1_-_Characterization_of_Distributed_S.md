### Concepts in Message Passing Systems for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Message passing is a form of inter-process communication (IPC) in distributed systems, where processes communicate by sending and receiving messages over a communication channel .
- Message passing can be used for both local and distant communication, where the communicating processes are located on the same node or on different nodes.
- Message passing can be synchronous or asynchronous, depending on whether the sender and receiver processes are blocked or not until the message is delivered.
- Message passing can be reliable or unreliable, depending on whether the message is guaranteed to be delivered or not, and whether it is delivered in the same order as it was sent or not.
- Message passing can be unicast, multicast, broadcast, or anycast, depending on whether the message is sent to one, many, all, or any process in the system.
- Message passing can be implemented using various protocols, such as TCP, UDP, HTTP, MQTT, AMQP, etc., depending on the requirements and characteristics of the system .
- Message passing can be used for various purposes, such as data transfer, synchronization, coordination, fault tolerance, load balancing, etc., in distributed systems .

Some advantages of message passing are:

- It is simple and intuitive to use, as it abstracts away the details of the network and the platforms.
- It is scalable and flexible, as it can handle dynamic changes in the system and support heterogeneous components.
- It is modular and decoupled, as it allows processes to communicate without sharing memory or state.

Some disadvantages of message passing are:

- It can be inefficient and unreliable, as it involves overheads of serialization, transmission, and delivery of messages, and may suffer from network failures or congestion.
- It can be complex and ambiguous, as it requires explicit handling of message formats, protocols, and semantics, and may cause problems of consistency, ordering, and synchronization.
- It can be insecure and vulnerable, as it exposes messages to potential attacks or interceptions by malicious processes or nodes.

Some mnemonics and learning tricks for the message passing concepts are:

- To remember the types of message passing, use the acronym **SARUBA** (Synchronous, Asynchronous, Reliable, Unreliable, Broadcast, Anycast).
- To remember the types of communication, use the acronym **LUDM** (Local, Unicast, Distant, Multicast).
- To remember the purposes of message passing, use the acronym **DSCFLL** (Data transfer, Synchronization, Coordination, Fault tolerance, Load balancing, Logging).