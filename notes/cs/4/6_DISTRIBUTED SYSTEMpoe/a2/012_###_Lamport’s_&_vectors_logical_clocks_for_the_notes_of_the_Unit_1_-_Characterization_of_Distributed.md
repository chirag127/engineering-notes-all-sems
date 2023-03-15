 Here is the content in markdown format for the topic ### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Lamport's Logical Clocks

- Lamport's logical clocks are a mechanism to partially order events in a distributed system.
- Each process maintains a logical clock, which is a counter of the number of events that have occurred at that process.
- The logical clock is incremented whenever a new event occurs at the process.
- When a process sends a message, it attaches its current logical clock value to the message.
- When a process receives a message, it updates its own logical clock to the greater of its current clock value and the clock value of the received message plus one.
- The logical clock values can be used to partially order events based on the following rules:
    - If event A happens before event B in the same process, then clock(A) < clock(B)
    - If event A sends a message m and event B receives message m, then clock(A) < clock(B)

Advantages:

- Simple to implement.
- Useful for detecting causal relationships between events.

Disadvantages:

- Does not capture synchronization between processes.
- Does not provide a total ordering of events.

Vectors Logical Clocks

- Vectors logical clocks extend Lamport's logical clocks to capture process synchronization.
- Each process maintains a vector of logical clocks, one component per process in the system.
- When a process sends a message, it includes the vector of its current clocks.
- When a process receives a message, it updates its clock vector to have the greater value of its corresponding component and the corresponding component of the received message vector plus one.
- The vectors can be used to totally order events using a lexicographic ordering.

Advantages:

- Captures synchronization between processes.
- Provides a total ordering of events.

Disadvantages:

- More complex to implement than Lamport's logical clocks.
- Clock values may grow unboundedly.