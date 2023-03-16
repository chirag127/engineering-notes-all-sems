### Logical Clocks

Logical clocks are an essential concept in the characterization of distributed systems. Here are some key points to remember:

1. A logical clock is a mechanism for capturing the causal relationships between events in a distributed system.
2. Logical clocks are used to assign timestamps to events in a distributed system, which can be used to determine the order of events.
3. Logical clocks do not measure the actual time, but rather the relative order of events.
4. There are two main types of logical clocks: Lamport clocks and vector clocks.
5. Lamport clocks assign a unique timestamp to each event, based on the number of events that have occurred in the system.
6. Vector clocks assign a vector of timestamps to each event, where each element of the vector represents the number of events that have occurred at each process in the system.
7. Logical clocks can be used to solve problems such as mutual exclusion and deadlock detection in distributed systems.
