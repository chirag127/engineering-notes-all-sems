### Lamport’s & vectors logical clocks

Lamport’s logical clocks and vector clocks are algorithms used for ordering events in a distributed system. These algorithms are important for understanding the behavior of distributed systems and for implementing distributed algorithms.

#### Lamport’s Logical Clocks:

- Lamport’s logical clocks are based on the idea of associating a logical timestamp with each event in a distributed system.
- The logical timestamp is an integer value that represents the relative order of events in the system.
- The logical clock of a process is incremented whenever an event occurs at that process.
- When a message is sent from one process to another, the sender includes its current logical clock value in the message.
- When a process receives a message, it updates its logical clock to be the maximum of its current value and the timestamp in the received message, and then increments its clock by one.
- This ensures that the logical clocks of all processes in the system are consistent with the happened-before relation.

#### Vector Clocks:

- Vector clocks are an extension of Lamport’s logical clocks that provide more information about the relative ordering of events.
- In a vector clock, each process maintains a vector of logical clocks, one for each process in the system.
- The vector clock of a process is updated whenever an event occurs at that process, or when a message is sent or received.
- When a process sends a message, it includes its entire vector clock in the message.
- When a process receives a message, it updates its vector clock by taking the element-wise maximum of its current vector clock and the vector clock in the received message.
- This allows processes to determine the causal relationship between any two events in the system.

These algorithms are important for understanding the behavior of distributed systems and for implementing distributed algorithms such as mutual exclusion, deadlock detection, and global snapshots. They provide a way to order events in a distributed system and to reason about the causal relationships between events.