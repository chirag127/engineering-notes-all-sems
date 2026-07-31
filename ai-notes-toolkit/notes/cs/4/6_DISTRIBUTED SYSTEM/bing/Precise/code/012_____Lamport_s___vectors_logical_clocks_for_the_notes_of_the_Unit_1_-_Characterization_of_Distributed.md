### Lamport’s & vectors logical clocks

Lamport’s logical clocks and vector clocks are algorithms used for ordering events in a distributed system.

#### Lamport’s Logical Clocks:

- Lamport’s logical clocks are based on the idea of a logical clock, which is a monotonically increasing software counter.
- Each process in the system maintains its own logical clock.
- The clock is incremented before each event in the process.
- When a process sends a message, it includes the current value of its logical clock in the message.
- When a process receives a message, it sets its logical clock to the maximum of its current value and the timestamp in the received message, and then increments it by one.
- This ensures that the timestamps of events in the system are consistent with the happened-before relation.

#### Vector Clocks:

- Vector clocks extend the idea of logical clocks by maintaining a vector of logical clocks, one for each process in the system.
- Each process maintains its own vector clock, which is an array of n logical clocks, where n is the number of processes in the system.
- When a process experiences an internal event, it increments its own entry in its vector clock.
- When a process sends a message, it includes its entire vector clock in the message.
- When a process receives a message, it updates each entry in its vector clock to the maximum of the current value and the corresponding value in the received message, and then increments its own entry by one.
- This allows the system to capture the happened-before relation between events in different processes.

These algorithms are used to provide a partial ordering of events in a distributed system, which is useful for various applications such as debugging, distributed algorithms, and distributed databases. They are an important tool for understanding and reasoning about the behavior of distributed systems.