### Lamport’s & Vectors Logical Clocks

Distributed systems are complex and require a way to synchronize events that occur across different nodes. One way to do this is by using logical clocks. There are two types of logical clocks: Lamport’s logical clocks and vector clocks.

#### Lamport’s Logical Clocks

1. Lamport’s logical clocks are a way to order events in a distributed system.
2. Each node has its own logical clock that is incremented whenever an event occurs.
3. The value of the clock is included in the message sent between nodes.
4. When a node receives a message, it updates its own logical clock based on the value of the clock in the message.
5. If two events have the same value in their logical clocks, then they are concurrent.
6. If one event has a lower value than another event in its logical clock, then it occurred before the other event.

#### Vector Clocks

1. Vector clocks are an extension of Lamport’s logical clocks.
2. Each node has a vector clock that contains a clock value for every node in the system.
3. When an event occurs, the node increments its own clock value in the vector clock and includes the entire vector clock in the message sent to other nodes.
4. When a node receives a message, it updates its own vector clock based on the vector clock in the message.
5. If two events have the same vector clock values, then they are concurrent.
6. If one event has a lower value than another event in a particular element of the vector clock, then it occurred before the other event.

In conclusion, both Lamport’s logical clocks and vector clocks are useful in ordering events in a distributed system. Lamport’s logical clocks are simpler and easier to implement, while vector clocks provide more information about the ordering of events.