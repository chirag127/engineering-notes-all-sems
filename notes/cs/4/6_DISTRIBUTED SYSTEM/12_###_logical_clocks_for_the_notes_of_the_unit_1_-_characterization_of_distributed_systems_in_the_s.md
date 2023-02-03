### Logical clocks for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

Logical clocks are a way of assigning timestamps to events in a distributed system. They are used to order events that occur in different parts of the system, even when the clocks in those parts are not synchronized. The following are some common types of logical clocks:

1. Lamport Timestamps: A simple logical clock that assigns a unique timestamp to each event in the system. The timestamp is incremented each time an event occurs.

2. Vector Clocks: A logical clock that assigns a vector of timestamps to each event in the system. The vector contains a timestamp for each process in the system.

3. Interval Tree Clocks: A logical clock that assigns a set of intervals to each event in the system. The intervals represent the possible values of the logical clock at the time of the event.

Logical clocks are used to order events in a distributed system, to detect causality relationships between events, and to resolve conflicts in replicated data. They are an important tool for understanding and managing the behavior of distributed systems.
