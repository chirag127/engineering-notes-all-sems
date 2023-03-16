### Logical Clocks

Logical clocks are an essential concept in the characterization of distributed systems. Here are some key points to remember:

1. A logical clock is a mechanism for capturing the causal relationships between events in a distributed system.
2. Logical clocks are used to assign timestamps to events in a distributed system, allowing the system to determine the order in which events occurred.
3. Logical clocks are not based on physical time, but rather on the ordering of events within the system.
4. There are two main types of logical clocks: Lamport clocks and vector clocks.
5. Lamport clocks assign a single timestamp to each event, while vector clocks assign a vector of timestamps to each event.
6. Logical clocks are used in distributed algorithms, such as mutual exclusion and distributed snapshots, to ensure that the algorithm behaves correctly in the presence of concurrency and failures.
