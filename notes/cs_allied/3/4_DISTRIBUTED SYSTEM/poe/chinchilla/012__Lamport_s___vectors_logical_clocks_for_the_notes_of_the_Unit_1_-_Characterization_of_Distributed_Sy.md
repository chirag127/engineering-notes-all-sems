### Lamport’s & Vectors Logical Clocks

Distributed systems are designed to work efficiently with multiple nodes communicating with each other. However, maintaining consistency among these nodes is a challenging task. One way to achieve this is by implementing logical clocks on each node that keep track of the order of events.

Lamport’s Logical Clocks
- Lamport’s logical clocks are a simple mechanism for ordering events in a distributed system.
- Each node in the system maintains a logical clock that assigns a unique timestamp to each event.
- The timestamp is a logical value that is incremented for each event.
- A timestamp is assigned to an event when it occurs at a particular node, and the timestamp is sent along with the event to other nodes.
- The receiving node updates its logical clock value to the maximum value of its current timestamp and the received timestamp plus one.
- The ordering of events is determined by comparing their logical timestamps.

Vector Clocks
- Vector clocks are an extension of Lamport’s logical clocks.
- In vector clocks, each node maintains a vector of logical clock values, one for each node in the system.
- Each vector entry represents the logical clock value for a particular node in the system.
- When an event occurs, the logical clock value for the node where the event occurred is incremented, and the resulting vector is sent with the event to other nodes.
- When a node receives a vector, it updates its own vector by taking the maximum value of each entry in its own vector and the corresponding entry in the received vector.
- The ordering of events is determined by comparing the vector clocks of each event.

Conclusion
- Logical clocks are a critical component of distributed systems that ensure consistency among nodes.
- Lamport’s logical clocks are a simple mechanism for ordering events in a distributed system, while vector clocks are an extension that provides more complex ordering mechanisms.
- Implementing logical clocks requires careful consideration of the size and complexity of the system, as well as the potential for clock skew and other errors.