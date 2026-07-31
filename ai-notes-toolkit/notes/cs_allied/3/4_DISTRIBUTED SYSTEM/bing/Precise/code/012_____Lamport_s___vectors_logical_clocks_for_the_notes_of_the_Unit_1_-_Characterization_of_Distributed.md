### Lamport’s & vectors logical clocks

Lamport’s logical clocks and vector clocks are algorithms used for ordering events in a distributed system. These algorithms are important for understanding the behavior of distributed systems and for implementing distributed algorithms.

#### Lamport’s Logical Clocks

- Lamport’s logical clocks are based on the idea of associating a logical timestamp with each event in a distributed system.
- The logical timestamps are used to order events in a way that is consistent with the causal relationships between events.
- The basic idea is that each process in the system maintains a logical clock, which is a counter that is incremented whenever an event occurs at that process.
- When a process sends a message, it includes the current value of its logical clock in the message.
- When a process receives a message, it updates its logical clock to be greater than the maximum of its current value and the timestamp in the received message.
- This ensures that the logical timestamps of events reflect the causal relationships between events.

#### Vector Clocks

- Vector clocks are an extension of Lamport’s logical clocks that provide more information about the causal relationships between events.
- In a vector clock, each process maintains a vector of logical clocks, one for each process in the system.
- The vector clock of a process is updated whenever an event occurs at that process, and whenever a message is sent or received.
- When a process sends a message, it includes its entire vector clock in the message.
- When a process receives a message, it updates its vector clock by taking the element-wise maximum of its current vector clock and the vector clock in the received message.
- This allows processes to determine not only the order of events, but also whether two events are causally related or concurrent.

These algorithms are important for understanding the behavior of distributed systems and for implementing distributed algorithms. They provide a way to order events in a distributed system in a way that is consistent with the causal relationships between events. This is essential for many distributed algorithms, such as distributed mutual exclusion and distributed snapshot algorithms.