### Theoretical Foundation for Distributed System

A distributed system is a collection of processes that are spatially separated and do not share a common memory and communicate with one another by exchanging messages with arbitrary delays .

Some of the theoretical foundations for distributed systems are:

- **Limitations of distributed systems**: Due to the lack of a global clock, shared memory, and reliable communication, distributed systems face some inherent challenges such as synchronization, consistency, fault tolerance, and scalability .
- **Logical clocks**: Logical clocks are a way of ordering events in a distributed system based on their causal relationships, rather than their physical timestamps. Logical clocks can be implemented using Lamport's clocks or vector clocks, which assign logical timestamps to events and messages that reflect their partial or total order .
- **Concepts in message passing systems**: Message passing systems are a model of distributed computation where processes communicate by sending and receiving messages. Some of the concepts in message passing systems are: message types, message ordering, message delivery, message buffering, message passing primitives, and message passing protocols .