### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM
Lamport's Logical Clocks: 
- A distributed system's time synchronization mechanism 
- Assigns unique timestamps to events in a way that reflects causality 
- Each process has its own logical clock and updates it before executing an event 
- A process's clock is incremented by 1 before an event, or set to max(local_clock, received_clock) + 1 if receiving a message from another process 

Vector Clocks: 
- An extension of Lamport's logical clocks 
- Each process has a vector of logical clocks, one for each process in the system 
- A process increments its own clock before executing an event 
- A process updates its own vector entry for a received message's sender 
- Vector clocks reflect partial ordering of events, allowing for detection of causality violations.
