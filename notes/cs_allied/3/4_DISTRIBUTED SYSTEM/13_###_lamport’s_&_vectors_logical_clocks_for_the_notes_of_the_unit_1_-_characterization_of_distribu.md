### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Lamport's and Vector Logical Clocks are techniques for resolving the problem of causality in distributed systems.

Lamport's Logical Clock is a simple and efficient mechanism for assigning a unique timestamp to events in a distributed system. Each process in the system has its own logical clock, and when a process sends a message, it includes its current logical clock value. When a process receives a message, it updates its own logical clock value based on the value in the message and the current value of its own clock.

Vector Logical Clocks are an extension of Lamport's Logical Clock that keep track of the relative ordering of events across multiple processes. Each process has a vector of logical clock values, one for each process in the system, and the value of a process's own clock is updated based on the values in received messages and the current values of its own clock.

Both Lamport's Logical Clock and Vector Logical Clocks are used to resolve the problem of causality in distributed systems, allowing processes to determine the order of events and to detect concurrent events. They are essential for ensuring the consistency and reliability of distributed systems.

In conclusion, Lamport's Logical Clock and Vector Logical Clocks are techniques for resolving the problem of causality in distributed systems, allowing processes to determine the order of events and to detect concurrent events. Understanding these concepts is important for designing and building reliable and consistent distributed systems.
