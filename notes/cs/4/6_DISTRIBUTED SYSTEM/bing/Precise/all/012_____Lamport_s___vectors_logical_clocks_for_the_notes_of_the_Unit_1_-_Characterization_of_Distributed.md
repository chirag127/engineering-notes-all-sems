# Lamport’s & vectors logical clocks

Lamport’s Logical Clock and Vector Clock are two algorithms used to determine the order of events in a distributed system.

## Lamport’s Logical Clock
- Created by Leslie Lamport.
- It is a procedure to determine the order of events occurring.
- Provides a basis for the more advanced Vector Clock Algorithm.
- Needed due to the absence of a Global Clock in a Distributed Operating System.

## Vector Clock
- Extends the capabilities of Lamport Clocks to allow us to understand the ordering across multiple processes which cross communicate.
- Can be invaluable in understanding the flow of messages in a distributed system.
- At a data level, Vector clocks are vectors of event counters.
- Inter-process messages contain the state of the sending process's logical clock.
- A vector clock of a system of N processes is an array/vector of N logical clocks, one clock per process.
- A local "largest possible values" copy of the global clock-array is kept in each process.

## Difference between Lamport timestamps and Vector clocks
- Both Lamport timestamps and vector clocks are logical clocks.
- Both provide a total ordering of events consistent with causality.
- Vector clocks allow you to determine if any two arbitrarily selected events are causally dependent or concurrent.
- Lamport timestamps cannot do this.
- Lamport timestamps are more compact.