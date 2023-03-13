
### Lamport's & Vectors Logical Clocks for the Notes of the Unit 1 - Characterization of Distributed Systems in the Subject of DISTRIBUTED SYSTEM

Logical clocks are used to provide a partial ordering of events in distributed systems. Lamport's logical clock and vector clocks are two types of logical clocks that are used to order events in distributed systems.

##### Lamport's Logical Clock

Lamport's logical clock is a simple algorithm that assigns a timestamp to every event in a distributed system. It assigns a timestamp to each event based on the timestamp of the previous event and the current time. The timestamp of an event is the maximum of the timestamp of the previous event and the current time. This ensures that the timestamp of each event is unique and that the events are ordered correctly.

##### Mnemonic for Lamport's Logical Clock

A mnemonic for remembering Lamport's logical clock is "Max of Previous and Current".

##### Vector Clocks

Vector clocks are an extension of Lamport's logical clock and are used to order events in distributed systems. Vector clocks assign a vector of timestamps to each event. The vector contains the timestamp of the event in each process in the distributed system. The timestamp of an event is the maximum of the timestamps of the previous event and the current time in each process. This ensures that the timestamps of the events are unique and that the events are ordered correctly.

##### Mnemonic for Vector Clocks

A mnemonic for remembering vector clocks is "Max of Previous and Current in Each Process".

##### Advantages of Logical Clocks

- Logical clocks provide a partial ordering of events in distributed systems.
- Logical clocks are simple to implement and understand.
- Logical clocks are efficient in terms of time and space.

##### Disadvantages of Logical Clocks

- Logical clocks cannot be used to detect causality between events in distributed systems.
- Logical clocks can only provide a partial ordering of events in distributed systems.
- Logical clocks are not guaranteed to be accurate.