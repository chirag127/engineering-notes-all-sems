### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Logical clocks are a way of assigning timestamps to events in a distributed system. The goal of logical clocks is to provide a partial ordering of events that occur across multiple nodes in the system. Logical clocks differ from physical clocks in that they do not rely on a single, global time source. Instead, each node in the system maintains its own logical clock.

There are two main types of logical clocks: vector clocks and Lamport clocks. 

1. Vector clocks: In a vector clock, each node in the system maintains a vector of timestamps, one for each node in the system. When a node generates an event, it increments its own timestamp in the vector and sends the updated vector to other nodes. 

2. Lamport clocks: In a Lamport clock, each node in the system maintains a single timestamp. When a node generates an event, it increments its own timestamp and sends the updated timestamp to other nodes. 

Both vector clocks and Lamport clocks provide a partial ordering of events. This means that they can be used to determine the order in which events occurred, but they do not provide a total ordering of events.

Logical clocks are important in distributed systems because they provide a way of assigning timestamps to events that occur across multiple nodes. This allows for the ordering of events, which is important for tasks such as conflict resolution and consistency maintenance.

In conclusion, logical clocks are a key tool in the characterization of distributed systems. They provide a way of assigning timestamps to events that occur across multiple nodes, allowing for the ordering of events and the resolution of conflicts.
