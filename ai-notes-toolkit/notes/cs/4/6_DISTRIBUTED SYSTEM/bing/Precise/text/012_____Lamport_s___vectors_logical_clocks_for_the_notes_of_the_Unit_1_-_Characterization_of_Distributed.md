### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Lamport's logical clock is an algorithm used to order events in a distributed system.
- It assigns a logical timestamp to each event, which is used to determine the order of events.
- The algorithm works by assigning a counter to each process in the system. The counter is incremented whenever an event occurs within the process.
- When a message is sent from one process to another, the sender includes its current counter value in the message. The receiver then updates its own counter to be the maximum of its current value and the received value, plus one.
- Vector clocks are an extension of Lamport's logical clock, which can be used to determine the partial order of events in a distributed system.
- Each process maintains a vector of counters, one for each process in the system.
- When an event occurs within a process, the corresponding counter in the vector is incremented.
- When a message is sent from one process to another, the sender includes its entire vector in the message. The receiver then updates its own vector by taking the element-wise maximum of its current vector and the received vector, and then increments its own counter.
- Vector clocks can be used to determine if two events are causally related, concurrent, or if one event happened before the other.