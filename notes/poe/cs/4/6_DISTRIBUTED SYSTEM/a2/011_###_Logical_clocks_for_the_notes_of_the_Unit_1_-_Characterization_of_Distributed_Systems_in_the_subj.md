 Here is the content in markdown format:

### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Logical clocks are a mechanism to assign timestamps to events in a distributed system. They are used to partially order events and detect causality violations.

- Lamport timestamps: Lamport timestamps are logical clocks that assign an integer timestamp to events. Each process increments its counter and assigns the new value as timestamp to new events. When a message is sent, it carries the timestamp of the sender. Upon receiving a message, the receiver picks the greater of its own timestamp and the received timestamp, and uses this value to timestamp the event of reception and any subsequent local events. This ensures that the timestamp of the reception of a message is greater than the timestamp of the send event.
- Vector clocks: Vector clocks are a logical clock mechanism that assigns a vector of integer clocks to processes. Each element represents the clock of a process. Upon an event, a process increments its own clock element. When a message is sent, the vector clock is attached. Upon receiving a message, the receiver component-wise picks the greater value of its own and received vector clock and uses it to timestamp the reception event. This enables detection of causal relationships between events at different processes.

Advantages:

- Simple to implement
- Detect causal relationships and ordering
- Do not require synchronization

Disadvantages:

- Do not measure absolute time
- Scalability - vector clock size grows with number of processes

Applications:

- Distributed debugging
- Distributed concurrency control
- Replication synchronization