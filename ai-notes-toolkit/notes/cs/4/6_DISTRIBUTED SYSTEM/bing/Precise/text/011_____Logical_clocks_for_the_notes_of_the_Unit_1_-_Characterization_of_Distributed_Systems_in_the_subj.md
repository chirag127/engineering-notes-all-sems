### Logical Clocks

- Logical clocks are used in distributed systems to provide a partial ordering of events.
- They are used to determine the order of events in a distributed system, where the physical clocks of the different processes may not be synchronized.
- A logical clock is a monotonically increasing software counter, which is updated according to certain rules.
- The most common implementation of logical clocks is Lamport's logical clock, which assigns a timestamp to each event in the system.
- The timestamp of an event is determined by the logical clock of the process where the event occurs.
- The logical clock of a process is incremented before the process sends a message, and the timestamp of the message is set to the value of the logical clock.
- When a process receives a message, it sets its logical clock to the maximum of its current value and the timestamp of the received message, and then increments it by one.
- Logical clocks provide a partial ordering of events, meaning that if event A happened before event B in the same process, then the timestamp of A will be less than the timestamp of B.
- However, if events A and B happened in different processes, their timestamps may not reflect their actual order of occurrence.
- Vector clocks are an extension of logical clocks that provide a total ordering of events in a distributed system.
- Vector clocks assign a vector of logical clocks to each event, where each element of the vector represents the logical clock of a process in the system.
- The vector clock of an event is updated according to certain rules, which ensure that the vector clocks of causally related events are ordered.
- Vector clocks can be used to determine the causal relationships between events in a distributed system.
