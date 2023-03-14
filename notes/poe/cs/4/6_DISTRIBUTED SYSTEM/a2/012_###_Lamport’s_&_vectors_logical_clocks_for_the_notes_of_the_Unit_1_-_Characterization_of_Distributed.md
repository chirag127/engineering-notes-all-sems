 Here is the content in markdown format for the topic ### Lamport’s & vectors logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Lamport's Logical Clocks

- Lamport's logical clocks are a mechanism to assign timestamps to events in a distributed system.
- They are logical clocks, not synchronized with real time. Their purpose is to establish a partial ordering of events.
- A process increments its clock before sending a message and includes this timestamp in the message.
- On receiving a message, a process takes the max of its clock and the timestamp in the message and uses this as the timestamp for any events that follow as a result of the message.
- This ensures that the timestamp of the sender is less than the timestamp of the receiver, thereby partially ordering the events.
- **Advantage:** Simple to implement. **Disadvantage:** Does not distinguish between events that are concurrent.

### Vector Clocks

- Vector clocks are a generalized version of Lamport clocks.
- A vector clock is a vector of logical clocks, one component for each process in the system.
- When a process sends a message, it includes the vector clock (VC) of the sending process in the message.
- On receiving a message, the receiver updates its VC to be a vector containing the max of the corresponding elements of the sender's VC and its own VC.
- Two events are concurrent if their vector clocks are component-wise greater than or equal to.
- **Advantage:** Can distinguish between concurrent events. **Disadvantage:** Requires more space than Lamport clocks.