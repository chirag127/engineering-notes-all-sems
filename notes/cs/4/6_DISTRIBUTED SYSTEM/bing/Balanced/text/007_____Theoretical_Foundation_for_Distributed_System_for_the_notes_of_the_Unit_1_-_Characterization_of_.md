### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundation for distributed system aims to understand the inherent limitations, capabilities and trade-offs of a distributed system and to develop abstract models, algorithms and techniques for solving problems in a distributed environment .
- Some of the topics covered by the theoretical foundation for distributed system are:
  - Limitation of distributed system: such as impossibility of consensus, failure detection, global state, mutual exclusion, etc. in the presence of failures, asynchrony or uncertainty .
  - Absence of global clock: the lack of a common notion of time or ordering of events in a distributed system and the need for synchronization mechanisms  .
  - Shared memory: the abstraction of a global memory that can be accessed by all processes in a distributed system and the challenges of consistency, coherence, replication, etc. in implementing it .
  - Logical clocks: the methods of assigning logical timestamps to events in a distributed system and the properties of causality, concurrency and partial ordering they capture   .
  - Lamport's and vector logical clocks: the two types of logical clocks that are widely used in distributed systems and their advantages and disadvantages   .
  - Concepts in message passing system: the communication model that relies on sending and receiving messages between processes in a distributed system and the issues of reliability, ordering, buffering, routing, etc. in it .