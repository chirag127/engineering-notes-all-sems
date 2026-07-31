### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Lamport’s logical clocks and vector clocks are algorithms used for ordering events in a distributed system.
- Lamport’s logical clocks algorithm is based on the idea of assigning a logical timestamp to each event in the system, which is used to determine the order of events.
- The algorithm works by assigning a logical clock value to each process in the system, which is incremented each time an event occurs at that process.
- When a message is sent from one process to another, the sender includes its current logical clock value in the message. The receiver then updates its own logical clock value to be the maximum of its current value and the value received in the message, plus one.
- Vector clocks extend the idea of Lamport’s logical clocks by maintaining a vector of logical clock values, one for each process in the system.
- Each process increments its own entry in the vector each time an event occurs, and when a message is sent, the entire vector is included in the message.
- The receiver then updates its own vector by taking the element-wise maximum of its current vector and the vector received in the message.
- Vector clocks provide more information about the causal relationships between events than Lamport’s logical clocks, as they can distinguish between concurrent events.
- Both Lamport’s logical clocks and vector clocks are useful tools for reasoning about the behavior of distributed systems and for implementing distributed algorithms.