### Lamport’s & Vectors Logical Clocks

Distributed systems are systems composed of multiple independent components that collaborate and communicate with each other to achieve a common goal. In such systems, it becomes necessary to order the events that are happening across different components. This is where logical clocks come into play.

Logical clocks are a mechanism used in distributed systems to order the events that occur across different components. Lamport’s and vector logical clocks are two popular mechanisms used in distributed systems.

#### Lamport’s Logical Clocks

- Lamport’s logical clocks are a mechanism used to order the events that take place in a distributed system.
- Each process in the system maintains a logical clock that represents the order of events that occur in that process.
- When an event occurs in a process, the process increments its logical clock and assigns the value to the event.
- The logical clock value of an event reflects the order in which it occurred, across all processes in the system.
- However, Lamport’s logical clocks do not guarantee a global ordering of events, as events that occur concurrently may have the same logical clock value.

#### Vector Logical Clocks

- Vector logical clocks are an extension of Lamport’s logical clocks and provide a mechanism to order events across multiple processes in a distributed system.
- Each process in the system maintains a vector clock that represents the order of events that occur in that process as well as in other processes.
- When an event occurs in a process, the process increments its own entry in the vector clock and assigns the value to the event.
- The vector clock value of an event reflects the order in which it occurred across all processes in the system.
- Vector logical clocks guarantee a global ordering of events, as events that occur concurrently are ordered based on the vector clock values.

In conclusion, logical clocks are an essential mechanism for ordering events in distributed systems. Lamport’s and vector logical clocks are two popular mechanisms used in distributed systems. While Lamport’s logical clocks provide a mechanism to order events within a single process, vector logical clocks provide a mechanism to order events across multiple processes.