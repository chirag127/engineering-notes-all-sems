### Lamport’s & vectors logical clocks

#### Lamport’s Logical Clock
- Lamport’s Logical Clock was created by Leslie Lamport. 
- It is a procedure to determine the order of events occurring. 
- It provides a basis for the more advanced Vector Clock Algorithm. 
- Due to the absence of a Global Clock in a Distributed Operating System, Lamport Logical Clock is needed. 
- A Lamport logical clock is a numerical software counter value maintained in each process. 
- Conceptually, this logical clock can be thought of as a clock that only has meaning in relation to messages moving between processes. 
- When a process receives a message, it re-synchronizes its logical clock with that sender. 

#### Vector Clocks
- Vector Clocks extend the capabilities of Lamport Clocks to allow us to understand the ordering across multiple processes which cross communicate. 
- They can also be invaluable in understanding the flow of messages in a distributed system. 
- As a data level, Vector clocks are vectors of event counters. 
- Just as in Lamport timestamps, inter-process messages contain the state of the sending process's logical clock. 
- A vector clock of a system of N processes is an array/vector of N logical clocks, one clock per process. 
- A local "largest possible values" copy of the global clock-array is kept in each process. 
- Vector clocks allow you to determine if any two arbitrarily selected events are causally dependent or concurrent. 
- Lamport timestamps cannot do this. 
- Lamport timestamps are more compact.