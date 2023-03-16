### Logical Clocks

- Logical clocks are a mechanism used in distributed systems to provide a partial ordering of events.
- They are used to capture the causal relationships between events in a distributed system.
- Logical clocks are not based on physical time, but rather on the occurrence of events in the system.
- Each process in the system maintains its own logical clock, which is updated whenever an event occurs.
- When a process sends a message, it includes the current value of its logical clock in the message.
- When a process receives a message, it updates its logical clock to be greater than the maximum of its current value and the value received in the message.
- Logical clocks can be implemented using Lamport timestamps or vector clocks.
- Lamport timestamps are a simple implementation of logical clocks, where each process maintains a single integer value as its logical clock.
- Vector clocks are a more sophisticated implementation of logical clocks, where each process maintains a vector of integer values, one for each process in the system.
- Logical clocks are useful for detecting concurrency and causality in distributed systems, and can be used to implement algorithms for mutual exclusion, deadlock detection, and other distributed coordination tasks.