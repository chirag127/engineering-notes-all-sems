### Theoretical Foundation for Distributed System

- A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .
- Theoretical foundation for distributed system aims to understand the inherent limitations, capabilities, and trade-offs of a distributed system and to develop mathematical models and algorithms for solving problems in a distributed environment  .
- Some of the topics covered by the theoretical foundation for distributed system are:
  - Limitation of distributed system: such as the impossibility of consensus, the lower bounds on communication and computation, the effects of failures and asynchrony, the complexity of coordination and synchronization, etc  .
  - Absence of global clock: the lack of a common notion of time among the processes in a distributed system and the challenges of ordering events and ensuring consistency and causality  .
  - Shared memory: the abstraction of a global memory that can be accessed by all processes in a distributed system and the issues of concurrency control, replication, consistency models, and fault tolerance  .
  - Logical clocks: the mechanisms for assigning logical timestamps to events in a distributed system and for comparing the order of events based on their timestamps, such as Lamport's logical clocks and vector clocks    .
  - Concepts in message passing system: the principles and techniques for designing and implementing distributed algorithms that use message passing as the communication paradigm, such as leader election, mutual exclusion, distributed snapshots, termination detection, etc   .