### Lamport’s & Vectors Logical Clocks

Distributed systems are complex systems that have multiple components communicating with each other. One of the most important requirements of distributed systems is to maintain consistency among different components. In order to achieve consistency, we need to have a mechanism to order events in a distributed system. Logical clocks are used to order events in a distributed system.

Lamport’s logical clocks and vector clocks are two of the most widely used logical clocks in distributed systems. In this section, we will discuss Lamport’s logical clocks and vector clocks.

#### Lamport’s Logical Clocks

Lamport’s logical clocks were introduced by Leslie Lamport in 1978. The idea behind Lamport’s logical clocks is to assign a timestamp to each event in a distributed system. The timestamp is a logical value that represents the order of events. The timestamp is assigned to each event based on the happened-before relationship. The happened-before relationship defines the ordering of events in a distributed system.

The rules for assigning timestamps using Lamport’s logical clocks are as follows:

- Each event is assigned a unique timestamp.
- If event A happens before event B, then the timestamp of event A is less than the timestamp of event B.
- If event A and event B are concurrent, then the timestamps of event A and event B can be equal.

Lamport’s logical clocks are simple to implement and require minimal resources. However, they do not take into account the causal relationship between events. This means that events that are not causally related can have the same timestamp.

#### Vector Clocks

Vector clocks were introduced by Colin Fidge and Alan Demers in 1987. Vector clocks are an extension of Lamport’s logical clocks. Vector clocks maintain the causal relationship between events.

In vector clocks, each process maintains a vector of timestamps. The vector has an entry for each process in the distributed system. Each entry in the vector represents the timestamp of the last event that the corresponding process has seen. The vector is updated whenever a process sends or receives a message.

The rules for updating the vector using vector clocks are as follows:

- When a process sends a message, it updates its own timestamp in the vector and includes the vector in the message.
- When a process receives a message, it updates its own timestamp in the vector and merges the received vector with its own vector.
- The entry in the vector corresponding to the process that sent the message is incremented by one.

Vector clocks are more complex than Lamport’s logical clocks but provide a more accurate ordering of events in a distributed system. Vector clocks take into account the causal relationship between events and ensure that causally related events are ordered correctly.

In conclusion, both Lamport’s logical clocks and vector clocks are useful tools for maintaining consistency in distributed systems. While Lamport’s logical clocks are simple and easy to implement, vector clocks provide a more accurate ordering of events by maintaining the causal relationship between events.